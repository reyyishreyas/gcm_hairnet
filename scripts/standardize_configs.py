#!/usr/bin/env python3
"""Standardize all config files to match canonical GCM+Addition training parameters."""

import yaml
from pathlib import Path

CONFIG_DIR = Path("configs")

CANONICAL_TRAINING = {
    "early_stopping": {"mode": "min", "monitor": "val_loss", "patience": 15},
    "epochs": 100,
    "gradient_accumulation_steps": 1,
    "gradient_clip_val": 1.0,
    "loss": {
        "focal_alpha": 0.25,
        "focal_gamma": 2.0,
        "focal_weight": 0.0,
        "huber_delta": 0.1,
        "huber_weight": 0.5,
        "l1_weight": 0.5,
        "mse_weight": 1.0,
        "type": "combined",
    },
    "optimizer": {
        "betas": [0.9, 0.999],
        "lr": 1.0e-4,
        "weight_decay": 1.0e-4,
    },
    "scheduler": {
        "T_max": 100,
        "eta_min": 1.0e-6,
        "type": "cosine_annealing",
        "warmup_epochs": 5,
    },
}

CANONICAL_DATASET = {
    "augmentation": True,
    "num_workers": 0,
    "pin_memory": True,
    "prefetch_factor": 2,
    "drop_last": True,
    "persistent_workers": False,
    "train_batch_size": 16,
    "val_batch_size": 32,
    "test_batch_size": 32,
}

CANONICAL_CHECKPOINT = {
    "every_n_epochs": 1,
    "monitor": "val_loss",
    "mode": "min",
    "save_last": True,
    "save_top_k": 5,
}


def standardize_config(path: Path):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    
    if not config:
        return False
    
    modified = False
    
    # Standardize training section
    if "training" in config:
        # Merge canonical training params
        for key, value in CANONICAL_TRAINING.items():
            if key not in config["training"]:
                config["training"][key] = value
                modified = True
            elif isinstance(value, dict) and isinstance(config["training"][key], dict):
                for subkey, subvalue in value.items():
                    if subkey not in config["training"][key]:
                        config["training"][key][subkey] = subvalue
                        modified = True
        
        # Fix loss weights if present
        if "loss" in config["training"]:
            loss = config["training"]["loss"]
            canonical_loss = CANONICAL_TRAINING["loss"]
            for key in ["mse_weight", "l1_weight", "huber_weight", "focal_weight"]:
                if key in loss and key in canonical_loss:
                    if loss[key] != canonical_loss[key]:
                        print(f"  {path.name}: Fixing loss.{key}: {loss[key]} -> {canonical_loss[key]}")
                        loss[key] = canonical_loss[key]
                        modified = True
        
        # Fix optimizer if present
        if "optimizer" in config["training"]:
            opt = config["training"]["optimizer"]
            canonical_opt = CANONICAL_TRAINING["optimizer"]
            for key in ["lr", "weight_decay", "betas"]:
                if key in canonical_opt:
                    if key not in opt or opt[key] != canonical_opt[key]:
                        print(f"  {path.name}: Fixing optimizer.{key}: {opt.get(key)} -> {canonical_opt[key]}")
                        opt[key] = canonical_opt[key]
                        modified = True
        
        # Fix epochs
        if "epochs" in config["training"]:
            if config["training"]["epochs"] != 100:
                print(f"  {path.name}: Fixing epochs: {config['training']['epochs']} -> 100")
                config["training"]["epochs"] = 100
                modified = True
        
        # Fix gradient_clip_val
        if "gradient_clip_val" not in config["training"]:
            config["training"]["gradient_clip_val"] = 1.0
            modified = True
    
    # Standardize checkpoint section
    if "checkpoint" in config:
        for key, value in CANONICAL_CHECKPOINT.items():
            if key not in config["checkpoint"]:
                config["checkpoint"][key] = value
                modified = True
    
    # Standardize dataset section
    if "dataset" in config:
        for key, value in CANONICAL_DATASET.items():
            if key not in config["dataset"]:
                config["dataset"][key] = value
                modified = True
    
    if modified:
        with open(path, "w") as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)
        print(f"  Updated: {path}")
    
    return modified


def main():
    updated = 0
    for yaml_file in CONFIG_DIR.rglob("*.yaml"):
        if yaml_file.name in ["dataset.yaml", "inference.yaml", "model.yaml"]:
            continue
        if standardize_config(yaml_file):
            updated += 1
    
    print(f"\nUpdated {updated} config files")
    
    # Also fix the default in losses/combined.py
    combined_path = Path("losses/combined.py")
    if combined_path.exists():
        content = combined_path.read_text()
        if 'l1_weight: float = 0.1' in content:
            content = content.replace('l1_weight: float = 0.1', 'l1_weight: float = 0.5')
            combined_path.write_text(content)
            print(f"Fixed default l1_weight in {combined_path}")
        elif 'l1_weight=0.1' in content:
            content = content.replace('l1_weight=0.1', 'l1_weight=0.5')
            combined_path.write_text(content)
            print(f"Fixed default l1_weight in {combined_path}")


if __name__ == "__main__":
    main()
