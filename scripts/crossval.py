import argparse
import sys
from pathlib import Path
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_crossval_dataloaders, get_train_transforms, get_val_transforms
from engine import Trainer
from models import build_model
from utils.misc import get_device


def main():
    parser = argparse.ArgumentParser(description="Run cross-validation for GCM-HAIRNet")
    parser.add_argument("--config", type=str, default="crossval", help="Config name")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--output-dir", type=str, default="./outputs/crossval", help="Output directory")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)
    output_dir = Path(args.output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    cv_config = config.get("cross_validation", {})
    num_folds = cv_config.get("folds", 5)
    seed = config.get("experiment", {}).get("seed", 42)

    fold_results = {}

    for fold in range(num_folds):
        print(f"\n{'='*50}")
        print(f"Fold {fold + 1}/{num_folds}")
        print(f"{'='*50}")

        train_loader, val_loader = build_crossval_dataloaders(
            root_dir=args.root_dir,
            fold=fold,
            num_folds=num_folds,
            batch_size=config.get("dataset", {}).get("train_batch_size", 16),
            num_workers=0,
            seed=seed,
            transforms_train=get_train_transforms(),
            transforms_val=get_val_transforms(),
        )

        model = build_model(config.get("model", {}))
        trainer = Trainer(model, train_loader, val_loader, config, device)
        trainer.fit()

        fold_results[f"fold_{fold}"] = {
            "best_val_loss": trainer.checkpoint_manager.best_value,
        }

    import json
    with open(output_dir / "crossval_results.json", "w") as f:
        json.dump(fold_results, f, indent=2)

    print(f"\nCross-validation complete. Results saved to {output_dir / 'crossval_results.json'}")


if __name__ == "__main__":
    main()
