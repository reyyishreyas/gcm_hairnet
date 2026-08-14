import argparse
import sys
from pathlib import Path
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from engine import Tester
from losses import build_loss
from metrics import Evaluator
from models import build_model
from utils.logger import Logger
from utils.misc import get_device


def main():
    parser = argparse.ArgumentParser(description="Test GCM-HAIRNet")
    parser.add_argument("--config", type=str, default="train", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--output-dir", type=str, default="./outputs/test", help="Output directory")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)

    test_dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
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
    logger = Logger(log_dir="./logs", experiment_name="test", use_tensorboard=True)
    metrics = Evaluator()

    tester = Tester(model, test_loader, loss_fn, device, metrics, logger)
    test_metrics, preds, targets, cities = tester.test()

    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    import numpy as np
    np.save(output_dir / "test_predictions.npy", np.concatenate(preds, axis=0))
    np.save(output_dir / "test_targets.npy", np.concatenate(targets, axis=0))

    print("Test Metrics:")
    for k, v in test_metrics.items():
        print(f"  {k}: {v:.4f}")

    logger.close()


if __name__ == "__main__":
    main()
