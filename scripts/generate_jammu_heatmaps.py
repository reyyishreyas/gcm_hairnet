#!/usr/bin/env python3
"""
Generate model-wise heatmap images for Jammu (and other cities).
Creates single-panel risk map visualizations similar to ref.png for:
1. Ground truth reference
2. Each model's prediction

Usage:
    python scripts/generate_jammu_heatmaps.py --city Jammu --output-dir outputs/jammu_heatmaps
"""

import argparse
import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LinearSegmentedColormap

GREEN_TO_RED = LinearSegmentedColormap.from_list(
    "green_to_red",
    ["#00ff00", "#ffff00", "#ff0000"],
    N=256,
)


def load_predictions(model_name: str, split: str = "test"):
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


def get_city_index(city_name: str, cities: list) -> int:
    """Find index of city in cities list."""
    for i, c in enumerate(cities):
        if c == city_name:
            return i
    raise ValueError(f"City {city_name} not found in cities list: {cities}")


def save_heatmap(
    data: np.ndarray,
    output_path: Path,
    title: str = "",
    cmap=GREEN_TO_RED,
    vmin: float = 0.0,
    vmax: float = 1.0,
    dpi: int = 200,
):
    """Save a single-panel heatmap visualization."""
    fig, ax = plt.subplots(figsize=(8, 8))
    im = ax.imshow(data, cmap=cmap, vmin=vmin, vmax=vmax)
    ax.set_title(title, fontsize=14, fontweight="bold", pad=10)
    ax.axis("off")
    plt.colorbar(im, ax=ax, label="Risk Probability", fraction=0.046, pad=0.04)
    plt.tight_layout()
    fig.savefig(output_path, dpi=dpi, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"  Saved: {output_path}")


def generate_jammu_heatmaps(city: str = "Jammu", output_dir: str = "outputs/jammu_heatmaps"):
    """Generate heatmaps for a specific city across all available models."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    # All models to process
    models = [
        "addition",
        "bilinear",
        "concat",
        "cross_attention",
        "gated",
        "gcm",
        "gis_only",
        "graphsage",
        "image_only",
        "mha",
        "multihead_cross_attention",
        "nonlocal",
        "swin",
        "vit",
    ]

    print(f"Generating heatmaps for {city}...")
    print(f"Output directory: {output_path}")

    # First, generate ground truth reference
    try:
        preds, targets, cities = load_predictions(models[0], "test")
        city_idx = get_city_index(city, cities)
        gt = targets[city_idx].squeeze()
        save_heatmap(
            gt,
            output_path / f"{city}_ground_truth.png",
            title=f"{city} - Ground Truth",
        )
    except Exception as e:
        print(f"  Could not load ground truth: {e}")

    # Generate predictions for each model
    for model in models:
        try:
            preds, targets, cities = load_predictions(model, "test")
            city_idx = get_city_index(city, cities)
            pred = preds[city_idx].squeeze()
            save_heatmap(
                pred,
                output_path / f"{city}_{model}.png",
                title=f"{city} - {model.upper()}",
            )
        except Exception as e:
            print(f"  Skip {model}: {e}")

    print(f"\nDone! Generated heatmaps for {city} in {output_path}")


def generate_all_cities_heatmaps(output_dir: str = "outputs/all_heatmaps"):
    """Generate heatmaps for all test cities across all models."""
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    models = [
        "addition",
        "bilinear",
        "concat",
        "cross_attention",
        "gated",
        "gcm",
        "gis_only",
        "graphsage",
        "image_only",
        "mha",
        "multihead_cross_attention",
        "nonlocal",
        "swin",
        "vit",
    ]

    # Load cities from first model
    _, targets, cities = load_predictions("addition", "test")
    print(f"Found {len(cities)} test cities: {cities}")

    for city in cities:
        city_dir = output_path / city
        city_dir.mkdir(parents=True, exist_ok=True)

        # Find city index
        city_idx = get_city_index(city, cities)

        # Ground truth
        gt = targets[city_idx].squeeze()
        save_heatmap(
            gt,
            city_dir / f"{city}_ground_truth.png",
            title=f"{city} - Ground Truth",
        )

        # Model predictions
        for model in models:
            try:
                preds, _, _ = load_predictions(model, "test")
                pred = preds[city_idx].squeeze()
                save_heatmap(
                    pred,
                    city_dir / f"{city}_{model}.png",
                    title=f"{city} - {model.upper()}",
                )
            except Exception as e:
                print(f"  Skip {model} for {city}: {e}")

    print(f"\nDone! Generated heatmaps for all cities in {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate model-wise heatmaps for cities")
    parser.add_argument(
        "--city",
        type=str,
        default="Jammu",
        help="City name to generate heatmaps for (default: Jammu)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default="outputs/jammu_heatmaps",
        help="Output directory for heatmaps",
    )
    parser.add_argument(
        "--all-cities",
        action="store_true",
        help="Generate heatmaps for all test cities",
    )
    args = parser.parse_args()

    if args.all_cities:
        generate_all_cities_heatmaps(args.output_dir)
    else:
        generate_jammu_heatmaps(args.city, args.output_dir)


if __name__ == "__main__":
    main()
