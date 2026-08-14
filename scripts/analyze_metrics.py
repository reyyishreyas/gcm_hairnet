import sys
from pathlib import Path
import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from models import build_model
from utils.misc import get_device


def analyze_predictions(model_name, config_name, checkpoint_path, device, root_dir="./data/processed"):
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

    print(f"\n{'='*60}")
    print(f"Model: {model_name}")
    print(f"{'='*60}")

    print("\n1. THRESHOLD USED")
    print("   Threshold: 0.5")
    print("   Method: torch.sigmoid(output) > 0.5")
    print("   Safe = 0 (pred <= 0.5), Hazardous = 1 (pred > 0.5)")

    print("\n2. CLASS DISTRIBUTION IN TEST SET")
    total_pixels = targets_by_image.size
    hazardous_pixels = np.sum(targets_by_image > 0.5)
    safe_pixels = total_pixels - hazardous_pixels
    print(f"   Total images: {len(image_city_names)}")
    print(f"   Total pixels: {total_pixels:,}")
    print(f"   Safe (<= 0.5): {safe_pixels:,} ({safe_pixels/total_pixels*100:.2f}%)")
    print(f"   Hazardous (> 0.5): {hazardous_pixels:,} ({hazardous_pixels/total_pixels*100:.2f}%)")

    print("\n3. PIXEL-WISE CLASSIFICATION METRICS (threshold=0.5)")
    threshold = 0.5
    preds_flat = preds_by_image.flatten()
    targets_flat = targets_by_image.flatten()
    preds_bin = (preds_flat > threshold).astype(int)
    targets_bin = (targets_flat > threshold).astype(int)

    tp = np.sum((preds_bin == 1) & (targets_bin == 1))
    fp = np.sum((preds_bin == 1) & (targets_bin == 0))
    tn = np.sum((preds_bin == 0) & (targets_bin == 0))
    fn = np.sum((preds_bin == 0) & (targets_bin == 1))

    accuracy = (tp + tn) / (tp + tn + fp + fn + 1e-8)
    precision = tp / (tp + fp + 1e-8)
    recall = tp / (tp + fn + 1e-8)
    f1 = 2 * precision * recall / (precision + recall + 1e-8)
    iou = tp / (tp + fp + fn + 1e-8)
    specificity = tn / (tn + fp + 1e-8)

    print(f"   Accuracy:  {accuracy:.4f}")
    print(f"   Precision: {precision:.4f}")
    print(f"   Recall:    {recall:.4f}")
    print(f"   F1:        {f1:.4f}")
    print(f"   IoU:       {iou:.4f}")
    print(f"   Specificity: {specificity:.4f}")

    print("\n4. CONFUSION MATRIX")
    print(f"                 Predicted")
    print(f"                 Safe    Hazardous")
    print(f"   Actual Safe   {tn:6d}   {fp:6d}")
    print(f"   Actual Hazard {fn:6d}   {tp:6d}")
    print(f"\n   TP={tp}, FP={fp}, TN={tn}, FN={fn}")

    print("\n5. REGRESSION METRICS")
    mse = np.mean((preds_flat - targets_flat) ** 2)
    mae = np.mean(np.abs(preds_flat - targets_flat))
    ss_res = np.sum((targets_flat - preds_flat) ** 2)
    ss_tot = np.sum((targets_flat - np.mean(targets_flat)) ** 2)
    r2 = 1 - ss_res / (ss_tot + 1e-8)
    print(f"   MSE: {mse:.6f}")
    print(f"   MAE: {mae:.6f}")
    print(f"   R2:  {r2:.4f}")

    print("\n6. PER-CITY BREAKDOWN")
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
        city_acc = np.mean(cb == ctb)
        city_tp = np.sum((cb == 1) & (ctb == 1))
        city_fp = np.sum((cb == 1) & (ctb == 0))
        city_tn = np.sum((cb == 0) & (ctb == 0))
        city_fn = np.sum((cb == 0) & (ctb == 1))
        city_precision = city_tp / (city_tp + city_fp + 1e-8)
        city_recall = city_tp / (city_tp + city_fn + 1e-8)
        city_f1 = 2 * city_precision * city_recall / (city_precision + city_recall + 1e-8)
        city_iou = city_tp / (city_tp + city_fp + city_fn + 1e-8)
        city_mse = np.mean((cp - ct) ** 2)
        city_mae = np.mean(np.abs(cp - ct))
        ss_res_c = np.sum((ct - cp) ** 2)
        ss_tot_c = np.sum((ct - np.mean(ct)) ** 2)
        city_r2 = 1 - ss_res_c / (ss_tot_c + 1e-8)
        print(f"   {city}: n_images={len(city_data[city]['preds'])}, n_pixels={len(cp)}, Acc={city_acc:.4f}, Prec={city_precision:.4f}, Rec={city_recall:.4f}, F1={city_f1:.4f}, IoU={city_iou:.4f}, MSE={city_mse:.6f}, MAE={city_mae:.6f}, R2={city_r2:.4f}")


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, default="gcm", choices=["gcm", "vit", "swin", "graphsage", "mha", "nonlocal"])
    parser.add_argument("--checkpoint", type=str, default=None)
    parser.add_argument("--root-dir", type=str, default="./data/processed")
    parser.add_argument("--device", type=str, default=None)
    args = parser.parse_args()

    device = get_device(args.device)

    model_configs = {
        "gcm": ("baselines/baseline_gcm", "./checkpoints/baselines/gcm/epoch_0103.pt"),
        "vit": ("baselines/baseline_vit", "./checkpoints/baselines/vit/best.pt"),
        "swin": ("baselines/baseline_swin", "./checkpoints/baselines/swin/best.pt"),
        "graphsage": ("baselines/baseline_graphsage", "./checkpoints/baselines/graphsage/best.pt"),
        "mha": ("baselines/baseline_mha", "./checkpoints/baselines/mha/best.pt"),
        "nonlocal": ("baselines/baseline_nonlocal", "./checkpoints/baselines/nonlocal/best.pt"),
    }

    if args.checkpoint:
        config_name, ckpt = args.model, args.checkpoint
    else:
        config_name, ckpt = model_configs[args.model]

    analyze_predictions(args.model.upper(), config_name, ckpt, device, args.root_dir)


if __name__ == "__main__":
    main()
