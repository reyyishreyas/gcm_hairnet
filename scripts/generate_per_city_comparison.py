#!/usr/bin/env python3
"""
Generate per-city comparison figures:
- Ground truth row
- All models sorted by R²
- 3 cities per row layout
- Consistent green-to-red colormap (0=green, 1=red)
- Separate figures for fusion, baselines, and ablations
"""

import json
import sys
from pathlib import Path

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

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


def get_metrics(model_name, all_metrics):
    """Get metrics dict for a model."""
    # Check baseline test metrics first
    if model_name in all_metrics.get("baselines", {}):
        return all_metrics["baselines"][model_name]
    # Check fusion metrics
    if model_name in all_metrics.get("fusion", {}):
        return all_metrics["fusion"][model_name]
    # Check ablation metrics
    if model_name in all_metrics.get("ablations", {}):
        return all_metrics["ablations"][model_name]
    return {}


def generate_per_city_comparison(
    models: list,
    split: str = "test",
    output_path: Path = None,
    title: str = "",
    all_metrics: dict = None,
    n_cols: int = 3,
):
    """
    Generate comparison figure with:
    - Row 0: Ground Truth for cities 0,1,2,...
    - Row 1..N: Each model's predictions for same cities
    
    All subplots share vmin=0, vmax=1.
    """
    if all_metrics is None:
        all_metrics = {}
    
    # Load data for all models
    models_data = {}
    for m in models:
        try:
            preds, targets, cities = load_predictions(m, split)
            metrics = get_metrics(m, all_metrics)
            models_data[m] = {
                "preds": preds,
                "targets": targets,
                "cities": cities,
                "metrics": metrics,
            }
        except Exception as e:
            print(f"  Skip {m}: {e}")
    
    if not models_data:
        print(f"  No models loaded for {title}")
        return
    
    # Sort models by R² descending
    def get_r2(m):
        return models_data[m].get("metrics", {}).get("r2", -999)
    
    sorted_models = sorted(models_data.keys(), key=lambda m: get_r2(m), reverse=True)
    
    # Use first model's cities as reference
    ref_cities = models_data[sorted_models[0]]["cities"]
    n_images = len(ref_cities)
    n_rows = int(np.ceil(n_images / n_cols))
    
    # Total rows: 1 GT + N models
    total_rows = 1 + len(sorted_models)
    
    fig, axes = plt.subplots(
        total_rows, n_cols,
        figsize=(n_cols * 5, total_rows * 4.5)
    )
    
    if total_rows == 1:
        axes = axes.reshape(1, -1)
    if n_rows == 1:
        axes = axes.reshape(total_rows, n_cols)
    
    targets = models_data[sorted_models[0]]["targets"]
    
    # Row 0: Ground Truth
    for idx in range(n_images):
        row, col = 0, idx % n_cols
        ax = axes[row, col]
        im = ax.imshow(targets[idx].squeeze(), cmap=GREEN_TO_RED, vmin=0, vmax=1)
        ax.set_title(f"Ground Truth: {ref_cities[idx]}", fontsize=11, fontweight="bold")
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
            im = ax.imshow(pred_img, cmap=GREEN_TO_RED, vmin=0, vmax=1)
            
            # Metrics overlay
            r2 = metrics.get("r2", 0)
            mse = metrics.get("mse", 0)
            f1 = metrics.get("f1", 0)
            iou = metrics.get("iou", 0)
            
            metric_text = f"R²: {r2:.3f}  MSE: {mse:.4f}\nF1: {f1:.3f}  IoU: {iou:.3f}"
            ax.text(
                0.02, 0.98, metric_text,
                transform=ax.transAxes,
                fontsize=8,
                verticalalignment="top",
                bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.85),
            )
            
            ax.set_title(f"{model_name}: {ref_cities[idx]}", fontsize=10)
            ax.axis("off")
        
        # Hide empty subplots
        for idx in range(n_images, n_rows * n_cols):
            col = idx % n_cols
            axes[row, col].axis("off")
    
    # Colorbar
    cbar_ax = fig.add_axes([0.92, 0.15, 0.015, 0.7])
    fig.colorbar(im, cax=cbar_ax, label="Risk Probability")
    
    fig.suptitle(f"{title} — {split.upper()} Set (Sorted by R²)", fontsize=18, y=0.98)
    
    plt.tight_layout(rect=[0, 0, 0.9, 0.96])
    fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Saved: {output_path}")


def main():
    split = "test"
    
    # Load all metrics
    all_metrics = {"baselines": {}, "fusion": {}, "ablations": {}}
    
    # Load baseline test metrics
    baseline_metrics_path = Path("outputs/experiments/results/baseline_test_metrics.json")
    if baseline_metrics_path.exists():
        with open(baseline_metrics_path) as f:
            all_metrics["baselines"] = json.load(f)
    
    # Load fusion metrics
    fusion_dir = Path("outputs/experiments/fusion")
    if fusion_dir.exists():
        for model_dir in fusion_dir.iterdir():
            if model_dir.is_dir():
                test_json = model_dir / "test_metrics.json"
                if test_json.exists():
                    with open(test_json) as f:
                        all_metrics["fusion"][model_dir.name] = json.load(f)
    
    # Load ablation metrics
    ablation_dir = Path("outputs/experiments/ablation")
    if ablation_dir.exists():
        for model_dir in ablation_dir.iterdir():
            if model_dir.is_dir():
                test_json = model_dir / "test_metrics.json"
                if test_json.exists():
                    with open(test_json) as f:
                        all_metrics["ablations"][model_dir.name] = json.load(f)
    
    output_dir = Path("outputs/experiments/results")
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # 1. Fusion comparison (8 models + GT)
    fusion_models = [
        "addition", "bilinear", "concat", "gated",
        "cross_attention", "multihead_cross_attention",
        "image_only", "gis_only"
    ]
    print(f"\nGenerating fusion comparison ({len(fusion_models)} models)...")
    generate_per_city_comparison(
        models=fusion_models,
        split=split,
        output_path=output_dir / f"fusion_comparison_{split}.png",
        title="Fusion Study Comparison",
        all_metrics=all_metrics,
    )
    
    # 2. Baseline comparison (7 valid models + GT)
    baseline_models = ["gcm", "vit", "swin", "graphsage", "mha", "nonlocal"]
    print(f"\nGenerating baseline comparison ({len(baseline_models)} models)...")
    generate_per_city_comparison(
        models=baseline_models,
        split=split,
        output_path=output_dir / f"baseline_comparison_{split}.png",
        title="Controlled Baselines Comparison",
        all_metrics=all_metrics,
    )
    
    # 3. Ablation comparison (9 variants + GT)
    ablation_models = [
        "full", "no_distance", "no_similarity", "no_road", "no_urban",
        "no_learned", "no_scene_weights", "no_gcm", "no_gct", "no_gct_no_gcm",
    ]
    print(f"\nGenerating ablation comparison ({len(ablation_models)} models)...")
    generate_per_city_comparison(
        models=ablation_models,
        split=split,
        output_path=output_dir / f"ablation_comparison_{split}.png",
        title="GCM Ablation Comparison",
        all_metrics=all_metrics,
    )
    
    # 4. All models together (15 valid + GT)
    all_models = fusion_models + baseline_models
    print(f"\nGenerating full comparison ({len(all_models)} models)...")
    generate_per_city_comparison(
        models=all_models,
        split=split,
        output_path=output_dir / f"full_comparison_{split}.png",
        title="All Valid Models Comparison",
        all_metrics=all_metrics,
    )
    
    # Generate val versions too
    for split in ["val", "test"]:
        print(f"\n--- {split.upper()} ---")
        
        fusion_models = [
            "addition", "bilinear", "concat", "gated",
            "cross_attention", "multihead_cross_attention",
            "image_only", "gis_only"
        ]
        generate_per_city_comparison(
            models=fusion_models,
            split=split,
            output_path=output_dir / f"fusion_comparison_{split}.png",
            title=f"Fusion Study Comparison",
            all_metrics=all_metrics,
        )
        
        baseline_models = ["gcm", "vit", "swin", "graphsage", "mha", "nonlocal"]
        generate_per_city_comparison(
            models=baseline_models,
            split=split,
            output_path=output_dir / f"baseline_comparison_{split}.png",
            title=f"Controlled Baselines Comparison",
            all_metrics=all_metrics,
        )
        
        ablation_models = [
            "full", "no_distance", "no_similarity", "no_road", "no_urban",
            "no_learned", "no_scene_weights", "no_gcm", "no_gct", "no_gct_no_gcm",
        ]
        generate_per_city_comparison(
            models=ablation_models,
            split=split,
            output_path=output_dir / f"ablation_comparison_{split}.png",
            title=f"GCM Ablation Comparison",
            all_metrics=all_metrics,
        )
        
        all_models = fusion_models + baseline_models
        generate_per_city_comparison(
            models=all_models,
            split=split,
            output_path=output_dir / f"full_comparison_{split}.png",
            title=f"All Valid Models Comparison",
            all_metrics=all_metrics,
        )
    
    print(f"\nAll comparison figures saved to {output_dir}")


if __name__ == "__main__":
    main()
