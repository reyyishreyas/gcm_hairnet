from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel


class GatedCrossAttention(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.hidden_dim = config.get("hidden_dim", 128)
        self.gis_input_dim = config.get("gis_input_dim", self.hidden_dim)
        self.num_heads = config.get("num_heads", 8)
        self.dropout_rate = config.get("dropout", 0.1)
        self.max_tokens = config.get("max_tokens", 256)
        self.rel_pos_scale = config.get("rel_pos_scale", 0.0)
        self._build_module()

    def _build_module(self):
        assert self.hidden_dim % self.num_heads == 0, (
            f"hidden_dim ({self.hidden_dim}) must be divisible by num_heads ({self.num_heads})"
        )
        self.head_dim = self.hidden_dim // self.num_heads
        self.q_proj = nn.Linear(self.hidden_dim, self.hidden_dim)
        self.k_proj = nn.Linear(self.gis_input_dim, self.hidden_dim)
        self.v_proj = nn.Linear(self.gis_input_dim, self.hidden_dim)
        self.out_proj = nn.Linear(self.hidden_dim, self.hidden_dim)
        self.norm = nn.LayerNorm(self.hidden_dim)
        self.dropout = nn.Dropout(self.dropout_rate)
        self.gate = nn.Sequential(
            nn.Linear(self.hidden_dim * 2, self.hidden_dim),
            nn.Tanh(),
            nn.Linear(self.hidden_dim, self.hidden_dim),
            nn.Sigmoid(),
        )
        for p in self.parameters():
            if p.dim() > 1:
                nn.init.xavier_uniform_(p)

        coords = self._generate_2d_coords(self.max_tokens)
        spatial_dist = torch.cdist(coords, coords, p=2)
        init_bias = -spatial_dist * self.rel_pos_scale
        self.register_buffer("rel_pos_bias", init_bias)

    @staticmethod
    def _generate_2d_coords(num_tokens: int) -> torch.Tensor:
        side = int(num_tokens ** 0.5)
        if side * side != num_tokens:
            side = 16
        x = torch.arange(side, dtype=torch.float32)
        y = torch.arange(side, dtype=torch.float32)
        xx, yy = torch.meshgrid(x, y, indexing="ij")
        coords = torch.stack([xx.flatten(), yy.flatten()], dim=-1)
        return coords

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        B, N, C = image_feats.shape

        if gis_feats.shape[1] != N:
            B2, N2, C2 = gis_feats.shape
            side = int(N2 ** 0.5)
            target_side = int(N ** 0.5)
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(B2, C2, side, side),
                size=(target_side, target_side),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)

        q = self.q_proj(image_feats).view(B, N, self.num_heads, self.head_dim).transpose(1, 2)
        k = self.k_proj(gis_feats).view(B, N, self.num_heads, self.head_dim).transpose(1, 2)
        v = self.v_proj(gis_feats).view(B, N, self.num_heads, self.head_dim).transpose(1, 2)

        attn = torch.matmul(q, k.transpose(-2, -1)) / (self.head_dim ** 0.5)
        if N <= self.max_tokens:
            bias = self.rel_pos_bias[:N, :N].unsqueeze(0)
            attn = attn + bias
        attn = torch.softmax(attn, dim=-1)
        attn = self.dropout(attn)

        out = torch.matmul(attn, v)
        out = out.transpose(1, 2).contiguous().view(B, N, C)
        concat = torch.cat([image_feats, out], dim=-1)
        gating = self.gate(concat)
        fused = image_feats * gating + out * (1 - gating)
        fused = self.out_proj(fused)
        fused = self.norm(fused + image_feats)
        return fused

    def get_intermediate_features(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {"gct_input": image_feats, "gis_input": gis_feats}
        features["gct_output"] = self.forward(image_feats, gis_feats)
        return features
