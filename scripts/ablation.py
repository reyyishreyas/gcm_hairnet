import argparse
import sys
from pathlib import Path
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils.misc import get_device
from utils.ablation import AblationManager
from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from losses import build_loss
from models import build_model


def main():
    parser = argparse.ArgumentParser(description="Run ablation study")
    parser.add_argument("--config", type=str, default="train", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--output-dir", type=str, default="./outputs/tables", help="Output directory")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)

    val_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split="val",
        transforms=get_val_transforms(),
    )
    val_loader = build_dataloader(
        val_dataset,
        batch_size=config.get("dataset", {}).get("val_batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    checkpoint = torch.load(args.checkpoint, map_location=device)
    model.load_state_dict(checkpoint["model_state_dict"])
    model.to(device)
    model.eval()

    loss_fn = build_loss(config.get("training", {}).get("loss", {}))
    ablation_manager = AblationManager(model, config.to_dict() if hasattr(config, "to_dict") else config)
    results = ablation_manager.run_ablation(val_loader, loss_fn, device)

    import json
    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    with open(output_path / "ablation_results.json", "w") as f:
        json.dump(results, f, indent=2)

    ckpt_dir = Path("./checkpoints/ablation")
    ckpt_dir.mkdir(parents=True, exist_ok=True)
    torch.save({"model_state_dict": ablation_manager.model.state_dict()}, ckpt_dir / "ablated_model.pt")

    print("Ablation Results:")
    for module, metrics in results.items():
        if isinstance(metrics, dict):
            print(f"  {module}: loss={metrics['loss']:.4f}, relative_drop={metrics['relative_drop_percent']:.2f}%")
        else:
            print(f"  {module}: {metrics:.4f}")


if __name__ == "__main__":
    main()
