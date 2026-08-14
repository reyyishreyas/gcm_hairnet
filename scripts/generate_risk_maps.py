import argparse
from pathlib import Path
import sys
import torch
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from models import build_model
from utils.misc import get_device
from visualization import save_risk_maps, save_comparison_maps


def run_inference_for_split(split, config, device, checkpoint_path, output_base, root_dir):
    dataset = GCMHAIRNetDataset(
        root_dir=root_dir,
        split=split,
        transforms=get_val_transforms(),
    )
    loader = build_dataloader(
        dataset,
        batch_size=config.get("inference", {}).get("batch_size", 32),
        shuffle=False,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    checkpoint = torch.load(checkpoint_path, map_location=device)
    ckpt_state = checkpoint["model_state_dict"]
    model_state = model.state_dict()
    new_state = {}
    for key, param in ckpt_state.items():
        if key in model_state and param.shape == model_state[key].shape:
            new_state[key] = param
    model.load_state_dict(new_state, strict=False)
    model.to(device)
    model.eval()

    all_preds = []
    all_targets = []
    all_cities = []

    with torch.no_grad():
        for batch in loader:
            image = batch["image"].to(device, non_blocking=True)
            gis = batch["gis"].to(device, non_blocking=True)
            label = batch["label"].to(device, non_blocking=True)

            preds = torch.sigmoid(model(image, gis)).cpu().numpy()
            all_preds.append(preds)
            all_targets.append(label.cpu().numpy())
            all_cities.extend(batch.get("city_name", []))

    preds = np.concatenate(all_preds, axis=0)
    targets = np.concatenate(all_targets, axis=0)

    out_dir = Path(output_base) / split
    out_dir.mkdir(parents=True, exist_ok=True)

    np.save(out_dir / f"{split}_predictions.npy", preds)
    np.save(out_dir / f"{split}_targets.npy", targets)

    save_risk_maps(preds, all_cities, str(out_dir), cmap="hot")
    save_comparison_maps(preds, targets, all_cities, str(out_dir))

    print(f"[{split}] Saved {len(all_cities)} risk maps and comparisons to {out_dir}")


def main():
    parser = argparse.ArgumentParser(description="Generate risk maps for all cities")
    parser.add_argument("--config", type=str, default="inference", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--output-dir", type=str, default="./outputs/all_risk_maps", help="Output directory")
    parser.add_argument("--splits", nargs="+", default=["train", "val", "test"], help="Splits to process")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)

    for split in args.splits:
        try:
            run_inference_for_split(split, config, device, args.checkpoint, args.output_dir, args.root_dir)
        except Exception as e:
            print(f"Error processing split {split}: {e}")


if __name__ == "__main__":
    main()
