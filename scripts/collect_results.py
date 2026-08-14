import json
import os
from pathlib import Path
from typing import Dict, List

import torch


def collect_results(checkpoint_dirs: List[str], output_dir: str = "./outputs/tables") -> Dict[str, Dict[str, float]]:
    results = {}
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for ckpt_dir in checkpoint_dirs:
        ckpt_path = Path(ckpt_dir)
        if not ckpt_path.exists():
            continue

        best_metrics = None
        best_loss = float("inf")
        best_epoch = -1

        for ckpt_file in sorted(ckpt_path.glob("*.pt")):
            try:
                checkpoint = torch.load(ckpt_file, map_location="cpu")
                if "metrics" not in checkpoint:
                    continue
                metrics = checkpoint["metrics"]
                val_loss = metrics.get("val_loss", float("inf"))
                if val_loss < best_loss:
                    best_loss = val_loss
                    best_metrics = metrics
                    best_epoch = checkpoint.get("epoch", -1)
            except Exception:
                continue

        if best_metrics:
            model_name = ckpt_path.parent.name
            run_name = ckpt_path.name
            key = f"{model_name}/{run_name}"
            results[key] = {
                "val_loss": best_metrics.get("val_loss", float("inf")),
                "val_mae": best_metrics.get("mae", float("inf")),
                "val_mse": best_metrics.get("mse", float("inf")),
                "val_rmse": best_metrics.get("rmse", float("inf")),
                "val_r2": best_metrics.get("r2", float("-inf")),
                "val_mape": best_metrics.get("mape", float("inf")),
                "best_epoch": best_epoch,
            }

    if results:
        json_path = output_path / "results.json"
        with open(json_path, "w") as f:
            json.dump(results, f, indent=2)

        csv_path = output_path / "results.csv"
        with open(csv_path, "w") as f:
            f.write("model,val_loss,val_mae,val_mse,val_rmse,val_r2,val_mape,best_epoch\n")
            for key, metrics in results.items():
                f.write(f"{key},{metrics['val_loss']},{metrics['val_mae']},{metrics['val_mse']},{metrics['val_rmse']},{metrics['val_r2']},{metrics['val_mape']},{metrics['best_epoch']}\n")

    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Collect experiment results from checkpoints")
    parser.add_argument("--checkpoint-dirs", nargs="+", default=[
        "./checkpoints/baseline/resnet",
        "./checkpoints/baseline/vit",
        "./checkpoints/baseline/swin",
        "./checkpoints/baseline/image_only",
        "./checkpoints/baseline/gis_only",
        "./checkpoints/gcm",
        "./checkpoints/ablation",
        "./checkpoints/crossval",
    ], help="Checkpoint directories to scan")
    parser.add_argument("--output-dir", type=str, default="./outputs/tables", help="Output directory")
    args = parser.parse_args()

    results = collect_results(args.checkpoint_dirs, args.output_dir)
    print(f"Collected results for {len(results)} models:")
    for model_name, metrics in results.items():
        print(f"  {model_name}: val_loss={metrics['val_loss']:.4f}, val_mae={metrics['val_mae']:.4f}")


if __name__ == "__main__":
    main()
