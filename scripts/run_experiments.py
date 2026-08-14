import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple

import numpy as np
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from engine import Tester, Trainer, Validator
from losses import build_loss
from metrics import Evaluator
from models import build_model
from utils.misc import get_device


EXPERIMENTS = [
    # Fusion Study (existing - preserves results)
    {"id": "image_only", "config": "baseline_image_only", "type": "fusion"},
    {"id": "gis_only", "config": "baseline_gis_only", "type": "fusion"},
    {"id": "concat", "config": "baseline_concat", "type": "fusion"},
    {"id": "addition", "config": "baseline_addition", "type": "fusion"},
    {"id": "gated", "config": "baseline_gated", "type": "fusion"},
    {"id": "cross_attention", "config": "baseline_cross_attention", "type": "fusion"},
    {"id": "multihead_cross_attention", "config": "baseline_multihead_cross_attention", "type": "fusion"},
    {"id": "bilinear", "config": "baseline_bilinear", "type": "fusion"},
    # Controlled Baselines (new - Addition fusion + alternative relation module)
    {"id": "baseline_gcm", "config": "baselines/baseline_gcm", "type": "baseline"},
    {"id": "baseline_vit", "config": "baselines/baseline_vit", "type": "baseline"},
    {"id": "baseline_swin", "config": "baselines/baseline_swin", "type": "baseline"},
    {"id": "baseline_graphsage", "config": "baselines/baseline_graphsage", "type": "baseline"},
    {"id": "baseline_mha", "config": "baselines/baseline_mha", "type": "baseline"},
    {"id": "baseline_nonlocal", "config": "baselines/baseline_nonlocal", "type": "baseline"},
    # GCM Ablation Study (new - Addition + GCM with component removal)
    {"id": "full_gcm", "config": "gcm_ablation/full_gcm", "type": "ablation"},
    {"id": "no_distance", "config": "gcm_ablation/no_distance", "type": "ablation"},
    {"id": "no_similarity", "config": "gcm_ablation/no_similarity", "type": "ablation"},
    {"id": "no_road", "config": "gcm_ablation/no_road", "type": "ablation"},
    {"id": "no_urban", "config": "gcm_ablation/no_urban", "type": "ablation"},
    {"id": "no_learned", "config": "gcm_ablation/no_learned", "type": "ablation"},
    {"id": "no_scene_weights", "config": "gcm_ablation/no_scene_weights", "type": "ablation"},
]


def run_training(experiment: Dict, device: torch.device, epochs: int = 100) -> Optional[str]:
    config_name = experiment["config"]
    exp_id = experiment["id"]
    print(f"\n{'='*60}")
    print(f"Training: {exp_id} (config={config_name})")
    print(f"{'='*60}")

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)

    from datasets.transforms import get_train_transforms

    train_dataset = GCMHAIRNetDataset(
        root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
        split="train",
        transforms=get_train_transforms(),
    )
    val_dataset = GCMHAIRNetDataset(
        root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
        split="val",
        transforms=get_val_transforms(),
    )

    train_loader = build_dataloader(
        train_dataset,
        batch_size=config.get("dataset", {}).get("train_batch_size", 16),
        shuffle=True,
        num_workers=0,
        pin_memory=(device.type == "cuda"),
        drop_last=True,
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
    trainer = Trainer(model, train_loader, val_loader, config, device)
    trainer.fit()

    best_path = Path(config.get("checkpoint", {}).get("dir", "./checkpoints")) / "best.pt"
    return str(best_path) if best_path.exists() else None


def run_evaluation(experiment: Dict, checkpoint_path: str, device: torch.device, split: str = "test") -> Dict:
    config_name = experiment["config"]
    exp_id = experiment["id"]
    print(f"\nEvaluating {exp_id} on {split}...")

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)

    if split == "val":
        dataset = GCMHAIRNetDataset(
            root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
            split="val",
            transforms=get_val_transforms(),
        )
    else:
        dataset = GCMHAIRNetDataset(
            root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
            split="test",
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

    loss_fn = build_loss(config.get("training", {}).get("loss", {}))
    evaluator = Evaluator()

    all_preds = []
    all_targets = []
    all_cities = []
    city_metrics = {}

    with torch.no_grad():
        for batch in loader:
            image = batch["image"].to(device)
            gis = batch["gis"].to(device)
            label = batch["label"].to(device)
            city_names = batch.get("city_name", ["unknown"] * image.shape[0])

            preds = model(image, gis)
            preds_prob = torch.sigmoid(preds)

            all_preds.append(preds_prob.cpu().numpy())
            all_targets.append(label.cpu().numpy())
            all_cities.extend(city_names)

            for i, city in enumerate(city_names):
                if city not in city_metrics:
                    city_metrics[city] = {"preds": [], "targets": []}
                city_metrics[city]["preds"].append(preds_prob[i].cpu().numpy().flatten())
                city_metrics[city]["targets"].append(label[i].cpu().numpy().flatten())

    preds_all = np.concatenate(all_preds, axis=0)
    targets_all = np.concatenate(all_targets, axis=0)
    metrics = evaluator(preds_all, targets_all)

    per_city = {}
    for city, data in city_metrics.items():
        city_preds = np.concatenate([p.reshape(1, -1) for p in data["preds"]], axis=0).flatten()
        city_targets = np.concatenate([t.reshape(1, -1) for t in data["targets"]], axis=0).flatten()
        city_eval = Evaluator()
        city_metrics_dict = city_eval(city_preds, city_targets)
        per_city[city] = city_metrics_dict

    result = {
        "experiment_id": exp_id,
        "split": split,
        "metrics": metrics,
        "per_city": per_city,
        "num_samples": len(targets_all),
    }
    return result


def save_common_results(results: List[Dict], output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)

    experiment_map = {e["id"]: e for e in EXPERIMENTS}

    existing_rows = []
    fieldnames = ["experiment_category", "model", "variant", "val_loss", "test_loss", "mse", "mae", "r2"]
    if output_path.exists():
        with open(output_path, "r") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row.get("variant") not in {r["experiment_id"] for r in results}:
                    existing_rows.append(row)

    model_name_map = {
        "image_only": "ImageOnly",
        "gis_only": "GISOnly",
        "concat": "Concat",
        "addition": "Addition",
        "gated": "Gated",
        "cross_attention": "CrossAttention",
        "multihead_cross_attention": "MultiHeadCrossAttention",
        "bilinear": "Bilinear",
        "baseline_gcm": "GCM-HAIRNet",
        "baseline_vit": "ViT",
        "baseline_swin": "Swin",
        "baseline_graphsage": "GraphSAGE",
        "baseline_mha": "MHA",
        "baseline_nonlocal": "Non-Local",
    }

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in existing_rows:
            writer.writerow(row)

        test_results = {r["experiment_id"]: r for r in results if r.get("split") == "test"}
        val_results = {r["experiment_id"]: r for r in results if r.get("split") == "val"}

        for exp_id, test_res in test_results.items():
            exp = experiment_map.get(exp_id, {})
            exp_type = exp.get("type", "unknown")

            if exp_type == "fusion":
                category = "fusion"
                model = model_name_map.get(exp_id, exp_id.replace("_", "-").title())
            elif exp_type == "baseline":
                category = "baseline"
                model = model_name_map.get(exp_id, exp_id.replace("baseline_", "").title())
            else:
                category = "ablation"
                model = "GCM"

            if exp_type == "ablation":
                variant = "full" if exp_id == "full_gcm" else exp_id
            else:
                variant = "default"
            val_res = val_results.get(exp_id, {})

            writer.writerow({
                "experiment_category": category,
                "model": model,
                "variant": variant,
                "val_loss": val_res.get("metrics", {}).get("mse", ""),
                "test_loss": test_res.get("metrics", {}).get("mse", ""),
                "mse": test_res.get("metrics", {}).get("mse", ""),
                "mae": test_res.get("metrics", {}).get("mae", ""),
                "r2": test_res.get("metrics", {}).get("r2", ""),
            })


def save_results(results: List[Dict], output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)

    summary = []
    for res in results:
        row = {"experiment": res["experiment_id"], "split": res["split"]}
        row.update(res["metrics"])
        summary.append(row)

    csv_path = output_dir / "all_metrics.csv"
    if summary:
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=summary[0].keys())
            writer.writeheader()
            writer.writerows(summary)

    json_path = output_dir / "all_metrics.json"
    with open(json_path, "w") as f:
        json.dump(results, f, indent=2, default=str)

    print(f"\nResults saved to {csv_path} and {json_path}")


def generate_comparison_plots(results: List[Dict], output_dir: Path):
    import matplotlib.pyplot as plt

    output_dir.mkdir(parents=True, exist_ok=True)
    test_results = [r for r in results if r["split"] == "test"]

    for metric in ["mse", "mae", "r2"]:
        names = [r["experiment_id"] for r in test_results]
        values = [r["metrics"].get(metric, 0.0) for r in test_results]

        fig, ax = plt.subplots(figsize=(12, 6))
        colors = ["#2ecc71" if "baseline" in n else "#3498db" if "ablation" in n else "#e74c3c" for n in names]
        bars = ax.bar(names, values, color=colors)
        ax.set_title(f"Test {metric.upper()} Comparison", fontsize=14, fontweight="bold")
        ax.set_ylabel(metric.upper(), fontsize=12)
        ax.tick_params(axis="x", rotation=45, labelsize=9)
        ax.grid(axis="y", alpha=0.3)

        for bar, val in zip(bars, values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{val:.4f}", ha="center", va="bottom", fontsize=8)

        plt.tight_layout()
        plt.savefig(output_dir / f"test_{metric}_comparison.png", dpi=150, bbox_inches="tight")
        plt.close(fig)

    print(f"Comparison plots saved to {output_dir}")


def generate_per_city_csv(results: List[Dict], output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    test_results = [r for r in results if r["split"] == "test"]

    rows = []
    for res in test_results:
        exp_id = res["experiment_id"]
        for city, metrics in res.get("per_city", {}).items():
            row = {"experiment": exp_id, "city": city}
            row.update(metrics)
            rows.append(row)

    if rows:
        csv_path = output_dir / "per_city_metrics.csv"
        with open(csv_path, "w", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=rows[0].keys())
            writer.writeheader()
            writer.writerows(rows)
        print(f"Per-city metrics saved to {csv_path}")


def generate_scene_weights(experiment: Dict, checkpoint_path: str, device: torch.device, output_dir: Path):
    config_name = experiment["config"]
    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)

    dataset = GCMHAIRNetDataset(
        root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
        split="test",
        transforms=get_val_transforms(),
    )
    loader = build_dataloader(
        dataset,
        batch_size=1,
        shuffle=False,
        num_workers=0,
        drop_last=False,
    )

    model = build_model(config.get("model", {}))
    checkpoint = torch.load(checkpoint_path, map_location=device)
    model.load_state_dict(checkpoint["model_state_dict"], strict=False)
    model.to(device)
    model.eval()

    all_weights = []
    all_cities = []

    with torch.no_grad():
        for batch in loader:
            image = batch["image"].to(device)
            gis = batch["gis"].to(device)
            city = batch.get("city_name", ["unknown"])[0]

            scene_weight_module = None
            if hasattr(model, "gcm") and hasattr(model.gcm, "grm") and hasattr(model.gcm.grm, "scene_weight_predictor"):
                scene_weight_module = model.gcm.grm.scene_weight_predictor
            elif hasattr(model, "relation_module") and hasattr(model.relation_module, "gcm_transformer"):
                grm = model.relation_module.gcm_transformer.grm
                if hasattr(grm, "scene_weight_predictor"):
                    scene_weight_module = grm.scene_weight_predictor

            if scene_weight_module is not None:
                weights = scene_weight_module(gis)
                all_weights.append(weights.cpu().numpy().mean(axis=0))
                all_cities.append(city)

    if all_weights:
        output_dir.mkdir(parents=True, exist_ok=True)
        weights_arr = np.array(all_weights)
        csv_path = output_dir / "scene_weights.csv"
        with open(csv_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["city", "distance", "similarity", "road", "urban", "learned"])
            for city, w in zip(all_cities, weights_arr):
                writer.writerow([city] + [f"{x:.4f}" for x in w])

        mean_weights = weights_arr.mean(axis=0)
        std_weights = weights_arr.std(axis=0)
        print(f"Scene weights: distance={mean_weights[0]:.4f}, similarity={mean_weights[1]:.4f}, road={mean_weights[2]:.4f}, urban={mean_weights[3]:.4f}, learned={mean_weights[4]:.4f}")
        print(f"Scene weights saved to {csv_path}")


def main():
    parser = argparse.ArgumentParser(description="Run all baseline and ablation experiments")
    parser.add_argument("--config", type=str, default="train", help="Base config name")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--output-dir", type=str, default="./outputs", help="Output directory")
    parser.add_argument("--epochs", type=int, default=100, help="Number of epochs")
    parser.add_argument("--skip-train", action="store_true", help="Skip training, only evaluate existing checkpoints")
    parser.add_argument("--experiments", type=str, default=None, help="Comma-separated experiment IDs to run")
    args = parser.parse_args()

    device = get_device(args.device)
    output_dir = Path(args.output_dir)

    selected = EXPERIMENTS
    if args.experiments:
        selected = [e for e in EXPERIMENTS if e["id"] in args.experiments.split(",")]
        if not selected:
            print(f"No experiments match: {args.experiments}")
            return

    results = []

    for experiment in selected:
        exp_id = experiment["id"]
        exp_type = experiment["type"]
        config_name = experiment["config"]

        config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
        config = config_manager.load(config_name)
        ckpt_dir = Path(config.get("checkpoint", {}).get("dir", f"./checkpoints/{exp_type}/{exp_id}"))
        best_path = ckpt_dir / "best.pt"

        if not args.skip_train:
            trained_path = run_training(experiment, device, epochs=args.epochs)
            if trained_path:
                best_path = Path(trained_path)

        if best_path.exists():
            for split in ["val", "test"]:
                result = run_evaluation(experiment, str(best_path), device, split=split)
                results.append(result)

                metrics_dir = output_dir / "experiments" / exp_type / exp_id
                metrics_dir.mkdir(parents=True, exist_ok=True)
                with open(metrics_dir / f"{split}_metrics.json", "w") as f:
                    json.dump(result, f, indent=2, default=str)

            if exp_type == "ablation" or exp_id in ["full"]:
                generate_scene_weights(experiment, str(best_path), device, output_dir / "experiments" / exp_type / exp_id / "attention")
        else:
            print(f"Warning: No checkpoint found for {exp_id} at {best_path}")

    save_results(results, output_dir / "tables")
    generate_comparison_plots(results, output_dir / "comparison")
    generate_per_city_csv(results, output_dir / "tables")
    save_common_results(results, output_dir / "experiments" / "results" / "experiment_results.csv")

    print(f"\n{'='*60}")
    print("All experiments completed!")
    print(f"Results: {output_dir}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
