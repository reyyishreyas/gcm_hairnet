# GCM-HAIRNet Repository Code

Complete repository source code organized by module, with file descriptions and full implementations.

---

### `__init__.py`

**Purpose:** Implementation of `__init__.py`.

```python

```

---

### `ablation.py`

**Purpose:** Contains `main` function.

```python
import argparse
import sys
from pathlib import Path
from typing import Optional

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from utils.misc import get_device
from utils.ablation import AblationManager
from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from engine import Validator
from losses import build_loss
from metrics import Evaluator
from models import GCMHAIRNet
from utils.logger import Logger


def main():
    parser = argparse.ArgumentParser(description="Run ablation study")
    parser.add_argument("--config", type=str, default="train", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--output-dir", type=str, default="./outputs/ablation", help="Output directory")
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
        num_workers=config.get("dataset", {}).get("num_workers", 4),
        drop_last=False,
    )

    model = GCMHAIRNet(config.get("model", {}))
    checkpoint = torch.load(args.checkpoint, map_location=device)
    model.load_state_dict(checkpoint["model_state_dict"])
    model.to(device)
    model.eval()

    loss_fn = build_loss(config.get("training", {}).get("loss", {}))
    ablation_manager = AblationManager(model, config.to_dict() if hasattr(config, "to_dict") else config)
    results = ablation_manager.run_ablation(val_loader, loss_fn, device)

    import json
    output_path = Path(args.output_dir)
    output_path.mkdir(parents=True, exist_ok=True)
    with open(output_path / "ablation_results.json", "w") as f:
        json.dump(results, f, indent=2)

    print("Ablation Results:")
    for module, loss in results.items():
        print(f"  {module}: {loss:.4f}")


if __name__ == "__main__":
    main()
```

---

### `collect_results.py`

**Purpose:** Contains `collect_results` function.

```python
import json
import os
from pathlib import Path
from typing import Dict, List

import torch


def collect_results(checkpoint_dirs: List[str], output_dir: str = "./outputs/tables") -> Dict[str, Dict[str, float]]:
    results = {}
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    for ckpt_dir in checkpoint_dirs:
        ckpt_path = Path(ckpt_dir)
        if not ckpt_path.exists():
            continue

        best_metrics = None
        best_loss = float("inf")
        best_epoch = -1

        for ckpt_file in sorted(ckpt_path.glob("*.pt")):
            try:
                checkpoint = torch.load(ckpt_file, map_location="cpu")
                if "metrics" not in checkpoint:
                    continue
                metrics = checkpoint["metrics"]
                val_loss = metrics.get("val_loss", float("inf"))
                if val_loss < best_loss:
                    best_loss = val_loss
                    best_metrics = metrics
                    best_epoch = checkpoint.get("epoch", -1)
            except Exception:
                continue

        if best_metrics:
            model_name = ckpt_path.parent.name
            run_name = ckpt_path.name
            key = f"{model_name}/{run_name}"
            results[key] = {
                "val_loss": best_metrics.get("val_loss", float("inf")),
                "val_mae": best_metrics.get("mae", float("inf")),
                "val_mse": best_metrics.get("mse", float("inf")),
                "val_rmse": best_metrics.get("rmse", float("inf")),
                "val_r2": best_metrics.get("r2", float("-inf")),
                "val_mape": best_metrics.get("mape", float("inf")),
                "best_epoch": best_epoch,
            }

    if results:
        json_path = output_path / "results.json"
        with open(json_path, "w") as f:
            json.dump(results, f, indent=2)

        csv_path = output_path / "results.csv"
        with open(csv_path, "w") as f:
            f.write("model,val_loss,val_mae,val_mse,val_rmse,val_r2,val_mape,best_epoch\n")
            for key, metrics in results.items():
                f.write(f"{key},{metrics['val_loss']},{metrics['val_mae']},{metrics['val_mse']},{metrics['val_rmse']},{metrics['val_r2']},{metrics['val_mape']},{metrics['best_epoch']}\n")

    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Collect experiment results from checkpoints")
    parser.add_argument("--checkpoint-dirs", nargs="+", default=[
        "./checkpoints/baseline/resnet",
        "./checkpoints/baseline/vit",
        "./checkpoints/baseline/swin",
        "./checkpoints/baseline/image_only",
        "./checkpoints/baseline/gis_only",
        "./checkpoints/gcm",
        "./checkpoints/ablation",
        "./checkpoints/crossval",
    ], help="Checkpoint directories to scan")
    parser.add_argument("--output-dir", type=str, default="./outputs/tables", help="Output directory")
    args = parser.parse_args()

    results = collect_results(args.checkpoint_dirs, args.output_dir)
    print(f"Collected results for {len(results)} models:")
    for model_name, metrics in results.items():
        print(f"  {model_name}: val_loss={metrics['val_loss']:.4f}, val_mae={metrics['val_mae']:.4f}")


if __name__ == "__main__":
    main()
```

---

### `compare_models.py`

**Purpose:** Contains `load_results` function.

```python
import json
from pathlib import Path
from typing import Dict, List

import matplotlib.pyplot as plt
import numpy as np


def load_results(results_path: str = "./outputs/tables/results.json") -> Dict[str, Dict[str, float]]:
    path = Path(results_path)
    if not path.exists():
        raise FileNotFoundError(f"Results file not found: {path}")
    with open(path, "r") as f:
        return json.load(f)


def plot_metric_comparison(
    results: Dict[str, Dict[str, float]],
    metric: str,
    output_path: str,
    title: str,
    ylabel: str,
    figsize: tuple = (10, 6),
):
    models = []
    values = []
    for model_name, metrics in results.items():
        if metric in metrics and not np.isinf(metrics[metric]):
            models.append(model_name)
            values.append(metrics[metric])

    if not values:
        return

    fig, ax = plt.subplots(figsize=figsize)
    bars = ax.bar(models, values, color="steelblue")
    ax.set_title(title, fontsize=14, fontweight="bold")
    ax.set_ylabel(ylabel, fontsize=12)
    ax.set_xlabel("Model", fontsize=12)
    ax.tick_params(axis="x", rotation=45, labelsize=9)
    ax.grid(axis="y", alpha=0.3)

    for bar, val in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height(), f"{val:.4f}", ha="center", va="bottom", fontsize=8)

    plt.tight_layout()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=150, bbox_inches="tight")
    plt.close(fig)


def compare_models(results_path: str = "./outputs/tables/results.json", output_dir: str = "./outputs/comparison"):
    results = load_results(results_path)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    metrics_to_plot = [
        ("val_mae", "MAE Comparison", "Mean Absolute Error"),
        ("val_mse", "MSE Comparison", "Mean Squared Error"),
        ("val_rmse", "RMSE Comparison", "Root Mean Squared Error"),
        ("val_r2", "R² Comparison", "R² Score"),
    ]

    for metric, title, ylabel in metrics_to_plot:
        plot_metric_comparison(
            results,
            metric,
            str(output_path / f"{metric}_comparison.png"),
            title,
            ylabel,
        )

    summary_path = output_path / "comparison_summary.txt"
    with open(summary_path, "w") as f:
        f.write("Model Comparison Summary\n")
        f.write("=" * 80 + "\n\n")
        for model_name, metrics in results.items():
            f.write(f"Model: {model_name}\n")
            f.write(f"  Val Loss:  {metrics.get('val_loss', float('inf')):.4f}\n")
            f.write(f"  Val MAE:   {metrics.get('val_mae', float('inf')):.4f}\n")
            f.write(f"  Val MSE:   {metrics.get('val_mse', float('inf')):.4f}\n")
            f.write(f"  Val RMSE:  {metrics.get('val_rmse', float('inf')):.4f}\n")
            f.write(f"  Val R²:    {metrics.get('val_r2', float('-inf')):.4f}\n")
            f.write(f"  Best Epoch: {metrics.get('best_epoch', -1)}\n")
            f.write("\n")

    print(f"Comparison plots saved to {output_dir}")


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Compare model results and generate plots")
    parser.add_argument("--results", type=str, default="./outputs/tables/results.json", help="Path to results JSON")
    parser.add_argument("--output-dir", type=str, default="./outputs/comparison", help="Output directory for plots")
    args = parser.parse_args()

    compare_models(args.results, args.output_dir)


if __name__ == "__main__":
    main()
```

---

### `crossval.py`

**Purpose:** Contains `main` function.

```python
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
from models import GCMHAIRNet
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
            num_workers=config.get("dataset", {}).get("num_workers", 4),
            seed=seed,
            transforms_train=get_train_transforms(),
            transforms_val=get_val_transforms(),
        )

        model = GCMHAIRNet(config.get("model", {}))
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
```

---

### `generate_repo_md.py`

**Purpose:** Regenerate REPOSITORY_CODE.md from actual source files.

```python
#!/usr/bin/env python3
"""Regenerate REPOSITORY_CODE.md from actual source files."""

import os
from pathlib import Path

REPO_ROOT = Path(__file__).parent
MD_FILE = REPO_ROOT / "REPOSITORY_CODE.md"

EXCLUDE_DIRS = {
    ".git", "__pycache__", "venv", ".pytest_cache",
    "gcm_hairnet.egg-info", "node_modules",
}

def extract_purpose(content: str, filename: str) -> str:
    """Extract a purpose description from file content."""
    lines = content.split("\n")
    for line in lines:
        stripped = line.strip()
        if stripped.startswith("class "):
            class_name = stripped.split("(")[0].replace("class ", "").strip()
            return f"Defines `{class_name}` module/class."
        if stripped.startswith("def "):
            func_name = stripped.split("(")[0].replace("def ", "").strip()
            return f"Contains `{func_name}` function."
        if stripped.startswith('"""') or stripped.startswith("'''"):
            docstring = stripped.strip('"""').strip("'''").strip()
            if docstring:
                return docstring.split("\n")[0][:100]
    return f"Implementation of `{filename}`."

def generate_md() -> str:
    md_parts = []
    md_parts.append("# GCM-HAIRNet Repository Code\n")
    md_parts.append("Complete repository source code organized by module, with file descriptions and full implementations.\n")
    md_parts.append("---\n")

    py_files = sorted(REPO_ROOT.rglob("*.py"))

    for py_file in py_files:
        rel_path = py_file.relative_to(REPO_ROOT)
        parts = rel_path.parts

        if any(excl in parts for excl in EXCLUDE_DIRS):
            continue

        content = py_file.read_text(encoding="utf-8")
        purpose = extract_purpose(content, rel_path.name)

        md_parts.append(f"### `{rel_path}`\n")
        md_parts.append(f"**Purpose:** {purpose}\n")
        md_parts.append("```python")
        md_parts.append(content.rstrip())
        md_parts.append("```\n")
        md_parts.append("---\n")

    return "\n".join(md_parts)

if __name__ == "__main__":
    md_content = generate_md()
    MD_FILE.write_text(md_content, encoding="utf-8")
    print(f"Generated {MD_FILE} with content from {len(md_content.split('### `')) - 1} files.")
```

---

### `inference.py`

**Purpose:** Contains `main` function.

```python
import argparse
import sys
from pathlib import Path
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_val_transforms
from engine import Inferencer
from models import GCMHAIRNet
from utils.misc import get_device


def main():
    parser = argparse.ArgumentParser(description="Run inference with GCM-HAIRNet")
    parser.add_argument("--config", type=str, default="inference", help="Config name")
    parser.add_argument("--checkpoint", type=str, required=True, help="Checkpoint path")
    parser.add_argument("--root-dir", type=str, default="./data/processed", help="Dataset root")
    parser.add_argument("--split", type=str, default="test", help="Data split to use")
    parser.add_argument("--device", type=str, default=None, help="Device")
    parser.add_argument("--output-dir", type=str, default="./outputs/inference", help="Output directory")
    args = parser.parse_args()

    config_manager = ConfigManager(root_dir=str(Path(__file__).resolve().parent.parent))
    config = config_manager.load(args.config)
    device = get_device(args.device)

    dataset = GCMHAIRNetDataset(
        root_dir=args.root_dir,
        split=args.split,
        transforms=get_val_transforms(),
    )
    data_loader = build_dataloader(
        dataset,
        batch_size=config.get("inference", {}).get("batch_size", 32),
        shuffle=False,
        num_workers=4,
        drop_last=False,
    )

    model = GCMHAIRNet(config.get("model", {}))
    inferencer = Inferencer(
        model=model,
        data_loader=data_loader,
        checkpoint_path=args.checkpoint,
        device=device,
        output_dir=args.output_dir,
        save_predictions=config.get("inference", {}).get("save_predictions", True),
        save_visualizations=config.get("inference", {}).get("save_visualizations", True),
    )

    results = inferencer.run()
    print(f"Predictions saved to {args.output_dir}")
    print(f"Shape: {results['predictions'].shape}")


if __name__ == "__main__":
    main()
```

---

### `test.py`

**Purpose:** Contains `main` function.

```python
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
from models import GCMHAIRNet
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
        num_workers=config.get("dataset", {}).get("num_workers", 4),
        drop_last=False,
    )

    model = GCMHAIRNet(config.get("model", {}))
    checkpoint = torch.load(args.checkpoint, map_location=device)
    model.load_state_dict(checkpoint["model_state_dict"])
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
```

---

### `train.py`

**Purpose:** Contains `main` function.

```python
import argparse
import sys
from pathlib import Path
from typing import Optional

import torch
from torch.utils.data import DataLoader

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader, get_train_transforms, get_val_transforms
from engine import Trainer
from models import GCMHAIRNet
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
        from pathlib import Path
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
        num_workers=config.get("dataset", {}).get("num_workers", 4),
    )
    val_loader = build_dataloader(
        val_dataset,
        batch_size=config.get("dataset", {}).get("val_batch_size", 32),
        shuffle=False,
        num_workers=config.get("dataset", {}).get("num_workers", 4),
        drop_last=False,
    )

    model = GCMHAIRNet(config.get("model", {}))
    vis_dir = str(Path(args.output_dir) / "gcm_attention")
    trainer = Trainer(model, train_loader, val_loader, config, device, vis_dir=vis_dir)

    if args.checkpoint:
        trainer.resume(args.checkpoint)

    trainer.fit()


if __name__ == "__main__":
    main()
```

---

### `train_simple.py`

**Purpose:** Contains `main` function.

```python
import sys
import torch
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from configs import ConfigManager
from datasets import GCMHAIRNetDataset, build_dataloader
from models import GCMHAIRNet
from losses import build_loss
from utils.misc import get_device

def main():
    print("Starting training...")
    config_manager = ConfigManager()
    config = config_manager.load("train")
    device = get_device()
    print(f"Using device: {device}")
    
    print("Loading data...")
    dataset = GCMHAIRNetDataset(root_dir="./data/processed", split="train")
    loader = build_dataloader(dataset, batch_size=4, shuffle=True)
    val_dataset = GCMHAIRNetDataset(root_dir="./data/processed", split="val")
    val_loader = build_dataloader(val_dataset, batch_size=4, shuffle=False)
    
    print(f"Train: {len(dataset)} samples, Val: {len(val_dataset)} samples")
    
    print("Creating model...")
    model = GCMHAIRNet(config.get("model", {})).to(device)
    optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4)
    loss_fn = build_loss({"type": "mse"})
    
    print(f"Parameters: {sum(p.numel() for p in model.parameters()):,}")
    print("=" * 60)
    
    for epoch in range(100):
        model.train()
        train_loss = 0.0
        count = 0
        
        for batch in loader:
            img = batch["image"].to(device)
            gis = batch["gis"].to(device)
            label = batch["label"].to(device)
            
            optimizer.zero_grad()
            pred = model(img, gis)
            loss = loss_fn(pred, label)
            loss.backward()
            optimizer.step()
            
            train_loss += loss.item()
            count += 1
        
        model.eval()
        val_loss = 0.0
        vcount = 0
        
        with torch.no_grad():
            for batch in val_loader:
                img = batch["image"].to(device)
                gis = batch["gis"].to(device)
                label = batch["label"].to(device)
                pred = model(img, gis)
                 oss = loss_fn(                 oss = lo    val_loss += loss.item()
                vcount += 1
        
        train_loss /= count
        val_loss /= vcount
        val_loss print(f"Epoch {epoch+1:3d}/100: train_loss={train_loss:.4f}   al_loss={val_loss:.4f}")        val_los   if (epoch +        val_loss print(f"E checkpoint_dir =         val_loss print(f"Epoch {e                 val_loss print(f"Epoch {epoch+1:3d}/=T    
            torch.save({
                'epoch': epoch,
                'model_state_dict': model.state_dict(),
                'optimizer_state_dict': optimizer.state_dict(),
                'train_loss': train_loss,
                'val_loss': val_loss,
            }, checkpoint_dir / f"epoch_{epoch+1:04d}.pt")
            print(f"  Saved checkpoint at epoch {epoch+1}")

if __name__ == "__main__":
    main()
```

---

### `validate.py`

**Purpose:** Contains `main` function.

```python
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
from models import GCMHAIRNet
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
        num_workers=config.get("dataset", {}).get("num_workers", 4),
        drop_last=False,
    )

    model = GCMHAIRNet(config.get("model", {}))
    checkpoint = torch.load(args.checkpoint, map_location=device)
    model.load_state_dict(checkpoint["model_state_dict"])
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

    logger.close()


if __name__ == "__main__":
    main()
```

---
