#!/usr/bin/env python3
"""
Generate comprehensive comparison figure:
- Ground truth row
- All models sorted by R² (best to worst)
- Metrics overlay on each subplot
- 3 images per row layout
"""

import json
import sys
from pathlib import Path

import numpy as np
import torch
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from models import build_model
from utils.misc import get_device


# Custom colormap: green (0) -> yellow -> red (1)
GREEN_TO_RED = LinearSegmentedColormap.from_list(
    "green_to_red",
    ["#00ff00", "#ffff00", "#ff0000"],
    N=256
)


def load_predictions(model_name, split="test"):
    """Load predictions and targets from outputs."""
    base = Path("outputs/experiments") / model_name / split
    preds = np.load(base / f"{split}_predictions.npy")
    targets = np.load(base / f"{split}_targets.npy")
    cities_path = base / f"{split}_cities.json"
    if cities_path.exists():
        with open(cities_path) as f:
            cities = json.load(f)
    else:
        cities = [f"img_{i}" for i in range(len(preds))]
    return preds, targets, cities


def get_model_metrics(model_name, metrics_dict):
    """Extract metrics string for overlay."""
    if model_name not in metrics_dict:
        return "N/A"
    m = metrics_dict[model_name]
    return f"MSE: {m.get('mse', 0):.4f}\nR²: {m.get('r2', 0):.4f}\nF1: {m.get('f1', 0):.4f}"


def generate_comparison_figure(
    models_data: dict,
    output_path: Path,
    split: str = "test",
    n_cols: int = 3,
    cmap=GREEN_TO_RED,
):
    """
    Generate comparison figure with ground truth + all models sorted by R².
    
    Args:
        models_data: dict of {model_name: {'preds': array, 'targets': array, 'cities': list, 'metrics': dict}}
        output_path: Path to save figure
        split: 'val' or 'test'
        n_cols: number of columns per row
    """
    # Sort models by R² descending (best first)
    def get_r2(model_name):
        m = models_data[model_name].get("metrics", {})
        return m.get("r2", -999)
    
    sorted_models = sorted(models_data.keys(), key=lambda m: get_r2(m), reverse=True)
    
    # All models should have same cities/order
    ref_cities = models_data[sorted_models[0]]["cities"]
    n_images = len(ref_cities)
    n_rows = int(np.ceil(n_images / n_cols))
    
    # Total rows: 1 for GT + N models
    total_rows = 1 + len(sorted_models)
    
    fig, axes = plt.subplots(
        total_rows, n_cols,
        figsize=(n_cols * 5, total_rows * 4.5)
    )
    
    if total_rows == 1:
        axes = axes.reshape(1, -1)
    if n_rows == 1:
        axes = axes.reshape(total_rows, n_cols)
    
    # First row: Ground Truth
    gt_model = sorted_models[0]
    targets = models_data[gt_model]["targets"]
    cities = models_data[gt_model]["cities"]
    
    for idx in range(n_images):
        row, col = 0, idx % n_cols
        ax = axes[row, col]
        im = ax.imshow(targets[idx].squeeze(), cmap=cmap, vmin=0, vmax=1)
        ax.set_title(f"Ground Truth: {cities[idx]}", fontsize=11, fontweight="bold")
        ax.axis("off")
    
    # Hide empty GT subplots
    for idx in range(n_images, n_rows * n_cols):
        row, col = 0, idx % n_cols
        axes[row, col].axis("off")
    
    # Subsequent rows: each model
    for model_idx, model_name in enumerate(sorted_models, start=1):
        row = model_idx
        preds = models_data[model_name]["preds"]
        metrics = models_data[model_name].get("metrics", {})
        
        for idx in range(n_images):
            col = idx % n_cols
            ax = axes[row, col]
            
            pred_img = preds[idx].squeeze()
            im = ax.imshow(pred_img, cmap=cmap, vmin=0, vmax=1)
            
            # Metrics overlay text
            r2 = metrics.get("r2", 0)
            mse = metrics.get("mse", 0)
            f1 = metrics.get("f1", 0)
            iou = metrics.get("iou", 0)
            
            metric_text = f"R²: {r2:.3f}\nMSE: {mse:.4f}\nF1: {f1:.3f}\nIoU: {iou:.3f}"
            ax.text(
                0.02, 0.98, metric_text,
                transform=ax.transAxes,
                fontsize=8,
                verticalalignment="top",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
            )
            
            ax.set_title(f"{model_name}: {ref_cities[idx]}", fontsize=10)
            ax.axis("off")
        
        # Hide empty subplots for this row
        for idx in range(n_images, n_rows * n_cols):
            col = idx % n_cols
            axes[row, col].axis("off")
    
    # Add colorbar
    cbar_ax = fig.add_axes([0.92, 0.15, 0.015, 0.7])
    fig.colorbar(im, cax=cbar_ax, label="Risk Probability")
    
    # Title
    fig.suptitle(f"GCM-HAIRNet Comparison — {split.upper()} Set (Sorted by R²)", fontsize=18, y=0.98)
    
    plt.tight_layout(rect=[0, 0, 0.9, 0.96])
    fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved comparison figure: {output_path}")


def generate_metrics_table_figure(models_data: dict, output_path: Path, split: str = "test"):
    """Generate a table figure summarizing all metrics."""
    sorted_models = sorted(
        models_data.keys(),
        key=lambda m: models_data[m].get("metrics", {}).get("r2", -999),
        reverse=True,
    )
    
    fig, ax = plt.subplots(figsize=(14, len(sorted_models) * 0.6 + 1))
    ax.axis("off")
    ax.axis("tight")
    
    table_data = []
    for model_name in sorted_models:
        m = models_data[model_name].get("metrics", {})
        table_data.append([
            model_name,
            f"{m.get('mse', 0):.6f}",
            f"{m.get('mae', 0):.6f}",
            f"{m.get('r2', 0):.6f}",
            f"{m.get('f1', 0):.6f}",
            f"{m.get('iou', 0):.6f}",
            f"{m.get('precision', 0):.6f}",
            f"{m.get('recall', 0):.6f}",
            f"{m.get('accuracy', 0):.6f}",
        ])
    
    columns = ["Model", "MSE", "MAE", "R²", "F1", "IoU", "Precision", "Recall", "Accuracy"]
    table = ax.table(
        cellText=table_data,
        colLabels=columns,
        cellLoc="center",
        loc="center",
        colWidths=[0.15] + [0.09] * 8,
    )
    
    table.auto_set_font_size(False)
    table.set_fontsize(9)
    table.scale(1, 2)
    
    # Color header
    for i in range(len(columns)):
        table[(0, i)].set_facecolor("#4472C4")
        table[(0, i)].set_text_props(color="white", fontweight="bold")
    
    # Color rows by R²
    for i, model_name in enumerate(sorted_models, start=1):
        r2 = models_data[model_name].get("metrics", {}).get("r2", 0)
        if r2 > 0.9:
            color = "#C6EFCE"  # green
        elif r2 > 0.7:
            color = "#FFEB9C"  # yellow
        elif r2 > 0.5:
            color = "#FFC7CE"  # light red
        else:
            color = "#FF0000"  # red
            table[(i, 0)].set_text_props(color="white")
        
        for j in range(len(columns)):
            table[(i, j)].set_facecolor(color)
    
    ax.set_title(f"GCM-HAIRNet Metrics Comparison — {split.upper()} Set", fontsize=14, pad=20)
    fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved metrics table: {output_path}")


def main():
    split = "test"
    
    # Load test metrics JSON
    metrics_path = Path("outputs/experiments/results/baseline_test_metrics.json")
    if not metrics_path.exists():
        print(f"Error: {metrics_path} not found. Run test evaluation first.")
        return
    
    with open(metrics_path) as f:
        baseline_metrics = json.load(f)
    
    # Also load fusion metrics from existing JSONs
    fusion_metrics = {}
    fusion_dir = Path("outputs/experiments/fusion")
    if fusion_dir.exists():
        for model_dir in fusion_dir.iterdir():
            if model_dir.is_dir():
                test_json = model_dir / "test_metrics.json"
                if test_json.exists():
                    with open(test_json) as f:
                        fusion_metrics[model_dir.name] = json.load(f)
    
    # Combine all models
    all_metrics = {**baseline_metrics, **fusion_metrics}
    
    # Load predictions for all valid models
    valid_models = [
        "image_only", "gis_only", "concat", "addition", "gated",
        "cross_attention", "multihead_cross_attention", "bilinear",
        "gcm", "vit", "swin", "graphsage", "mha", "nonlocal"
    ]
    
    models_data = {}
    for model_name in valid_models:
        try:
            preds, targets, cities = load_predictions(model_name, split)
            metrics = all_metrics.get(model_name, {})
            models_data[model_name] = {
                "preds": preds,
                "targets": targets,
                "cities": cities,
                "metrics": metrics,
            }
        except Exception as e:
            print(f"Skip {model_name}: {e}")
    
    print(f"\nLoaded {len(models_data)} models for comparison")
    
    # Generate outputs
    output_dir = Path("outputs/experiments/results")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    generate_comparison_figure(
        models_data,
        output_dir / f"comparison_{split}_sorted.png",
        split=split,
    )
    
    generate_metrics_table_figure(
        models_data,
        output_dir / f"metrics_table_{split}.png",
        split=split,
    )
    
    # Also generate val comparison
    val_models_data = {}
    for model_name in valid_models:
        try:
            preds, targets, cities = load_predictions(model_name, "val")
            metrics = all_metrics.get(model_name, {})
            val_models_data[model_name] = {
                "preds": preds,
                "targets": targets,
                "cities": cities,
                "metrics": metrics,
            }
        except Exception as e:
            print(f"Skip {model_name} val: {e}")
    
    if val_models_data:
        generate_comparison_figure(
            val_models_data,
            output_dir / "comparison_val_sorted.png",
            split="val",
        )
        generate_metrics_table_figure(
            val_models_data,
            output_dir / "metrics_table_val.png",
            split="val",
        )
    
    print(f"\nAll comparison figures saved to {output_dir}")


if __name__ == "__main__":
    main()
