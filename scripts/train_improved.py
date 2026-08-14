import sys
import time
from pathlib import Path
from typing import Dict

import numpy as np
import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_train_transforms, get_val_transforms
from models import build_model
from losses import build_loss
from metrics import Evaluator
from utils.misc import get_device


def evaluate(model, loader, loss_fn, device):
    model.eval()
    metric_fn = Evaluator()
    all_preds, all_targets = [], []
    total_loss, num_batches = 0.0, 0
    with torch.no_grad():
        for batch in loader:
            img = batch["image"].to(device)
            gis = batch["gis"].to(device)
            lab = batch["label"].to(device)
            out = model(img, gis)
            loss = loss_fn(out, lab)
            total_loss += loss.item()
            num_batches += 1
            all_preds.append(torch.sigmoid(out).cpu().numpy())
            all_targets.append(lab.cpu().numpy())
    preds = np.concatenate(all_preds, axis=0)
    targets = np.concatenate(all_targets, axis=0)
    metrics = metric_fn(preds, targets)
    metrics["loss"] = total_loss / max(num_batches, 1)
    return metrics


def main():
    config_name = sys.argv[1] if len(sys.argv) > 1 else "improved_full_fast"
    epochs = int(sys.argv[2]) if len(sys.argv) > 2 else 100

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(config_name)
    device = get_device()
    print(f"Device: {device}", flush=True)

    root_dir = config.get("data", {}).get("root_dir", "./data/processed")

    train_ds = GCMHAIRNetDataset(root_dir=root_dir, split="train", transforms=get_train_transforms())
    val_ds = GCMHAIRNetDataset(root_dir=root_dir, split="val", transforms=get_val_transforms())
    test_ds = GCMHAIRNetDataset(root_dir=root_dir, split="test", transforms=get_val_transforms())
    print(f"Train: {len(train_ds)}, Val: {len(val_ds)}, Test: {len(test_ds)}", flush=True)

    bs = config.get("dataset", {}).get("train_batch_size", 16)
    train_loader = build_dataloader(train_ds, batch_size=bs, shuffle=True, num_workers=0, drop_last=True)
    val_loader = build_dataloader(val_ds, batch_size=32, shuffle=False, num_workers=0, drop_last=False)
    test_loader = build_dataloader(test_ds, batch_size=32, shuffle=False, num_workers=0, drop_last=False)

    torch.manual_seed(config.get("experiment", {}).get("seed", 42))
    model = build_model(config.get("model", {})).to(device)
    print(f"Parameters: {sum(p.numel() for p in model.parameters()):,}", flush=True)

    lr = config.get("training", {}).get("optimizer", {}).get("lr", 1e-4)
    wd = config.get("training", {}).get("optimizer", {}).get("weight_decay", 1e-4)
    betas = tuple(config.get("training", {}).get("optimizer", {}).get("betas", [0.9, 0.999]))
    optimizer = torch.optim.AdamW(model.parameters(), lr=lr, weight_decay=wd, betas=betas)

    sched_cfg = config.get("training", {}).get("scheduler", {})
    warmup = sched_cfg.get("warmup_epochs", 0)
    if sched_cfg.get("type") == "cosine_annealing":
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=sched_cfg.get("T_max", epochs), eta_min=sched_cfg.get("eta_min", 1e-6)
        )
    else:
        scheduler = None

    loss_fn = build_loss(config.get("training", {}).get("loss", {}))
    gclip = config.get("training", {}).get("gradient_clip_val", 1.0)

    ckpt_dir = Path(config.get("checkpoint", {}).get("dir", "./checkpoints/improved"))
    ckpt_dir.mkdir(parents=True, exist_ok=True)

    best_val_r2 = float("-inf")
    best_val_loss = float("inf")
    patience = config.get("training", {}).get("early_stopping", {}).get("patience", 15)
    monitor = config.get("training", {}).get("early_stopping", {}).get("monitor", "val_loss")
    mode = config.get("training", {}).get("early_stopping", {}).get("mode", "min")

    epochs_no_improve = 0

    for epoch in range(epochs):
        t0 = time.time()
        model.train()
        train_loss, n = 0.0, 0
        for batch in train_loader:
            img = batch["image"].to(device)
            gis = batch["gis"].to(device)
            lab = batch["label"].to(device)
            optimizer.zero_grad()
            out = model(img, gis)
            loss = loss_fn(out, lab)
            loss.backward()
            if gclip:
                torch.nn.utils.clip_grad_norm_(model.parameters(), gclip)
            optimizer.step()
            train_loss += loss.item()
            n += 1

        if epoch < warmup and warmup > 0:
            lr_scale = (epoch + 1) / warmup
            for pg in optimizer.param_groups:
                pg["lr"] = lr * lr_scale

        val_metrics = evaluate(model, val_loader, loss_fn, device)

        if scheduler and epoch >= warmup:
            scheduler.step()

        dt = time.time() - t0
        cur_lr = optimizer.param_groups[0]["lr"]
        print(
            f"Epoch {epoch+1:3d}/{epochs}: train_loss={train_loss/n:.4f} "
            f"val_loss={val_metrics['loss']:.4f} val_mse={val_metrics['mse']:.4f} "
            f"val_mae={val_metrics['mae']:.4f} val_r2={val_metrics['r2']:.4f} "
            f"val_acc={val_metrics['accuracy']:.4f} val_f1={val_metrics['f1']:.4f} "
            f"val_iou={val_metrics['iou']:.4f} lr={cur_lr:.6f} time={dt:.1f}s",
            flush=True,
        )

        torch.save(
            {"epoch": epoch, "model_state_dict": model.state_dict(), "optimizer_state_dict": optimizer.state_dict(), "val_metrics": val_metrics},
            ckpt_dir / "last.pt",
        )

        improved = False
        if monitor == "val_loss" and mode == "min":
            improved = val_metrics["loss"] < best_val_loss
            if improved:
                best_val_loss = val_metrics["loss"]
        elif monitor == "r2" and mode == "max":
            improved = val_metrics["r2"] > best_val_r2
            if improved:
                best_val_r2 = val_metrics["r2"]
        if improved:
            torch.save(
                {"epoch": epoch, "model_state_dict": model.state_dict(), "optimizer_state_dict": optimizer.state_dict(), "val_metrics": val_metrics},
                ckpt_dir / "best.pt",
            )
            epochs_no_improve = 0
        else:
            epochs_no_improve += 1

        if patience > 0 and epochs_no_improve >= patience:
            print(f"Early stopping at epoch {epoch+1}", flush=True)
            break

    best = torch.load(ckpt_dir / "best.pt", map_location=device, weights_only=False)
    model.load_state_dict(best["model_state_dict"])

    model.eval()
    metric_fn = Evaluator()
    all_preds, all_targets = [], []
    with torch.no_grad():
        for batch in test_loader:
            img = batch["image"].to(device)
            gis = batch["gis"].to(device)
            lab = batch["label"].to(device)
            out = model(img, gis)
            all_preds.append(torch.sigmoid(out).cpu().numpy())
            all_targets.append(lab.cpu().numpy())
    preds = np.concatenate(all_preds, axis=0)
    targets = np.concatenate(all_targets, axis=0)
    test_metrics = metric_fn(preds, targets)
    test_metrics["loss"] = evaluate(model, test_loader, loss_fn, device)["loss"]
    print(
        f"\nBEST (epoch {best['epoch']}): TEST loss={test_metrics['loss']:.4f} "
        f"mse={test_metrics['mse']:.4f} mae={test_metrics['mae']:.4f} "
        f"r2={test_metrics['r2']:.4f} acc@0.5={test_metrics['accuracy']:.4f} "
        f"f1={test_metrics['f1']:.4f} prec={test_metrics['precision']:.4f} "
        f"rec={test_metrics['recall']:.4f} iou={test_metrics['iou']:.4f}",
        flush=True,
    )

    import json
    with open(ckpt_dir / "test_metrics.json", "w") as f:
        json.dump(test_metrics, f, indent=2, default=str)
    np.save(ckpt_dir / "test_predictions.npy", preds)
    np.save(ckpt_dir / "test_targets.npy", targets)


if __name__ == "__main__":
    main()
