import argparse
import sys
from pathlib import Path
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from engine import Validator
from losses import build_loss
from metrics import Evaluator
from models import build_model
from utils.logger import Logger
from utils.misc import get_device


def main():
    parser = argparse.ArgumentParser(description="Validate GCM-HAIRNet")
    parser.add_argument("--config", type=str, default="train", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)

    val_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
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
    checkpoint = torch.load(args.checkpoint, map_location=device)
    ckpt_state = checkpoint["model_state_dict"]
    model_state = model.state_dict()
    new_state = {}
    matched = 0
    skipped = 0
    for key, param in ckpt_state.items():
        if key in model_state:
            if param.shape == model_state[key].shape:
                new_state[key] = param
                matched += 1
            else:
                skipped += 1
        else:
            skipped += 1
    result = model.load_state_dict(new_state, strict=False)
    if result.missing_keys or result.unexpected_keys:
        print(f"Warning: Partial checkpoint load - missing: {result.missing_keys}, unexpected: {result.unexpected_keys}")
    if skipped > 0:
        print(f"Info: Loaded {matched} layers, skipped {skipped} incompatible layers from checkpoint")
    model.to(device)
    model.eval()

    loss_fn = build_loss(config.get("training", {}).get("loss", {}))
    logger = Logger(log_dir="./logs", experiment_name="validation", use_tensorboard=True)
    metrics = Evaluator()

    validator = Validator(model, val_loader, loss_fn, device, metrics, logger)
    val_metrics = validator.validate()

    print("Validation Metrics:")
    for k, v in val_metrics.items():
        print(f"  {k}: {v:.4f}")

    if hasattr(logger, "log_metrics"):
        logger.log_metrics(val_metrics, step=0, prefix="val")

    logger.close()


if __name__ == "__main__":
    main()
