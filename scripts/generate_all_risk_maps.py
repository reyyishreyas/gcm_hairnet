#!/usr/bin/env python3
"""
Comprehensive post-processing script:
1. Run inference on all models to generate predictions
2. Generate risk maps with green-to-red colormap
3. Generate comparison grids (3 images per row)
"""

import argparse
import json
import sys
from pathlib import Path

import numpy as np
import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from models import build_model
from utils.misc import get_device


# ─────────────────────────────────────────────
# 1. CANONICAL CSV CLEANING
# ─────────────────────────────────────────────
def clean_canonical_csv(csv_path: Path):
    """Rename invalid ablation row."""
    import csv

    # Read existing
    rows = []
    with open(csv_path, "r") as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        for row in reader:
            rows.append(row)

    # Rename baseline,GCM-HAIRNet,full -> baseline,GCM-Ablation-Full,full
    for r in rows:
        if r["model"] == "GCM-HAIRNet" and r["variant"] == "full":
            r["model"] = "GCM-Ablation-Full"

    # Write back
    with open(csv_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in rows:
            clean_row = {k: ("" if v is None else str(v)) for k, v in r.items()}
            writer.writerow(clean_row)

    print(f"[CSV] Cleaned canonical results saved to {csv_path}")
    return rows


# ─────────────────────────────────────────────
# 2. INFERENCE ENGINE
# ─────────────────────────────────────────────
def load_model_from_checkpoint(config, checkpoint_path, device):
    """Build model and load checkpoint with flexible state dict matching."""
    model = build_model(config.get("model", {}))
    checkpoint = torch.load(checkpoint_path, map_location=device)
    ckpt_state = checkpoint["model_state_dict"]
    model_state = model.state_dict()

    new_state = {}
    matched = 0
    skipped = 0
    for key, param in ckpt_state.items():
        if key in model_state:
            if param.shape == model_state[key].shape:
                new_state[key] = param
                matched += 1
            else:
                skipped += 1
        else:
            skipped += 1

    result = model.load_state_dict(new_state, strict=False)
    if result.missing_keys or result.unexpected_keys:
        print(f"  Warning: Partial load - missing: {len(result.missing_keys)}, unexpected: {len(result.unexpected_keys)}")
    if skipped > 0:
        print(f"  Info: Loaded {matched} layers, skipped {skipped} incompatible layers")

    model.to(device)
    model.eval()
    return model


def run_inference(model, loader, device) -> tuple[np.ndarray, np.ndarray, list]:
    """Run inference and return predictions, targets, city names."""
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
    return preds, targets, all_cities


def get_model_config_mapping() -> dict:
    """Return mapping of model_name -> (config_name, checkpoint_path)."""
    mapping = {}

    # Fusion models
    fusion_models = [
        "image_only", "gis_only", "concat", "addition",
        "gated", "cross_attention", "multihead_cross_attention", "bilinear",
    ]
    for m in fusion_models:
        mapping[m] = (f"baseline_{m}", f"checkpoints/baselines/{m}/best.pt")

    # Controlled baselines
    baseline_models = ["gcm", "vit", "swin", "graphsage", "mha", "nonlocal"]
    for m in baseline_models:
        mapping[m] = (f"baselines/baseline_{m}", f"checkpoints/baselines/{m}/best.pt")

    # Ablations (skip - no checkpoints exist; use JSON metrics only)
    ablation_models = [
        "full", "no_distance", "no_similarity", "no_road", "no_urban",
        "no_learned", "no_scene_weights", "no_gcm", "no_gct", "no_gct_no_gcm",
    ]
    for m in ablation_models:
        mapping[f"ablation_{m}"] = (f"gcm_ablation/{m}", f"checkpoints/ablations/{m}/best.pt")

    return mapping


# ─────────────────────────────────────────────
# 3. RISK MAP GENERATION
# ─────────────────────────────────────────────
def save_risk_map_grid(
    predictions: np.ndarray,
    targets: np.ndarray,
    city_names: list,
    output_path: Path,
    model_name: str,
    split: str,
    cmap: str = "RdYlGn_r",
    n_cols: int = 3,
):
    """Save a grid of risk maps: predictions and targets, 3 per row."""
    try:
        import matplotlib.pyplot as plt
        from matplotlib.colors import LinearSegmentedColormap
    except ImportError:
        print("Matplotlib not available, skipping grid generation")
        return

    output_path.mkdir(parents=True, exist_ok=True)

    n_images = len(predictions)
    n_rows = int(np.ceil(n_images / n_cols))

    # Create figure with 2 rows per image (pred + target), 3 columns
    fig, axes = plt.subplots(n_rows * 2, n_cols, figsize=(n_cols * 5, n_rows * 5))
    if n_rows * n_cols == 1:
        axes = np.array([[axes[0], axes[1]]])
    elif n_rows == 1:
        axes = axes.reshape(2, n_cols)
    else:
        axes = axes.reshape(n_rows * 2, n_cols)

    fig.suptitle(f"{model_name} — {split} set", fontsize=16, y=0.98)

    for idx in range(n_images):
        row = (idx // n_cols) * 2
        col = idx % n_cols

        pred = predictions[idx].squeeze()
        target = targets[idx].squeeze()
        city = city_names[idx] if idx < len(city_names) else f"img_{idx}"

        # Target row
        ax_target = axes[row, col]
        im_t = ax_target.imshow(target, cmap=cmap, vmin=0, vmax=1)
        ax_target.set_title(f"GT: {city}", fontsize=10)
        ax_target.axis("off")

        # Prediction row
        ax_pred = axes[row + 1, col]
        im_p = ax_pred.imshow(pred, cmap=cmap, vmin=0, vmax=1)
        ax_pred.set_title(f"Pred: {city}", fontsize=10)
        ax_pred.axis("off")

    # Hide empty subplots
    total_slots = n_rows * n_cols
    for idx in range(n_images, total_slots):
        row = (idx // n_cols) * 2
        col = idx % n_cols
        axes[row, col].axis("off")
        axes[row + 1, col].axis("off")

    # Add colorbar
    cbar_ax = fig.add_axes([0.92, 0.15, 0.015, 0.7])
    fig.colorbar(im_p, cax=cbar_ax, label="Risk Probability")

    plt.tight_layout(rect=[0, 0, 0.9, 0.96])
    fig.savefig(output_path / f"{split}_risk_maps_grid.png", dpi=150, bbox_inches="tight")
    plt.close(fig)
    print(f"  Saved grid: {output_path / f'{split}_risk_maps_grid.png'}")


def save_individual_maps(
    predictions: np.ndarray,
    targets: np.ndarray,
    city_names: list,
    output_path: Path,
    model_name: str,
    split: str,
    cmap: str = "RdYlGn_r",
):
    """Save individual risk map PNGs and NPY files."""
    output_path.mkdir(parents=True, exist_ok=True)

    for idx, (pred, target) in enumerate(zip(predictions, targets)):
        city = city_names[idx] if idx < len(city_names) else f"img_{idx}"
        pred_2d = pred.squeeze()
        target_2d = target.squeeze()

        # Save npy
        np.save(output_path / f"{city}_predictions.npy", pred_2d)
        np.save(output_path / f"{city}_targets.npy", target_2d)

        # Save PNGs
        try:
            import matplotlib.pyplot as plt

            fig, axes = plt.subplots(1, 3, figsize=(15, 5))

            axes[0].imshow(target_2d, cmap=cmap, vmin=0, vmax=1)
            axes[0].set_title(f"Ground Truth: {city}")
            axes[0].axis("off")

            axes[1].imshow(pred_2d, cmap=cmap, vmin=0, vmax=1)
            axes[1].set_title(f"Prediction: {city}")
            axes[1].axis("off")

            diff = np.abs(target_2d - pred_2d)
            axes[2].imshow(diff, cmap="viridis")
            axes[2].set_title(f"Absolute Error: {city}")
            axes[2].axis("off")

            fig.savefig(output_path / f"{city}_comparison.png", dpi=100, bbox_inches="tight")
            plt.close(fig)
        except ImportError:
            pass

    print(f"  Saved {len(predictions)} individual maps to {output_path}")


# ─────────────────────────────────────────────
# 4. MAIN ORCHESTRATION
# ─────────────────────────────────────────────
def process_model(model_name, config_name, checkpoint_path, device, root_dir, output_base, split="val"):
    """Run inference and generate risk maps for a single model."""
    print(f"\n{'='*60}")
    print(f"Processing: {model_name} (config={config_name}, ckpt={checkpoint_path})")
    print(f"{'='*60}")

    ckpt_path = Path(checkpoint_path)
    if not ckpt_path.exists():
        print(f"  SKIP: Checkpoint not found: {ckpt_path}")
        return None

    try:
        config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
        config = config_manager.load(config_name)
    except Exception as e:
        print(f"  SKIP: Config load failed: {e}")
        return None

    try:
        dataset = GCMHAIRNetDataset(
            root_dir=root_dir,
            split=split,
            transforms=get_val_transforms(),
        )
        loader = build_dataloader(
            dataset,
            batch_size=config.get("dataset", {}).get("test_batch_size", 32),
            shuffle=False,
            num_workers=0,
            pin_memory=(device.type == "cuda"),
            drop_last=False,
        )
    except Exception as e:
        print(f"  SKIP: Dataset load failed: {e}")
        return None

    try:
        model = load_model_from_checkpoint(config, str(ckpt_path), device)
        preds, targets, cities = run_inference(model, loader, device)
    except Exception as e:
        print(f"  SKIP: Inference failed: {e}")
        return None

    # Save outputs
    model_out_dir = Path(output_base) / model_name / split
    model_out_dir.mkdir(parents=True, exist_ok=True)

    np.save(model_out_dir / f"{split}_predictions.npy", preds)
    np.save(model_out_dir / f"{split}_targets.npy", targets)

    with open(model_out_dir / f"{split}_cities.json", "w") as f:
        json.dump(cities, f, indent=2)

    save_risk_map_grid(preds, targets, cities, model_out_dir, model_name, split)
    save_individual_maps(preds, targets, cities, model_out_dir, model_name, split)

    print(f"  Done. Processed {len(cities)} images.")
    return {"predictions": preds, "targets": targets, "cities": cities}


def main():
    parser = argparse.ArgumentParser(description="Generate risk maps for all models")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--output-dir", type=str, default="./outputs/experiments", help="Output directory")
    parser.add_argument("--splits", nargs="+", default=["val", "test"], help="Splits to process")
    parser.add_argument("--skip-existing", action="store_true", help="Skip if predictions exist")
    args = parser.parse_args()

    device = get_device(None)
    print(f"Using device: {device}")

    # 1. Clean canonical CSV
    csv_path = Path(args.output_dir) / "results" / "experiment_results.csv"
    if csv_path.exists():
        clean_canonical_csv(csv_path)
    else:
        print(f"Warning: Canonical CSV not found at {csv_path}")

    # 2. Define all models to process
    model_configs = get_model_config_mapping()

    # 3. Process each model
    results = {}
    for model_name, (config_name, ckpt_path) in model_configs.items():
        for split in args.splits:
            preds_path = Path(args.output_dir) / model_name / split / f"{split}_predictions.npy"
            if args.skip_existing and preds_path.exists():
                print(f"\nSKIP {model_name}/{split}: predictions already exist")
                continue

            result = process_model(
                model_name=model_name,
                config_name=config_name,
                checkpoint_path=ckpt_path,
                device=device,
                root_dir=args.root_dir,
                output_base=args.output_dir,
                split=split,
            )
            if result:
                results[f"{model_name}/{split}"] = result

    print(f"\n{'='*60}")
    print(f"Completed processing {len(results)} model/split combinations")
    print(f"Outputs saved to: {args.output_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
