import argparse
import csv
import json
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from engine import Validator
from losses import build_loss
from metrics import Evaluator
from models import build_model
from utils.misc import get_device


EXPERIMENTS = [
    {"id": "image_only", "config": "baseline_image_only", "type": "fusion", "label": "Image-Only"},
    {"id": "gis_only", "config": "baseline_gis_only", "type": "fusion", "label": "GIS-Only"},
    {"id": "concat", "config": "baseline_concat", "type": "fusion", "label": "Concat"},
    {"id": "addition", "config": "baseline_addition", "type": "fusion", "label": "Addition"},
    {"id": "gated", "config": "baseline_gated", "type": "fusion", "label": "Gated"},
    {"id": "cross_attention", "config": "baseline_cross_attention", "type": "fusion", "label": "Cross-Attention"},
    {"id": "multihead_cross_attention", "config": "baseline_multihead_cross_attention", "type": "fusion", "label": "MultiHead-Cross-Attention"},
    {"id": "bilinear", "config": "baseline_bilinear", "type": "fusion", "label": "Bilinear"},
    {"id": "gcm", "config": "train", "type": "main", "label": "GCM-HAIRNet"},
    {"id": "improved_full", "config": "improved_full", "type": "main", "label": "Improved-Full"},
    {"id": "improved_small", "config": "improved_full_small", "type": "main", "label": "Improved-Small"},
    {"id": "tiny_cnn", "config": "baseline_tiny_cnn", "type": "baseline", "label": "TinyRiskCNN"},
    {"id": "baseline_gcm", "config": "baselines/baseline_gcm", "type": "baseline", "label": "Baseline-GCM"},
    {"id": "baseline_vit", "config": "baselines/baseline_vit", "type": "baseline", "label": "ViT"},
    {"id": "baseline_swin", "config": "baselines/baseline_swin", "type": "baseline", "label": "Swin"},
    {"id": "baseline_graphsage", "config": "baselines/baseline_graphsage", "type": "baseline", "label": "GraphSAGE"},
    {"id": "baseline_mha", "config": "baselines/baseline_mha", "type": "baseline", "label": "MHA"},
    {"id": "baseline_nonlocal", "config": "baselines/baseline_nonlocal", "type": "baseline", "label": "Non-Local"},
    {"id": "full_gcm", "config": "gcm_ablation/full_gcm", "type": "ablation", "label": "GCM-Full"},
    {"id": "no_distance", "config": "gcm_ablation/no_distance", "type": "ablation", "label": "GCM-NoDistance"},
    {"id": "no_similarity", "config": "gcm_ablation/no_similarity", "type": "ablation", "label": "GCM-NoSimilarity"},
    {"id": "no_road", "config": "gcm_ablation/no_road", "type": "ablation", "label": "GCM-NoRoad"},
    {"id": "no_urban", "config": "gcm_ablation/no_urban", "type": "ablation", "label": "GCM-NoUrban"},
    {"id": "no_learned", "config": "gcm_ablation/no_learned", "type": "ablation", "label": "GCM-NoLearned"},
    {"id": "no_scene_weights", "config": "gcm_ablation/no_scene_weights", "type": "ablation", "label": "GCM-NoSceneWeights"},
]


def find_best_checkpoint(config: Dict) -> Optional[Path]:
    ckpt_dir = Path(config.get("checkpoint", {}).get("dir", "./checkpoints"))
    if not ckpt_dir.exists():
        return None
    candidates = sorted(ckpt_dir.glob("best.pt"))
    if not candidates:
        candidates = sorted(ckpt_dir.glob("*.pt"))
    return candidates[0] if candidates else None


def extract_model_params(config: Dict) -> Dict[str, Any]:
    model_cfg = config.get("model", {})
    training_cfg = config.get("training", {})
    dataset_cfg = config.get("dataset", {})
    optimizer_cfg = training_cfg.get("optimizer", {})
    scheduler_cfg = training_cfg.get("scheduler", {})
    loss_cfg = training_cfg.get("loss", {})
    checkpoint_cfg = config.get("checkpoint", {})

    image_enc = model_cfg.get("image_encoder", {})
    gis_enc = model_cfg.get("gis_encoder", {})
    gct = model_cfg.get("gct", {})
    grm = model_cfg.get("grm", {})
    decoder = model_cfg.get("decoder", {})
    gcm = model_cfg.get("gcm", {})

    return {
        "model_name": model_cfg.get("name", "Unknown"),
        "image_encoder_type": image_enc.get("type", ""),
        "image_encoder_pretrained": image_enc.get("pretrained", False),
        "image_encoder_embed_dim": image_enc.get("embed_dim", ""),
        "image_encoder_depths": str(image_enc.get("depths", ""))[1:-1].replace(" ", ""),
        "image_encoder_num_heads": str(image_enc.get("num_heads", ""))[1:-1].replace(" ", ""),
        "image_encoder_window_size": image_enc.get("window_size", ""),
        "image_encoder_drop_path_rate": image_enc.get("drop_path_rate", ""),
        "gis_encoder_type": gis_enc.get("type", ""),
        "gis_encoder_input_channels": gis_enc.get("input_channels", ""),
        "gis_encoder_hidden_dim": gis_enc.get("hidden_dim", ""),
        "gis_encoder_output_dim": gis_enc.get("output_dim", ""),
        "gis_encoder_dropout": gis_enc.get("dropout", ""),
        "gct_type": gct.get("type", ""),
        "gct_hidden_dim": gct.get("hidden_dim", ""),
        "gct_num_heads": gct.get("num_heads", ""),
        "gct_dropout": gct.get("dropout", ""),
        "grm_type": grm.get("type", ""),
        "grm_hidden_dim": grm.get("hidden_dim", ""),
        "grm_num_relations": grm.get("num_relations", ""),
        "grm_num_layers": grm.get("num_layers", ""),
        "grm_dropout": grm.get("dropout", ""),
        "decoder_type": decoder.get("type", ""),
        "decoder_hidden_dim": decoder.get("hidden_dim", ""),
        "decoder_num_classes": decoder.get("num_classes", ""),
        "decoder_dropout": decoder.get("dropout", ""),
        "gcm_enable": gcm.get("enable", False),
        "gcm_embed_dim": gcm.get("embed_dim", ""),
        "gcm_num_heads": gcm.get("num_heads", ""),
        "gcm_num_blocks": gcm.get("num_blocks", ""),
        "gcm_num_semantic_heads": gcm.get("num_semantic_heads", ""),
        "gcm_mlp_ratio": gcm.get("mlp_ratio", ""),
        "gcm_dropout": gcm.get("dropout", ""),
        "gcm_gate_init": gcm.get("gate_init", ""),
        "gcm_sigma_distance": gcm.get("sigma_distance", ""),
        "gcm_scene_weight_hidden": gcm.get("scene_weight_hidden", ""),
        "gcm_gis_channels": gcm.get("gis_channels", ""),
        "gcm_gis_feature_dim": gcm.get("gis_feature_dim", ""),
        "gcm_grid_size": gcm.get("grid_size", ""),
        "gcm_enable_distance": gcm.get("enable_distance", ""),
        "gcm_enable_similarity": gcm.get("enable_similarity", ""),
        "gcm_enable_road": gcm.get("enable_road", ""),
        "gcm_enable_urban": gcm.get("enable_urban", ""),
        "gcm_enable_learned": gcm.get("enable_learned", ""),
        "gcm_enable_scene_weights": gcm.get("enable_scene_weights", ""),
        "fusion_type": model_cfg.get("fusion", {}).get("type", ""),
        "relation_module_type": model_cfg.get("relation_module", {}).get("type", ""),
        "epochs": training_cfg.get("epochs", ""),
        "optimizer_type": optimizer_cfg.get("type", ""),
        "learning_rate": optimizer_cfg.get("lr", ""),
        "weight_decay": optimizer_cfg.get("weight_decay", ""),
        "betas": str(optimizer_cfg.get("betas", ""))[1:-1].replace(" ", ""),
        "scheduler_type": scheduler_cfg.get("type", ""),
        "scheduler_T_max": scheduler_cfg.get("T_max", ""),
        "scheduler_eta_min": scheduler_cfg.get("eta_min", ""),
        "scheduler_warmup_epochs": scheduler_cfg.get("warmup_epochs", ""),
        "loss_type": loss_cfg.get("type", ""),
        "loss_mse_weight": loss_cfg.get("mse_weight", ""),
        "loss_l1_weight": loss_cfg.get("l1_weight", ""),
        "loss_focal_weight": loss_cfg.get("focal_weight", ""),
        "loss_focal_alpha": loss_cfg.get("focal_alpha", ""),
        "loss_focal_gamma": loss_cfg.get("focal_gamma", ""),
        "loss_huber_weight": loss_cfg.get("huber_weight", ""),
        "loss_huber_delta": loss_cfg.get("huber_delta", ""),
        "loss_ssim_weight": loss_cfg.get("ssim_weight", ""),
        "loss_ssim_window_size": loss_cfg.get("ssim_window_size", ""),
        "gradient_clip_val": training_cfg.get("gradient_clip_val", ""),
        "gradient_accumulation_steps": training_cfg.get("gradient_accumulation_steps", ""),
        "train_batch_size": dataset_cfg.get("train_batch_size", ""),
        "val_batch_size": dataset_cfg.get("val_batch_size", ""),
        "test_batch_size": dataset_cfg.get("test_batch_size", ""),
        "num_workers": dataset_cfg.get("num_workers", ""),
        "augmentation": dataset_cfg.get("augmentation", ""),
        "early_stopping_patience": training_cfg.get("early_stopping", {}).get("patience", ""),
        "early_stopping_monitor": training_cfg.get("early_stopping", {}).get("monitor", ""),
        "early_stopping_mode": training_cfg.get("early_stopping", {}).get("mode", ""),
        "checkpoint_dir": checkpoint_cfg.get("dir", ""),
        "checkpoint_save_top_k": checkpoint_cfg.get("save_top_k", ""),
        "checkpoint_every_n_epochs": checkpoint_cfg.get("every_n_epochs", ""),
        "seed": config.get("experiment", {}).get("seed", ""),
        "deterministic": config.get("experiment", {}).get("deterministic", ""),
    }


def run_validation(config: Dict, checkpoint_path: Path, device: torch.device) -> Dict[str, float]:
    val_dataset = GCMHAIRNetDataset(
        root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
        split="val",
        transforms=get_val_transforms(),
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
    checkpoint = torch.load(checkpoint_path, map_location=device)
    ckpt_state = checkpoint.get("model_state_dict", checkpoint)
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
        for batch in val_loader:
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
    metrics["val_loss"] = total_loss / max(num_batches, 1)
    return metrics


def count_parameters(model: torch.nn.Module) -> Dict[str, int]:
    total = sum(p.numel() for p in model.parameters())
    trainable = sum(p.numel() for p in model.parameters() if p.requires_grad)
    return {"total_params": total, "trainable_params": trainable}


def main():
    parser = argparse.ArgumentParser(description="Generate final research-paper results CSV")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device to use")
    parser.add_argument("--output", type=str, default="./outputs/final_results.csv", help="Output CSV path")
    parser.add_argument("--skip-val", action="store_true", help="Skip validation, use existing metrics only")
    args = parser.parse_args()

    device = get_device(args.device)
    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        "experiment_id", "experiment_type", "label",
        "model_name",
        "image_encoder_type", "image_encoder_pretrained", "image_encoder_embed_dim",
        "image_encoder_depths", "image_encoder_num_heads", "image_encoder_window_size", "image_encoder_drop_path_rate",
        "gis_encoder_type", "gis_encoder_input_channels", "gis_encoder_hidden_dim", "gis_encoder_output_dim", "gis_encoder_dropout",
        "gct_type", "gct_hidden_dim", "gct_num_heads", "gct_dropout",
        "grm_type", "grm_hidden_dim", "grm_num_relations", "grm_num_layers", "grm_dropout",
        "decoder_type", "decoder_hidden_dim", "decoder_num_classes", "decoder_dropout",
        "gcm_enable", "gcm_embed_dim", "gcm_num_heads", "gcm_num_blocks", "gcm_num_semantic_heads",
        "gcm_mlp_ratio", "gcm_dropout", "gcm_gate_init", "gcm_sigma_distance", "gcm_scene_weight_hidden",
        "gcm_gis_channels", "gcm_gis_feature_dim", "gcm_grid_size",
        "gcm_enable_distance", "gcm_enable_similarity", "gcm_enable_road", "gcm_enable_urban",
        "gcm_enable_learned", "gcm_enable_scene_weights",
        "fusion_type", "relation_module_type",
        "epochs", "optimizer_type", "learning_rate", "weight_decay", "betas",
        "scheduler_type", "scheduler_T_max", "scheduler_eta_min", "scheduler_warmup_epochs",
        "loss_type", "loss_mse_weight", "loss_l1_weight", "loss_focal_weight",
        "loss_focal_alpha", "loss_focal_gamma", "loss_huber_weight", "loss_huber_delta",
        "loss_ssim_weight", "loss_ssim_window_size",
        "gradient_clip_val", "gradient_accumulation_steps",
        "train_batch_size", "val_batch_size", "test_batch_size", "num_workers", "augmentation",
        "early_stopping_patience", "early_stopping_monitor", "early_stopping_mode",
        "checkpoint_dir", "checkpoint_save_top_k", "checkpoint_every_n_epochs",
        "seed", "deterministic",
        "total_params", "trainable_params",
        "val_loss", "val_mse", "val_mae", "val_r2", "val_accuracy", "val_f1", "val_precision", "val_recall", "val_iou",
        "test_loss", "test_mse", "test_mae", "test_r2", "test_accuracy", "test_f1", "test_precision", "test_recall", "test_iou",
        "checkpoint_path",
    ]

    rows = []

    for exp in EXPERIMENTS:
        exp_id = exp["id"]
        config_name = exp["config"]
        print(f"\n{'='*60}")
        print(f"Processing: {exp['label']} ({config_name})")
        print(f"{'='*60}")

        try:
            config = config_manager.load(config_name)
        except Exception as e:
            print(f"  Failed to load config: {e}")
            continue

        best_path = find_best_checkpoint(config)
        if best_path is None:
            print(f"  No checkpoint found, skipping.")
            continue

        print(f"  Checkpoint: {best_path}")

        row = extract_model_params(config)
        row["experiment_id"] = exp_id
        row["experiment_type"] = exp["type"]
        row["label"] = exp["label"]
        row["checkpoint_path"] = str(best_path)

        try:
            model = build_model(config.get("model", {}))
            param_info = count_parameters(model)
            row["total_params"] = param_info["total_params"]
            row["trainable_params"] = param_info["trainable_params"]
            print(f"  Parameters: {param_info['total_params']:,}")
        except Exception as e:
            print(f"  Failed to build model for param count: {e}")
            row["total_params"] = ""
            row["trainable_params"] = ""

        val_metrics = {}
        test_metrics = {}
        if not args.skip_val:
            try:
                val_metrics = run_validation(config, best_path, device)
                row.update({
                    "val_loss": round(val_metrics.get("val_loss", val_metrics.get("loss", "")), 6),
                    "val_mse": round(val_metrics.get("mse", ""), 6),
                    "val_mae": round(val_metrics.get("mae", ""), 6),
                    "val_r2": round(val_metrics.get("r2", ""), 6),
                    "val_accuracy": round(val_metrics.get("accuracy", ""), 6),
                    "val_f1": round(val_metrics.get("f1", ""), 6),
                    "val_precision": round(val_metrics.get("precision", ""), 6),
                    "val_recall": round(val_metrics.get("recall", ""), 6),
                    "val_iou": round(val_metrics.get("iou", ""), 6),
                })
                print(f"  Val: MSE={val_metrics.get('mse', 'N/A'):.6f}, R2={val_metrics.get('r2', 'N/A'):.6f}")
            except Exception as e:
                print(f"  Validation failed: {e}")

            try:
                test_dataset = GCMHAIRNetDataset(
                    root_dir=config.get("data", {}).get("root_dir", "./data/processed"),
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
                checkpoint = torch.load(best_path, map_location=device)
                ckpt_state = checkpoint.get("model_state_dict", checkpoint)
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
                all_preds, all_targets = [], []
                total_loss, num_batches = 0.0, 0

                with torch.no_grad():
                    for batch in test_loader:
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
                test_metrics = evaluator(preds_all, targets_all)
                test_metrics["loss"] = total_loss / max(num_batches, 1)

                row.update({
                    "test_loss": round(test_metrics.get("loss", ""), 6),
                    "test_mse": round(test_metrics.get("mse", ""), 6),
                    "test_mae": round(test_metrics.get("mae", ""), 6),
                    "test_r2": round(test_metrics.get("r2", ""), 6),
                    "test_accuracy": round(test_metrics.get("accuracy", ""), 6),
                    "test_f1": round(test_metrics.get("f1", ""), 6),
                    "test_precision": round(test_metrics.get("precision", ""), 6),
                    "test_recall": round(test_metrics.get("recall", ""), 6),
                    "test_iou": round(test_metrics.get("iou", ""), 6),
                })
                print(f"  Test: MSE={test_metrics.get('mse', 'N/A'):.6f}, R2={test_metrics.get('r2', 'N/A'):.6f}")
            except Exception as e:
                print(f"  Test failed: {e}")

        rows.append(row)

    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"\n{'='*60}")
    print(f"Final results saved to: {output_path}")
    print(f"Total experiments: {len(rows)}")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
