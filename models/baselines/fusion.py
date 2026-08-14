from typing import Dict

import torch
import torch.nn as nn


class ConcatFusion(nn.Module):
    def __init__(self, image_dim: int = 128, gis_dim: int = 64, output_dim: int = 128, dropout: float = 0.1):
        super().__init__()
        self.proj = nn.Sequential(
            nn.Linear(image_dim + gis_dim, output_dim),
            nn.LayerNorm(output_dim),
            nn.Dropout(dropout),
        )

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        if gis_feats.shape[1] != image_feats.shape[1]:
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(gis_feats.shape[0], gis_feats.shape[2], int(gis_feats.shape[1] ** 0.5), int(gis_feats.shape[1] ** 0.5)),
                size=(int(image_feats.shape[1] ** 0.5), int(image_feats.shape[1] ** 0.5)),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)
        concat = torch.cat([image_feats, gis_feats], dim=-1)
        return self.proj(concat)


class AdditionFusion(nn.Module):
    def __init__(self, image_dim: int = 128, gis_dim: int = 64, output_dim: int = 128, dropout: float = 0.1):
        super().__init__()
        self.image_proj = nn.Linear(image_dim, output_dim)
        self.gis_proj = nn.Linear(gis_dim, output_dim)
        self.norm = nn.LayerNorm(output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        if gis_feats.shape[1] != image_feats.shape[1]:
            B, N, C = gis_feats.shape
            side = int(N ** 0.5)
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(B, C, side, side),
                size=(int(image_feats.shape[1] ** 0.5), int(image_feats.shape[1] ** 0.5)),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)
        img = self.image_proj(image_feats)
        gis = self.gis_proj(gis_feats)
        fused = img + gis
        return self.norm(fused)


class GatedFusion(nn.Module):
    def __init__(self, image_dim: int = 128, gis_dim: int = 64, output_dim: int = 128, dropout: float = 0.1):
        super().__init__()
        self.gate = nn.Sequential(
            nn.Linear(image_dim + gis_dim, output_dim),
            nn.Sigmoid(),
        )
        self.image_proj = nn.Linear(image_dim, output_dim)
        self.gis_proj = nn.Linear(gis_dim, output_dim)
        self.norm = nn.LayerNorm(output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        if gis_feats.shape[1] != image_feats.shape[1]:
            B, N, C = gis_feats.shape
            side = int(N ** 0.5)
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(B, C, side, side),
                size=(int(image_feats.shape[1] ** 0.5), int(image_feats.shape[1] ** 0.5)),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)
        concat = torch.cat([image_feats, gis_feats], dim=-1)
        g = self.gate(concat)
        img = self.image_proj(image_feats)
        gis = self.gis_proj(gis_feats)
        fused = g * img + (1 - g) * gis
        return self.norm(fused)


class CrossAttentionFusion(nn.Module):
    def __init__(self, image_dim: int = 128, gis_dim: int = 64, output_dim: int = 128, dropout: float = 0.1):
        super().__init__()
        self.q_proj = nn.Linear(image_dim, output_dim)
        self.k_proj = nn.Linear(gis_dim, output_dim)
        self.v_proj = nn.Linear(gis_dim, output_dim)
        self.out_proj = nn.Linear(output_dim, output_dim)
        self.norm = nn.LayerNorm(output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        if gis_feats.shape[1] != image_feats.shape[1]:
            B, N, C = gis_feats.shape
            side = int(N ** 0.5)
            target_side = int(image_feats.shape[1] ** 0.5)
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(B, C, side, side),
                size=(target_side, target_side),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)
        q = self.q_proj(image_feats)
        k = self.k_proj(gis_feats)
        v = self.v_proj(gis_feats)
        attn = torch.matmul(q, k.transpose(-2, -1)) / (self.q_proj.out_features ** 0.5)
        attn = torch.softmax(attn, dim=-1)
        attn = self.dropout(attn)
        out = torch.matmul(attn, v)
        out = self.out_proj(out)
        return self.norm(out + image_feats)


class MultiHeadCrossAttentionFusion(nn.Module):
    def __init__(self, image_dim: int = 128, gis_dim: int = 64, output_dim: int = 128, num_heads: int = 8, dropout: float = 0.1):
        super().__init__()
        assert output_dim % num_heads == 0
        self.num_heads = num_heads
        self.head_dim = output_dim // num_heads
        self.q_proj = nn.Linear(image_dim, output_dim)
        self.k_proj = nn.Linear(gis_dim, output_dim)
        self.v_proj = nn.Linear(gis_dim, output_dim)
        self.out_proj = nn.Linear(output_dim, output_dim)
        self.norm = nn.LayerNorm(output_dim)
        self.dropout = nn.Dropout(dropout)

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        if gis_feats.shape[1] != image_feats.shape[1]:
            B, N, C = gis_feats.shape
            side = int(N ** 0.5)
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(B, C, side, side),
                size=(int(image_feats.shape[1] ** 0.5), int(image_feats.shape[1] ** 0.5)),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)
        B, N, _ = image_feats.shape
        q = self.q_proj(image_feats).reshape(B, N, self.num_heads, self.head_dim).transpose(1, 2)
        k = self.k_proj(gis_feats).reshape(B, -1, self.num_heads, self.head_dim).transpose(1, 2)
        v = self.v_proj(gis_feats).reshape(B, -1, self.num_heads, self.head_dim).transpose(1, 2)
        attn = torch.matmul(q, k.transpose(-2, -1)) / (self.head_dim ** 0.5)
        attn = torch.softmax(attn, dim=-1)
        attn = self.dropout(attn)
        out = torch.matmul(attn, v)
        out = out.transpose(1, 2).reshape(B, N, -1)
        out = self.out_proj(out)
        return self.norm(out + image_feats)


class BilinearFusion(nn.Module):
    def __init__(self, image_dim: int = 128, gis_dim: int = 64, output_dim: int = 128, rank: int = 32, dropout: float = 0.1):
        super().__init__()
        self.image_proj = nn.Linear(image_dim, rank)
        self.gis_proj = nn.Linear(gis_dim, rank)
        self.out_proj = nn.Sequential(
            nn.Linear(rank, output_dim),
            nn.LayerNorm(output_dim),
            nn.Dropout(dropout),
        )
        self.norm = nn.LayerNorm(output_dim)

    def forward(self, image_feats: torch.Tensor, gis_feats: torch.Tensor) -> torch.Tensor:
        if gis_feats.shape[1] != image_feats.shape[1]:
            B, N, C = gis_feats.shape
            side = int(N ** 0.5)
            gis_feats = nn.functional.interpolate(
                gis_feats.transpose(1, 2).reshape(B, C, side, side),
                size=(int(image_feats.shape[1] ** 0.5), int(image_feats.shape[1] ** 0.5)),
                mode="bilinear",
                align_corners=False,
            ).flatten(2).transpose(1, 2)
        img = self.image_proj(image_feats)
        gis = self.gis_proj(gis_feats)
        bilinear = img * gis
        out = self.out_proj(bilinear)
        return self.norm(out + image_feats)
