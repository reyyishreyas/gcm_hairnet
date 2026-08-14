import argparse
import csv
import json
import shutil
import sys
from pathlib import Path
from typing import Dict, List, Optional

import numpy as np
import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms, get_train_transforms
from engine import Tester, Trainer, Validator
from losses import build_loss
from metrics import Evaluator
from models import build_model
from utils.misc import get_device


BASELINE_EXPERIMENTS = [
    {"id": "gcm", "config": "baselines/baseline_gcm", "label": "GCM-HAIRNet"},
    {"id": "vit", "config": "baselines/baseline_vit", "label": "ViT"},
    {"id": "swin", "config": "baselines/baseline_swin", "label": "Swin"},
    {"id": "graphsage", "config": "baselines/baseline_graphsage", "label": "GraphSAGE"},
    {"id": "mha", "config": "baselines/baseline_mha", "label": "MHA"},
    {"id": "nonlocal", "config": "baselines/baseline_nonlocal", "label": "Non-Local"},
]

BASELINE_CONFIG_FILES = {
    "gcm": "baseline_gcm",
    "vit": "baseline_vit",
    "swin": "baseline_swin",
    "graphsage": "baseline_graphsage",
    "mha": "baseline_mha",
    "nonlocal": "baseline_nonlocal",
}


ABLATION_EXPERIMENTS = [
    {"id": "full_gcm", "config": "gcm_ablation/full_gcm", "label": "Full GCM"},
    {"id": "no_distance", "config": "gcm_ablation/no_distance", "label": "GCM - Distance Prior"},
    {"id": "no_similarity", "config": "gcm_ablation/no_similarity", "label": "GCM - Similarity Prior"},
    {"id": "no_road", "config": "gcm_ablation/no_road", "label": "GCM - Road Prior"},
    {"id": "no_urban", "config": "gcm_ablation/no_urban", "label": "GCM - Urban Prior"},
    {"id": "no_learned", "config": "gcm_ablation/no_learned", "label": "GCM - Learned Relation"},
    {"id": "no_scene_weights", "config": "gcm_ablation/no_scene_weights", "label": "GCM - Scene Weights"},
]


def _make_json_serializable(obj):
    if isinstance(obj, dict):
        return {k: _make_json_serializable(v) for k, v in obj.items()}
    if isinstance(obj, (list, tuple)):
        return [_make_json_serializable(item) for item in obj]
    if isinstance(obj, (np.floating, np.float32, np.float64)):
        return float(obj)
    if isinstance(obj, (np.integer, np.int32, np.int64)):
        return int(obj)
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    return obj


def run_training(config_name: str, device: torch.device, root_dir: str, epochs: int = 100) -> Optional[str]:
    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)
    config["training"]["epochs"] = epochs

    train_dataset = GCMHAIRNetDataset(
        root_dir=root_dir,
        split="train",
        transforms=get_train_transforms(),
    )
    val_dataset = GCMHAIRNetDataset(
        root_dir=root_dir,
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
    vis_dir = str(Path(config.get("outputs", {}).get("root_dir", "./outputs")) / "gcm_attention")
    trainer = Trainer(model, train_loader, val_loader, config, device, vis_dir=vis_dir)
    trainer.fit()

    best_path = Path(config.get("checkpoint", {}).get("dir", "./checkpoints")) / "best.pt"
    return str(best_path) if best_path.exists() else None


def run_evaluation(config_name: str, checkpoint_path: str, device: torch.device, root_dir: str, split: str = "test") -> Dict:
    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)

    if split == "val":
        dataset = GCMHAIRNetDataset(
            root_dir=root_dir,
            split="val",
            transforms=get_val_transforms(),
        )
    else:
        dataset = GCMHAIRNetDataset(
            root_dir=root_dir,
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
    total_loss = 0.0
    num_batches = 0

    with torch.no_grad():
        for batch in loader:
            image = batch["image"].to(device)
            gis = batch["gis"].to(device)
            label = batch["label"].to(device)

            preds = model(image, gis)
            loss = loss_fn(preds, label)
            total_loss += loss.item()
            num_batches += 1

            preds_prob = torch.sigmoid(preds)
            all_preds.append(preds_prob.cpu().numpy())
            all_targets.append(label.cpu().numpy())

    preds_all = np.concatenate(all_preds, axis=0)
    targets_all = np.concatenate(all_targets, axis=0)
    metrics = evaluator(preds_all, targets_all)
    metrics["loss"] = total_loss / max(num_batches, 1)
    return metrics


def save_results_csv(results: List[Dict], output_path: Path):
    output_path.parent.mkdir(parents=True, exist_ok=True)
    existing_rows = []
    if output_path.exists():
        with open(output_path, "r") as f:
            reader = csv.DictReader(f)
            existing_rows = list(reader)

    fieldnames = ["experiment_category", "model", "variant", "val_loss", "test_loss", "mse", "mae", "r2"]
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()

        for row in existing_rows:
            if row.get("model") not in [r["model"] for r in results]:
                writer.writerow(row)

        for res in results:
            writer.writerow(res)


def run_baseline_study(args):
    device = get_device(args.device)
    root_dir = args.root_dir
    output_dir = Path(args.output_dir)
    results_path = output_dir / "experiments" / "results" / "experiment_results.csv"

    experiments_to_run = []
    if args.experiments:
        exp_ids = args.experiments.split(",")
        experiments_to_run = [e for e in BASELINE_EXPERIMENTS + ABLATION_EXPERIMENTS if e["id"] in exp_ids]
    else:
        experiments_to_run = BASELINE_EXPERIMENTS + ABLATION_EXPERIMENTS

    results = []

    for exp in experiments_to_run:
        exp_id = exp["id"]
        config_name = exp["config"]
        label = exp["label"]
        print(f"\n{'='*60}")
        print(f"Running: {label} (config={config_name})")
        print(f"{'='*60}")

        config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
        config = config_manager.load(config_name)

        ckpt_dir = Path(config.get("checkpoint", {}).get("dir", f"./checkpoints/{exp_id}"))
        best_path = ckpt_dir / "best.pt"

        if exp_id == "gcm":
            skip_train = False
            train_epochs = 100
            print(f"Training gcm for {train_epochs} epochs from scratch.")
        else:
            skip_train = args.skip_train
            train_epochs = 100
            if hasattr(args, "train_only_untrained") and args.train_only_untrained:
                if best_path.exists():
                    skip_train = True
                    print(f"Checkpoint already exists at {best_path}, skipping training.")
                else:
                    print(f"No checkpoint found at {best_path}, will train.")

        if not skip_train:
            trained_path = run_training(config_name, device, root_dir, epochs=train_epochs)
            if trained_path:
                best_path = Path(trained_path)

        if best_path.exists():
            val_metrics = run_evaluation(config_name, str(best_path), device, root_dir, split="val")
            test_metrics = run_evaluation(config_name, str(best_path), device, root_dir, split="test")

            category = "baseline" if exp in BASELINE_EXPERIMENTS else "ablation"
            result = {
                "experiment_category": category,
                "model": label.split(" ")[0] if " " in label else label,
                "variant": exp_id,
                "val_loss": round(val_metrics.get("loss", 0), 6),
                "test_loss": round(test_metrics.get("loss", 0), 6),
                "mse": round(test_metrics.get("mse", 0), 6),
                "mae": round(test_metrics.get("mae", 0), 6),
                "r2": round(test_metrics.get("r2", 0), 6),
            }
            results.append(result)
            print(f"Result: MSE={result['mse']:.6f}, R2={result['r2']:.6f}")

            metrics_dir = output_dir / ("baselines" if category == "baseline" else "ablations") / exp_id
            metrics_dir.mkdir(parents=True, exist_ok=True)
            with open(metrics_dir / "test_metrics.json", "w") as f:
                json.dump(_make_json_serializable(test_metrics), f, indent=2)
            with open(metrics_dir / "val_metrics.json", "w") as f:
                json.dump(_make_json_serializable(val_metrics), f, indent=2)
        else:
            print(f"Warning: No checkpoint found for {label} at {best_path}")

    save_results_csv(results, results_path)

    print(f"\n{'='*60}")
    print("Baseline study completed!")
    print(f"Results saved to: {results_path}")
    print(f"{'='*60}")


def copy_existing_fusion_results(output_dir: Path):
    fusion_dir = output_dir / "experiments" / "fusion"
    fusion_dir.mkdir(parents=True, exist_ok=True)

    existing_fusion_dirs = Path("./outputs/baselines").glob("*")
    for d in existing_fusion_dirs:
        if d.name in ["image_only", "gis_only", "concat", "addition", "gated",
                       "cross_attention", "multihead_cross_attention", "bilinear"]:
            dest = fusion_dir / d.name
            if dest.exists():
                shutil.rmtree(dest)
            shutil.copytree(d, dest)

    addition_dir = fusion_dir / "addition"
    if not addition_dir.exists():
        for d in Path("./outputs/baselines").glob("addition"):
            if d.is_dir():
                shutil.copytree(d, addition_dir)
                break


def register_existing_results(output_dir: Path):
    results_path = output_dir / "experiments" / "results" / "experiment_results.csv"
    results_path.parent.mkdir(parents=True, exist_ok=True)

    existing_results = []
    csv_path = Path("./outputs/tables/all_metrics.csv")
    if csv_path.exists():
        import csv as csv_mod
        with open(csv_path, "r") as f:
            reader = csv_mod.DictReader(f)
            for row in reader:
                split = row.get("split", "")
                exp_id = row.get("experiment", "")
                if split == "test":
                    category = "fusion" if exp_id in ["image_only", "gis_only", "concat", "addition", "gated",
                                                       "cross_attention", "multihead_cross_attention", "bilinear"] else (
                        "baseline" if exp_id in ["full"] else "ablation"
                    )
                    model_name = exp_id.replace("_", "-").title() if exp_id != "full" else "GCM-HAIRNet"
                    if exp_id == "addition":
                        model_name = "GCM-HAIRNet"
                    result = {
                        "experiment_category": category,
                        "model": model_name,
                        "variant": exp_id,
                        "val_loss": "",
                        "test_loss": "",
                        "mse": row.get("mse", ""),
                        "mae": row.get("mae", ""),
                        "r2": row.get("r2", ""),
                    }
                    existing_results.append(result)

    if existing_results:
        with open(results_path, "w", newline="") as f:
            fieldnames = ["experiment_category", "model", "variant", "val_loss", "test_loss", "mse", "mae", "r2"]
            writer = csv_mod.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for res in existing_results:
                writer.writerow(res)
        print(f"Registered {len(existing_results)} existing results in {results_path}")


def main():
    parser = argparse.ArgumentParser(description="Run controlled baseline study")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--output-dir", type=str, default="./outputs", help="Output directory")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--epochs", type=int, default=100, help="Number of epochs")
    parser.add_argument("--experiments", type=str, default=None, help="Comma-separated experiment IDs")
    parser.add_argument("--skip-train", action="store_true", help="Skip training, only evaluate")
    parser.add_argument("--train-only-untrained", action="store_true", help="Skip experiments that already have checkpoints")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    register_existing_results(output_dir)
    copy_existing_fusion_results(output_dir)

    run_baseline_study(args)


if __name__ == "__main__":
    main()
