from pathlib import Path
from typing import Any, Dict, List, Optional

import numpy as np
import torch


def save_gcm_priors(
    priors: Dict[str, torch.Tensor],
    output_dir: str,
    epoch: int = 0,
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not _matplotlib_available():
        return

    try:
        import matplotlib.pyplot as plt

        for name, prior in priors.items():
            if prior is None:
                continue
            prior_np = prior.detach().cpu().numpy()
            if prior_np.ndim == 3:
                prior_np = prior_np[0]
            fig, ax = plt.subplots(figsize=(8, 6))
            im = ax.imshow(prior_np, cmap="viridis")
            ax.set_title(f"{name} Prior (epoch {epoch})")
            plt.colorbar(im, ax=ax)
            fig.savefig(output_path / f"epoch_{epoch:04d}_{name}_prior.png")
            plt.close(fig)
    except ImportError:
        pass


def save_attention_maps(
    attention_maps: List[Dict[str, torch.Tensor]],
    output_dir: str,
    epoch: int = 0,
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not _matplotlib_available():
        return

    try:
        import matplotlib.pyplot as plt

        for block_idx, block_maps in enumerate(attention_maps):
            for head_name, attn in block_maps.items():
                attn_np = attn.detach().cpu().numpy()
                if attn_np.ndim == 3:
                    attn_np = attn_np[0]
                fig, ax = plt.subplots(figsize=(8, 6))
                im = ax.imshow(attn_np, cmap="hot")
                ax.set_title(f"Block {block_idx} {head_name} (epoch {epoch})")
                plt.colorbar(im, ax=ax)
                fig.savefig(output_path / f"epoch_{epoch:04d}_block_{block_idx}_{head_name}.png")
                plt.close(fig)
    except ImportError:
        pass


def save_scene_weights(
    scene_weights: torch.Tensor,
    output_dir: str,
    epoch: int = 0,
) -> None:
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    if not _matplotlib_available():
        return

    try:
        import matplotlib.pyplot as plt

        weights_np = scene_weights.detach().cpu().numpy()
        labels = ["Distance", "Similarity", "Road", "Urban", "Learned"]

        fig, ax = plt.subplots(figsize=(10, 6))
        for i in range(min(5, weights_np.shape[-1])):
            ax.plot(weights_np[:, i], label=labels[i])
        ax.set_xlabel("Sample")
        ax.set_ylabel("Weight")
        ax.set_title(f"Scene Weights (epoch {epoch})")
        ax.legend()
        ax.grid(True)
        fig.savefig(output_path / f"epoch_{epoch:04d}_scene_weights.png")
        plt.close(fig)
    except ImportError:
        pass


def _matplotlib_available() -> bool:
    try:
        import matplotlib  # noqa: F401
        return True
    except ImportError:
        return False
