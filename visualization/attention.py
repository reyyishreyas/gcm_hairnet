from typing import Any, Dict, List, Optional

import numpy as np
import torch


def plot_attention_map(
    attention_weights: torch.Tensor,
    save_path: Optional[str] = None,
    title: str = "Attention Map",
    cmap: str = "viridis",
):
    try:
        import matplotlib.pyplot as plt

        attn = attention_weights.detach().cpu().numpy().squeeze()
        fig, ax = plt.subplots(figsize=(10, 8))
        im = ax.imshow(attn, cmap=cmap)
        ax.set_title(title)
        plt.colorbar(im, ax=ax)

        if save_path:
            fig.savefig(save_path)
        plt.close(fig)
    except ImportError:
        pass


def save_attention_maps(
    attention_weights: np.ndarray,
    layer_names: List[str],
    output_dir: str,
) -> None:
    from pathlib import Path
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    try:
        import matplotlib.pyplot as plt

        for i, attn in enumerate(attention_weights):
            layer = layer_names[i] if i < len(layer_names) else f"layer_{i}"
            fig, ax = plt.subplots(figsize=(10, 8))
            im = ax.imshow(attn.squeeze(), cmap="viridis")
            ax.set_title(f"Attention: {layer}")
            plt.colorbar(im, ax=ax)
            fig.savefig(output_path / f"{layer}_attention.png")
            plt.close(fig)
    except ImportError:
        pass
