from typing import Optional

import torch
import torch.nn as nn
from timm.models.vision_transformer import Block


class ViTRelationModule(nn.Module):
    def __init__(self, hidden_dim: int = 128, num_heads: int = 8, dropout: float = 0.1, num_layers: int = 4):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.blocks = nn.ModuleList([
            Block(
                dim=hidden_dim,
                num_heads=num_heads,
                mlp_ratio=4.0,
                qkv_bias=True,
                proj_drop=dropout,
                attn_drop=dropout,
                drop_path=dropout,
                act_layer=nn.GELU,
                norm_layer=nn.LayerNorm,
            )
            for _ in range(num_layers)
        ])
        self.norm = nn.LayerNorm(hidden_dim)
        self.proj = nn.Sequential(
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
        )

    def forward(
        self,
        x: torch.Tensor,
        gis_features: Optional[torch.Tensor] = None,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        for block in self.blocks:
            x = block(x)
        x = self.norm(x)
        return self.proj(x) + x
