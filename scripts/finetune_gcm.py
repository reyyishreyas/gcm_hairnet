import argparse
import sys
from pathlib import Path

import torch

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_train_transforms, get_val_transforms
from engine import Trainer
from models import build_model
from utils.misc import get_device


class DynamicLR:
    def __init__(self, optimizer, init_lr, factor=0.5, patience=10, min_lr=1e-7, max_lr=1e-3, increase_factor=1.05):
        self.optimizer = optimizer
        self.current_lr = init_lr
        self.factor = factor
        self.patience = patience
        self.min_lr = min_lr
        self.max_lr = max_lr
        self.increase_factor = increase_factor
        self.best_loss = float("inf")
        self.num_bad_epochs = 0
        self.consecutive_improvements = 0

        for param_group in optimizer.param_groups:
            param_group["lr"] = init_lr

    def step(self, val_loss):
        if val_loss < self.best_loss:
            self.best_loss = val_loss
            self.num_bad_epochs = 0
            self.consecutive_improvements += 1
            if self.consecutive_improvements >= 3:
                self.current_lr = min(self.current_lr * self.increase_factor, self.max_lr)
                for param_group in self.optimizer.param_groups:
                    param_group["lr"] = self.current_lr
                self.consecutive_improvements = 0
                return f"LR increased to {self.current_lr:.2e}"
        else:
            self.num_bad_epochs += 1
            self.consecutive_improvements = 0
            if self.num_bad_epochs >= self.patience:
                self.current_lr = max(self.current_lr * self.factor, self.min_lr)
                for param_group in self.optimizer.param_groups:
                    param_group["lr"] = self.current_lr
                self.num_bad_epochs = 0
                return f"LR decreased to {self.current_lr:.2e}"
        return None


def main():
    parser = argparse.ArgumentParser(description="Dynamic fine-tune GCM-HAIRNet with auto LR adjustment")
    parser.add_argument("--config", type=str, default="baselines/baseline_gcm", help="Config name")
    parser.add_argument("--checkpoint", type=str, default="./checkpoints/baselines/gcm/last.pt", help="Checkpoint to resume from")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root directory")
    parser.add_argument("--device", type=str, default=None, help="Device to use (cuda, mps, cpu)")
    parser.add_argument("--output-dir", type=str, default="./outputs/baselines/gcm", help="Output directory")
    parser.add_argument("--lr", type=float, default=1e-4, help="Initial fine-tuning learning rate")
    parser.add_argument("--additional-epochs", type=int, default=100, help="Additional epochs to train beyond current checkpoint")
    parser.add_argument("--patience", type=int, default=10, help="LR reduction patience")
    parser.add_argument("--factor", type=float, default=0.5, help="LR reduction factor")
    parser.add_argument("--min-lr", type=float, default=1e-7, help="Minimum learning rate")
    parser.add_argument("--max-lr", type=float, default=1e-3, help="Maximum learning rate")
    parser.add_argument("--increase-factor", type=float, default=1.05, help="LR increase factor when improving")
    parser.add_argument("--grad-clip", type=float, default=1.0, help="Gradient clipping value")
    parser.add_argument("--early-stopping-patience", type=int, default=30, help="Early stopping patience")
    args = parser.parse_args()

    device = get_device(args.device)

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)

    checkpoint_path = Path(args.checkpoint)
    if not checkpoint_path.exists():
        print(f"Checkpoint not found: {checkpoint_path}")
        sys.exit(1)

    ckpt = torch.load(checkpoint_path, map_location="cpu")
    start_epoch = ckpt.get("epoch", 0) + 1
    total_epochs = start_epoch + args.additional_epochs

    config["training.epochs"] = total_epochs
    config["training.optimizer.lr"] = args.lr
    config["training.gradient_clip_val"] = args.grad_clip
    config["training.early_stopping.patience"] = args.early_stopping_patience
    config["outputs.root_dir"] = args.output_dir

    train_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split="train",
        transforms=get_train_transforms(),
    )
    val_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
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
    model.load_state_dict(ckpt["model_state_dict"], strict=False)
    model.to(device)
    print(f"Loaded model weights from: {checkpoint_path}")

    vis_dir = str(Path(args.output_dir) / "gcm_attention")
    trainer = Trainer(model, train_loader, val_loader, config, device, vis_dir=vis_dir)

    for param_group in trainer.optimizer.param_groups:
        param_group["lr"] = args.lr
    print(f"Fine-tuning learning rate set to: {args.lr}")

    dynamic_lr = DynamicLR(
        trainer.optimizer,
        init_lr=args.lr,
        factor=args.factor,
        patience=args.patience,
        min_lr=args.min_lr,
        max_lr=args.max_lr,
        increase_factor=args.increase_factor,
    )

    def epoch_callback(epoch, val_metrics):
        val_loss = val_metrics.get("val_loss", float("inf"))
        lr_msg = dynamic_lr.step(val_loss)
        if lr_msg:
            print(f"  -> {lr_msg}")

    trainer.epoch = start_epoch
    trainer.num_epochs = total_epochs
    print(f"Resuming from epoch {start_epoch}, training until epoch {total_epochs}")

    trainer.fit(epoch_callback=epoch_callback)


if __name__ == "__main__":
    main()
