import json
import sys
from pathlib import Path
import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from models import build_model
from utils.misc import get_device


def evaluate_model(model_name, config_name, checkpoint_path, device, root_dir="./data/processed"):
    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)

    test_dataset = GCMHAIRNetDataset(
        root_dir=root_dir,
        split="test",
        transforms=get_val_transforms(),
    )
    test_loader = build_dataloader(
        test_dataset,
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

    all_preds = []
    all_targets = []
    image_city_names = []

    with torch.no_grad():
        for batch in test_loader:
            image = batch["image"].to(device)
            gis = batch["gis"].to(device)
            label = batch["label"].to(device)
            preds = model(image, gis)
            preds_prob = torch.sigmoid(preds)

            batch_size = image.shape[0]
            pixels_per_image = image.shape[2] * image.shape[3]

            batch_preds = preds_prob.cpu().numpy().reshape(batch_size, pixels_per_image)
            batch_targets = label.cpu().numpy().reshape(batch_size, pixels_per_image)
            all_preds.append(batch_preds)
            all_targets.append(batch_targets)

            city_names = batch.get("city_name", ["unknown"] * batch_size)
            image_city_names.extend(city_names)

    preds_by_image = np.concatenate(all_preds, axis=0)
    targets_by_image = np.concatenate(all_targets, axis=0)
    preds_flat = preds_by_image.flatten()
    targets_flat = targets_by_image.flatten()

    threshold = 0.5
    preds_bin = (preds_flat > threshold).astype(int)
    targets_bin = (targets_flat > threshold).astype(int)

    tp = float(np.sum((preds_bin == 1) & (targets_bin == 1)))
    fp = float(np.sum((preds_bin == 1) & (targets_bin == 0)))
    tn = float(np.sum((preds_bin == 0) & (targets_bin == 0)))
    fn = float(np.sum((preds_bin == 0) & (targets_bin == 1)))

    accuracy = (tp + tn) / (tp + tn + fp + fn + 1e-8)
    precision = tp / (tp + fp + 1e-8)
    recall = tp / (tp + fn + 1e-8)
    f1 = 2 * precision * recall / (precision + recall + 1e-8)
    iou = tp / (tp + fp + fn + 1e-8)
    specificity = tn / (tn + fp + 1e-8)

    mse = float(np.mean((preds_flat - targets_flat) ** 2))
    mae = float(np.mean(np.abs(preds_flat - targets_flat)))
    ss_res = np.sum((targets_flat - preds_flat) ** 2)
    ss_tot = np.sum((targets_flat - np.mean(targets_flat)) ** 2)
    r2 = float(1 - ss_res / (ss_tot + 1e-8))

    total_pixels = int(targets_flat.size)
    hazardous_pixels = int(np.sum(targets_flat > 0.5))
    safe_pixels = total_pixels - hazardous_pixels

    per_city = {}
    unique_cities = sorted(set(image_city_names))
    city_data = {c: {"preds": [], "targets": []} for c in unique_cities}

    for i, city in enumerate(image_city_names):
        city_data[city]["preds"].append(preds_by_image[i])
        city_data[city]["targets"].append(targets_by_image[i])

    for city in unique_cities:
        cp = np.concatenate(city_data[city]["preds"]).flatten()
        ct = np.concatenate(city_data[city]["targets"]).flatten()
        cb = (cp > 0.5).astype(int)
        ctb = (ct > 0.5).astype(int)
        city_acc = float(np.mean(cb == ctb))
        city_tp = float(np.sum((cb == 1) & (ctb == 1)))
        city_fp = float(np.sum((cb == 1) & (ctb == 0)))
        city_tn = float(np.sum((cb == 0) & (ctb == 0)))
        city_fn = float(np.sum((cb == 0) & (ctb == 1)))
        city_precision = city_tp / (city_tp + city_fp + 1e-8)
        city_recall = city_tp / (city_tp + city_fn + 1e-8)
        city_f1 = 2 * city_precision * city_recall / (city_precision + city_recall + 1e-8)
        city_iou = city_tp / (city_tp + city_fp + city_fn + 1e-8)
        city_mse = float(np.mean((cp - ct) ** 2))
        city_mae = float(np.mean(np.abs(cp - ct)))
        ss_res_c = np.sum((ct - cp) ** 2)
        ss_tot_c = np.sum((ct - np.mean(ct)) ** 2)
        city_r2 = float(1 - ss_res_c / (ss_tot_c + 1e-8))

        per_city[city] = {
            "n_images": len(city_data[city]["preds"]),
            "n_pixels": len(cp),
            "accuracy": city_acc,
            "precision": city_precision,
            "recall": city_recall,
            "f1": city_f1,
            "iou": city_iou,
            "mse": city_mse,
            "mae": city_mae,
            "r2": city_r2,
            "safe_pixels": int(np.sum(ct <= 0.5)),
            "hazardous_pixels": int(np.sum(ct > 0.5)),
        }

    result = {
        "model_name": model_name,
        "config": config_name,
        "checkpoint": checkpoint_path,
        "threshold": threshold,
        "class_distribution": {
            "total_pixels": total_pixels,
            "safe_pixels": safe_pixels,
            "hazardous_pixels": hazardous_pixels,
            "safe_percentage": round(safe_pixels / total_pixels * 100, 2),
            "hazardous_percentage": round(hazardous_pixels / total_pixels * 100, 2),
        },
        "overall_metrics": {
            "accuracy": accuracy,
            "precision": precision,
            "recall": recall,
            "f1": f1,
            "iou": iou,
            "specificity": specificity,
            "mse": mse,
            "mae": mae,
            "r2": r2,
        },
        "confusion_matrix": {
            "tp": tp,
            "fp": fp,
            "tn": tn,
            "fn": fn,
        },
        "per_city": per_city,
    }

    return result


def main():
    device = get_device(None)
    print(f"Using device: {device}")

    baseline_dir = Path("./checkpoints/baselines")
    output_path = Path("./outputs/baselines/all_baseline_metrics.json")
    output_path.parent.mkdir(parents=True, exist_ok=True)

    model_configs = {
        "addition": "baseline_addition",
        "bilinear": "baseline_bilinear",
        "concat": "baseline_concat",
        "cross_attention": "baseline_cross_attention",
        "gated": "baseline_gated",
        "gcm": "baselines/baseline_gcm",
        "gis_only": "baseline_gis_only",
        "image_only": "baseline_image_only",
        "multihead_cross_attention": "baseline_multihead_cross_attention",
        "swin": "baselines/baseline_swin",
        "vit": "baselines/baseline_vit",
        "graphsage": "baselines/baseline_graphsage",
        "mha": "baselines/baseline_mha",
        "nonlocal": "baselines/baseline_nonlocal",
    }

    results = {}
    missing = []
    skipped = []

    for model_name, config_name in model_configs.items():
        ckpt_dir = baseline_dir / model_name
        best_path = ckpt_dir / "best.pt"

        if not best_path.exists():
            missing.append(f"{model_name}: {best_path}")
            continue

        print(f"\nEvaluating {model_name} ...")
        try:
            result = evaluate_model(model_name, config_name, str(best_path), device)
            results[model_name] = result
            print(f"  -> Acc={result['overall_metrics']['accuracy']:.4f}, R2={result['overall_metrics']['r2']:.4f}")
        except Exception as e:
            skipped.append(f"{model_name}: {e}")
            print(f"  -> SKIPPED: {e}")

    output = {
        "evaluated": results,
        "missing_checkpoints": missing,
        "skipped_models": skipped,
        "note": "Fusion study models (addition, bilinear, concat, etc.) use BaselineModel. New controlled baselines (gcm, vit, swin, etc.) use GCMHAIRNetBaseline.",
    }

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2, default=str)

    print(f"\n{'='*60}")
    print(f"Evaluated: {len(results)} models")
    print(f"Missing:   {len(missing)} models")
    print(f"Skipped:   {len(skipped)} models")
    print(f"Saved to:  {output_path}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
