from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np


def plot_training_curves(
    metrics: Dict[str, List[float]],
    save_path: Optional[str] = None,
    title: str = "Training Curves",
):
    try:
        import matplotlib.pyplot as plt

        fig, ax = plt.subplots(figsize=(10, 6))
        for name, values in metrics.items():
            ax.plot(values, label=name)
        ax.set_xlabel("Step/Epoch")
        ax.set_ylabel("Value")
        ax.set_title(title)
        ax.legend()
        ax.grid(True)

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass


def save_training_summary(
    metrics: Dict[str, List[float]],
    output_dir: str,
    experiment_name: str = "experiment",
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    plot_training_curves(
        metrics,
        save_path=str(output_path / f"{experiment_name}_curves.png"),
        title=experiment_name,
    )
