import argparse
import sys
from pathlib import Path

import torch
import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from models import GCMHAIRNet
from utils.misc import get_device


def main():
    parser = argparse.ArgumentParser(description="Diagnose model predictions")
    parser.add_argument("--config", type=str, default="train", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--split", type=str, default="val", help="Data split")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)

    dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split=args.split,
        transforms=get_val_transforms(),
    )
    loader = build_dataloader(
        dataset,
        batch_size=1,
        shuffle=False,
        num_workers=0,
        drop_last=False,
    )

    model = GCMHAIRNet(config.get("model", {}))
    checkpoint = torch.load(args.checkpoint, map_location=device)
    model.load_state_dict(checkpoint["model_state_dict"], strict=False)
    model.to(device)
    model.eval()

    print(f"Analyzing {len(dataset)} samples from {args.split} split")
    print("=" * 60)

    all_preds = []
    all_targets = []
    all_pred_mins = []
    all_pred_maxs = []
    all_pred_means = []
    all_pred_stds = []

    with torch.no_grad():
        for i, batch in enumerate(loader):
            image = batch["image"].to(device)
            gis = batch["gis"].to(device)
            label = batch["label"].to(device)
            city = batch.get("city_name", [f"sample_{i}"])[0]

            preds = model(image, gis)
            preds_prob = torch.sigmoid(preds)

            all_preds.append(preds_prob.cpu().numpy().flatten())
            all_targets.append(label.cpu().numpy().flatten())
            all_pred_mins.append(preds_prob.min().item())
            all_pred_maxs.append(preds_prob.max().item())
            all_pred_means.append(preds_prob.mean().item())
            all_pred_stds.append(preds_prob.std().item())

            print(f"\nSample {i+1}: {city}")
            print(f"  Label  - min: {label.min():.4f}, max: {label.max():.4f}, mean: {label.mean():.4f}, std: {label.std():.4f}")
            print(f"  Pred   - min: {preds_prob.min():.4f}, max: {preds_prob.max():.4f}, mean: {preds_prob.mean():.4f}, std: {preds_prob.std():.4f}")
            print(f"  Error  - MSE: {((preds_prob - label)**2).mean():.4f}, MAE: {(preds_prob - label).abs().mean():.4f}")

    all_preds = np.concatenate(all_preds)
    all_targets = np.concatenate(all_targets)

    print("\n" + "=" * 60)
    print("OVERALL STATISTICS")
    print("=" * 60)
    print(f"Predictions - min: {all_preds.min():.4f}, max: {all_preds.max():.4f}, mean: {all_preds.mean():.4f}, std: {all_preds.std():.4f}")
    print(f"Targets     - min: {all_targets.min():.4f}, max: {all_targets.max():.4f}, mean: {all_targets.mean():.4f}, std: {all_targets.std():.4f}")
    print(f"Global MSE: {((all_preds - all_targets)**2).mean():.4f}")
    print(f"Global MAE: {np.abs(all_preds - all_targets).mean():.4f}")

    # Check if predictions are too narrow (collapsed)
    pred_range = all_preds.max() - all_preds.min()
    target_range = all_targets.max() - all_targets.min()
    print(f"\nPrediction range: {pred_range:.4f} (target: {target_range:.4f})")
    if pred_range < 0.1:
        print("WARNING: Predictions are very narrow - model may be collapsed!")
    if pred_range < target_range * 0.5:
        print("WARNING: Predictions have much less variance than targets!")

    # R² calculation
    ss_res = np.sum((all_targets - all_preds) ** 2)
    ss_tot = np.sum((all_targets - np.mean(all_targets)) ** 2)
    r2 = 1 - ss_res / (ss_tot + 1e-8)
    print(f"Global R²: {r2:.4f}")

    # Check prediction distribution
    print(f"\nPrediction percentiles:")
    for p in [1, 5, 25, 50, 75, 95, 99]:
        print(f"  {p}th: {np.percentile(all_preds, p):.4f}")


if __name__ == "__main__":
    main()
