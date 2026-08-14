from typing import Optional

import torch
import torch.nn as nn
import torch.nn.functional as F


class NonLocalRelationModule(nn.Module):
    def __init__(self, hidden_dim: int = 128, num_heads: int = 8, dropout: float = 0.1, num_layers: int = 4):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.head_dim = hidden_dim // num_heads
        assert hidden_dim % num_heads == 0

        self.layers = nn.ModuleList()
        for _ in range(num_layers):
            self.layers.append(NonLocalBlock(hidden_dim, num_heads, dropout))

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


class NonLocalBlock(nn.Module):
    def __init__(self, hidden_dim: int, num_heads: int = 8, dropout: float = 0.1):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.q_proj = nn.Linear(hidden_dim, hidden_dim)
        self.k_proj = nn.Linear(hidden_dim, hidden_dim)
        self.v_proj = nn.Linear(hidden_dim, hidden_dim)
        self.out_proj = nn.Linear(hidden_dim, hidden_dim)
        self.scale = nn.Parameter(torch.tensor(float(hidden_dim) ** -0.5))
        self.norm = nn.LayerNorm(hidden_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        B, N, C = x.shape
        residual = x
        x = self.norm(x)

        q = self.q_proj(x)
        k = self.k_proj(x)
        v = self.v_proj(x)

        attn = torch.matmul(q, k.transpose(-2, -1)) * self.scale
        attn = F.softmax(attn, dim=-1)
        attn = self.dropout(attn)

        out = torch.matmul(attn, v)
        out = self.out_proj(out)

        return residual + self.dropout(out)
