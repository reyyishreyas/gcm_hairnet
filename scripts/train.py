from pathlib import Path
import argparse
import sys
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_train_transforms, get_val_transforms
from engine import Trainer
from models import build_model
from utils.misc import get_device


def main():
    parser = argparse.ArgumentParser(description="Train GCM-HAIRNet")
    parser.add_argument("--config", type=str, default="train", help="Config name (without .yaml)")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root directory")
    parser.add_argument("--checkpoint", type=str, default=None, help="Checkpoint to resume from")
    parser.add_argument("--device", type=str, default=None, help="Device to use")
    parser.add_argument("--output-dir", type=str, default="./outputs", help="Output directory")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)

    device = get_device(args.device)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    norm_stats_path = config.get("data", {}).get("normalization_stats")
    norm_stats = None
    if norm_stats_path:
        norm_stats_file = Path(norm_stats_path)
        if norm_stats_file.exists():
            import json
            with open(norm_stats_file, "r") as f:
                norm_stats = json.load(f)

    train_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split="train",
        transforms=get_train_transforms(normalization_stats=norm_stats),
    )
    val_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split="val",
        transforms=get_val_transforms(normalization_stats=norm_stats),
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
    vis_dir = str(Path(args.output_dir) / "gcm_attention")
    trainer = Trainer(model, train_loader, val_loader, config, device, vis_dir=vis_dir)

    if args.checkpoint:
        trainer.resume(args.checkpoint)

    trainer.fit()


if __name__ == "__main__":
    main()
