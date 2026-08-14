from typing import Dict, Optional, Tuple

import torch
import torch.nn as nn
import torch.nn.functional as F


class SemanticGeographicAttention(nn.Module):
    def __init__(
        self,
        embed_dim: int = 512,
        num_heads: int = 8,
        num_semantic_heads: int = 5,
        dropout: float = 0.1,
        gate_init: float = 0.1,
        enable_scene_weights: bool = True,
        prior_scale: float = 4.0,
    ):
        super().__init__()
        self.embed_dim = embed_dim
        self.num_heads = num_heads
        self.num_semantic_heads = num_semantic_heads
        self.head_dim = embed_dim // num_heads
        self.enable_scene_weights = enable_scene_weights
        assert embed_dim % num_heads == 0

        self.q_proj = nn.Linear(embed_dim, embed_dim)
        self.k_proj = nn.Linear(embed_dim, embed_dim)
        self.v_proj = nn.Linear(embed_dim, embed_dim)
        self.out_proj = nn.Linear(embed_dim, embed_dim)
        self.dropout = nn.Dropout(dropout)
        self.beta_gate = nn.Parameter(torch.tensor(gate_init))

        self.prior_scale = nn.Parameter(torch.tensor(prior_scale))

        self.semantic_projections = nn.ModuleList([
            nn.Linear(embed_dim, embed_dim) for _ in range(num_semantic_heads)
        ])
        self.semantic_grg_projections = nn.ModuleList([
            nn.Linear(embed_dim, embed_dim) for _ in range(num_semantic_heads)
        ])

    def _apply_semantic_attention(
        self,
        Q: torch.Tensor,
        K: torch.Tensor,
        V: torch.Tensor,
        G: torch.Tensor,
    ) -> torch.Tensor:
        B, H, N, D = Q.shape
        attn_scores = torch.bmm(Q, K.transpose(1, 2)) / (self.head_dim ** 0.5)
        attn_scores = attn_scores + G
        attn_weights = F.softmax(attn_scores, dim=-1)
        attn_weights = self.dropout(attn_weights)
        attn_output = torch.bmm(attn_weights, V)
        return attn_output

    def forward(
        self,
        x: torch.Tensor,
        grg: torch.Tensor,
        priors: Optional[Dict[str, torch.Tensor]] = None,
    ) -> Tuple[torch.Tensor, Dict[str, torch.Tensor]]:
        B, N, C = x.shape
        H = self.num_heads
        D = self.head_dim

        Q = self.q_proj(x).view(B, N, H, D).transpose(1, 2)
        K = self.k_proj(x).view(B, N, H, D).transpose(1, 2)
        V = self.v_proj(x).view(B, N, H, D).transpose(1, 2)

        attention_maps = {}
        outputs = []
        prior_names = ["distance", "similarity", "road", "urban", "learned"]

        scaled_grg = grg * self.prior_scale

        for head_idx in range(H):
            q_h = Q[:, head_idx, :, :]
            k_h = K[:, head_idx, :, :]
            v_h = V[:, head_idx, :, :]

            if head_idx < self.num_semantic_heads:
                prior_name = prior_names[head_idx]
                G = priors.get(prior_name, torch.zeros(B, N, N, device=x.device)) if priors else torch.zeros(B, N, N, device=x.device)
                G = G * self.prior_scale
            else:
                G = scaled_grg

            attn_scores = torch.bmm(q_h, k_h.transpose(1, 2)) / (D ** 0.5)
            attn_scores = attn_scores + G
            attn_weights = F.softmax(attn_scores, dim=-1)
            attn_weights = attn_weights * (1.0 + self.beta_gate * G)
            attn_weights = self.dropout(attn_weights)
            attn_output = torch.bmm(attn_weights, v_h)

            outputs.append(attn_output)

            if head_idx < self.num_semantic_heads:
                attention_maps[f"head_{head_idx}_{prior_name}"] = G.detach()

        attn_output = torch.cat(outputs, dim=-1)
        attn_output = attn_output.view(B, N, C)
        attn_output = self.out_proj(attn_output)
        return attn_output, attention_maps
