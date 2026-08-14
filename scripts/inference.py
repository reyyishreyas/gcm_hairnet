import argparse
import sys
from pathlib import Path
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from engine import Inferencer
from models import build_model
from utils.misc import get_device


def main():
    parser = argparse.ArgumentParser(description="Run inference with GCM-HAIRNet")
    parser.add_argument("--config", type=str, default="inference", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--split", type=str, default="test", help="Data split to use")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--output-dir", type=str, default="./outputs/inference", help="Output directory")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)

    dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split=args.split,
        transforms=get_val_transforms(),
    )
    data_loader = build_dataloader(
        dataset,
        batch_size=config.get("inference", {}).get("batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    inferencer = Inferencer(
        model=model,
        data_loader=data_loader,
        checkpoint_path=args.checkpoint,
        device=device,
        output_dir=args.output_dir,
        save_predictions=config.get("inference", {}).get("save_predictions", True),
        save_visualizations=config.get("inference", {}).get("save_visualizations", True),
    )

    results = inferencer.run()
    print(f"Predictions saved to {args.output_dir}")
    print(f"Shape: {results['predictions'].shape}")


if __name__ == "__main__":
    main()
