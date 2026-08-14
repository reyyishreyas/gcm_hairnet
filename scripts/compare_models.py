import json
from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np


def load_results(results_path: str = "./outputs/tables/results.json") -> Dict[str, Dict[str, float]]:
    path = Path(results_path)
    if not path.exists():
        raise FileNotFoundError(f"Results file not found: {path}")
    with open(path, "r") as f:
        return json.load(f)


def plot_metric_comparison(
    results: Dict[str, Dict[str, float]],
    metric: str,
    output_path: str,
    title: str,
    ylabel: str,
    figsize: tuple = (10, 6),
):
    models = []
    values = []
    for model_name, metrics in results.items():
        if metric in metrics and not np.isinf(metrics[metric]):
            models.append(model_name)
            values.append(metrics[metric])

    if not values:
        return

    fig, ax = plt.subplots(figsize=figsize)
    bars = ax.bar(models, values, color="steelblue")
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_xlabel("Model", fontsize=12)
    ax.tick_params(axis="x", rotation=45, labelsize=9)
    ax.grid(axis="y", alpha=0.3)

    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{val:.4f}", ha="center", va="bottom", fontsize=8)

    plt.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def compare_models(results_path: str = "./outputs/tables/results.json", output_dir: str = "./outputs/comparison"):
    results = load_results(results_path)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    metrics_to_plot = [
        ("val_mae", "MAE Comparison", "Mean Absolute Error"),
        ("val_mse", "MSE Comparison", "Mean Squared Error"),
        ("val_rmse", "RMSE Comparison", "Root Mean Squared Error"),
        ("val_r2", "R² Comparison", "R² Score"),
    ]

    for metric, title, ylabel in metrics_to_plot:
        plot_metric_comparison(
            results,
            metric,
            str(output_path / f"{metric}_comparison.png"),
            title,
            ylabel,
        )

    summary_path = output_path / "comparison_summary.txt"
    with open(summary_path, "w") as f:
        f.write("Model Comparison Summary\n")
        f.write("=" * 80 + "\n\n")
        for model_name, metrics in results.items():
            f.write(f"Model: {model_name}\n")
            f.write(f"  Val Loss:  {metrics.get('val_loss', float('inf')):.4f}\n")
            f.write(f"  Val MAE:   {metrics.get('val_mae', float('inf')):.4f}\n")
            f.write(f"  Val MSE:   {metrics.get('val_mse', float('inf')):.4f}\n")
            f.write(f"  Val RMSE:  {metrics.get('val_rmse', float('inf')):.4f}\n")
            f.write(f"  Val R²:    {metrics.get('val_r2', float('-inf')):.4f}\n")
            f.write(f"  Best Epoch: {metrics.get('best_epoch', -1)}\n")
            f.write("\n")

    print(f"Comparison plots saved to {output_dir}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Compare model results and generate plots")
    parser.add_argument("--results", type=str, default="./outputs/tables/results.json", help="Path to results JSON")
    parser.add_argument("--output-dir", type=str, default="./outputs/comparison", help="Output directory for plots")
    args = parser.parse_args()

    compare_models(args.results, args.output_dir)


if __name__ == "__main__":
    main()
