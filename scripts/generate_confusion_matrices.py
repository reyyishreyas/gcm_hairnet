#!/usr/bin/env python3
"""
Generate confusion matrices and threshold analysis for all models.
Computes TP, TN, FP, FN, accuracy, precision, recall, F1, and IoU
at threshold=0.5 for all available test predictions.
"""

import json
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np

MODELS = {
    "GCM-HAIRNet (Addition)": "outputs/experiments/addition/test",
    "Bilinear": "outputs/experiments/bilinear/test",
    "Concatenation": "outputs/experiments/concat/test",
    "Gated": "outputs/experiments/gated/test",
    "Cross-Attention": "outputs/experiments/cross_attention/test",
    "MultiHead-Cross-Attention": "outputs/experiments/multihead_cross_attention/test",
    "GIS-Only": "outputs/experiments/gis_only/test",
    "Image-Only": "outputs/experiments/image_only/test",
    "Controlled GCM": "outputs/experiments/gcm/test",
    "ViT": "outputs/experiments/vit/test",
    "Swin": "outputs/experiments/swin/test",
    "GraphSAGE": "outputs/experiments/graphsage/test",
    "MHA": "outputs/experiments/mha/test",
    "Non-Local": "outputs/experiments/nonlocal/test",
}


def compute_metrics(preds, targets, threshold=0.5):
    pred_binary = (preds >= threshold).astype(int)
    target_binary = (targets >= threshold).astype(int)

    tp = int(((pred_binary == 1) & (target_binary == 1)).sum())
    tn = int(((pred_binary == 0) & (target_binary == 0)).sum())
    fp = int(((pred_binary == 1) & (target_binary == 0)).sum())
    fn = int(((pred_binary == 0) & (target_binary == 1)).sum())
    total = tp + tn + fp + fn

    accuracy = (tp + tn) / total if total > 0 else 0.0
    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0
    iou = tp / (tp + fp + fn) if (tp + fp + fn) > 0 else 0.0

    return {
        "tp": tp,
        "tn": tn,
        "fp": fp,
        "fn": fn,
        "total": total,
        "accuracy": accuracy,
        "precision": precision,
        "recall": recall,
        "f1": f1,
        "iou": iou,
    }


def plot_confusion_matrix(cm, model_name, output_path):
    fig, ax = plt.subplots(figsize=(5, 4))
    data = np.array([[cm["tn"], cm["fp"]], [cm["fn"], cm["tp"]]])
    im = ax.imshow(data, cmap="Blues", aspect="auto")
    ax.set_xticks([0, 1])
    ax.set_yticks([0, 1])
    ax.set_xticklabels(["Predicted Negative", "Predicted Positive"])
    ax.set_yticklabels(["Actual Negative", "Actual Positive"])
    ax.set_xlabel("Prediction")
    ax.set_ylabel("Actual")
    ax.set_title(f"{model_name}\nConfusion Matrix (threshold=0.5)")

    for i in range(2):
        for j in range(2):
            ax.text(j, i, f"{data[i, j]:,}\n({data[i, j]/data.sum()*100:.1f}%)",
                    ha="center", va="center", color="white" if data[i, j] > data.max()/2 else "black",
                    fontsize=10, fontweight="bold")

    plt.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    plt.tight_layout()
    fig.savefig(output_path, dpi=200, bbox_inches="tight", facecolor="white")
    plt.close(fig)
    print(f"Saved: {output_path}")


def main():
    output_dir = Path("outputs/experiments/results")
    output_dir.mkdir(parents=True, exist_ok=True)

    all_results = {}
    print("=" * 110)
    print(f"{'Model':<30} {'TP':>8} {'TN':>8} {'FP':>8} {'FN':>8} {'Accuracy':>10} {'Precision':>10} {'Recall':>10} {'F1':>10} {'IoU':>10}")
    print("=" * 110)

    for name, path in MODELS.items():
        pred_file = Path(path) / "test_predictions.npy"
        target_file = Path(path) / "test_targets.npy"

        if pred_file.exists() and target_file.exists():
            preds = np.load(pred_file).squeeze().flatten()
            targets = np.load(target_file).squeeze().flatten()
            cm = compute_metrics(preds, targets, threshold=0.5)
            all_results[name] = cm

            print(f"{name:<30} {cm['tp']:>8,} {cm['tn']:>8,} {cm['fp']:>8,} {cm['fn']:>8,} "
                  f"{cm['accuracy']:>10.4f} {cm['precision']:>10.4f} {cm['recall']:>10.4f} {cm['f1']:>10.4f} {cm['iou']:>10.4f}")

            plot_confusion_matrix(cm, name, output_dir / f"confusion_matrix_{name.replace(' ', '_').replace('(', '').replace(')', '')}.png")
        else:
            print(f"{name:<30} MISSING prediction files")

    print("=" * 110)

    # Save all results
    with open(output_dir / "confusion_matrices_all_models.json", "w") as f:
        json.dump(all_results, f, indent=2)
    print(f"\nSaved all confusion matrices to {output_dir / 'confusion_matrices_all_models.json'}")

    # Class distribution
    target_file = Path("outputs/experiments/addition/test/test_targets.npy")
    if target_file.exists():
        targets = np.load(target_file).squeeze().flatten()
        target_binary = (targets >= 0.5).astype(int)
        pos = int((target_binary == 1).sum())
        neg = int((target_binary == 0).sum())
        total = len(target_binary)
        print(f"\nClass distribution in test set (threshold=0.5):")
        print(f"  Positive (high risk): {pos:,} ({pos/total:.2%})")
        print(f"  Negative (low risk): {neg:,} ({neg/total:.2%})")
        print(f"  Total pixels: {total:,}")
        print(f"  Trivial accuracy (all-negative): {neg/total:.4f}")


if __name__ == "__main__":
    main()
