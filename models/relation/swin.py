from typing import Optional

import torch
import torch.nn as nn


class SwinTransformerLayer(nn.Module):
    def __init__(self, hidden_dim: int, num_heads: int, window_size: int = 8, mlp_ratio: float = 4.0, dropout: float = 0.1):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.window_size = window_size
        self.head_dim = hidden_dim // num_heads
        assert hidden_dim % num_heads == 0

        self.norm1 = nn.LayerNorm(hidden_dim)
        self.attn = nn.Linear(hidden_dim, hidden_dim)
        self.proj_drop = nn.Dropout(dropout)
        self.norm2 = nn.LayerNorm(hidden_dim)
        self.mlp = nn.Sequential(
            nn.Linear(hidden_dim, int(hidden_dim * mlp_ratio)),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(int(hidden_dim * mlp_ratio), hidden_dim),
            nn.Dropout(dropout),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, N, C = x.shape
        side = int(N ** 0.5)

        residual = x
        x = self.norm1(x)
        x = self.attn(x)
        x = self.proj_drop(x)
        x = residual + x

        residual = x
        x = self.norm2(x)
        x = self.mlp(x)
        x = residual + x
        return x


class SwinRelationModule(nn.Module):
    def __init__(self, hidden_dim: int = 128, num_heads: int = 8, dropout: float = 0.1, num_layers: int = 4):
        super().__init__()
        self.hidden_dim = hidden_dim
        layers = []
        for i in range(num_layers):
            layers.append(SwinTransformerLayer(
                hidden_dim=hidden_dim,
                num_heads=min(num_heads, hidden_dim // (2 ** i)),
                window_size=8,
                mlp_ratio=4.0,
                dropout=dropout,
            ))
        self.layers = nn.Sequential(*layers)
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
        for layer in self.layers:
            x = layer(x)
        x = self.norm(x)
        return self.proj(x) + x
