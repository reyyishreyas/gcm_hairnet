from typing import Dict, List, Optional, Tuple

import torch
import torch.nn as nn


class GCMTransformerBlock(nn.Module):
    def __init__(
        self,
        embed_dim: int = 512,
        num_heads: int = 8,
        num_semantic_heads: int = 5,
        mlp_ratio: float = 4.0,
        dropout: float = 0.1,
        gate_init: float = 0.1,
        enable_scene_weights: bool = True,
    ):
        super().__init__()
        self.norm1 = nn.LayerNorm(embed_dim)
        from models.gcm.geographic_attention import SemanticGeographicAttention
        self.attn = SemanticGeographicAttention(
            embed_dim=embed_dim,
            num_heads=num_heads,
            num_semantic_heads=num_semantic_heads,
            dropout=dropout,
            gate_init=gate_init,
            enable_scene_weights=enable_scene_weights,
        )
        self.norm2 = nn.LayerNorm(embed_dim)
        self.mlp = nn.Sequential(
            nn.Linear(embed_dim, int(embed_dim * mlp_ratio)),
            nn.GELU(),
            nn.Dropout(dropout),
            nn.Linear(int(embed_dim * mlp_ratio), embed_dim),
            nn.Dropout(dropout),
        )

    def forward(
        self,
        x: torch.Tensor,
        grg: torch.Tensor,
        priors: Optional[Dict[str, torch.Tensor]] = None,
    ) -> Tuple[torch.Tensor, Dict[str, torch.Tensor]]:
        attn_out, attn_maps = self.attn(self.norm1(x), grg, priors)
        x = x + attn_out
        x = x + self.mlp(self.norm2(x))
        return x, attn_maps


class GCMTransformer(nn.Module):
    def __init__(
        self,
        embed_dim: int = 512,
        num_heads: int = 8,
        num_blocks: int = 4,
        num_semantic_heads: int = 5,
        mlp_ratio: float = 4.0,
        dropout: float = 0.1,
        gate_init: float = 0.1,
        gis_channels: int = 18,
        gis_feature_dim: int = 64,
        grid_size: int = 16,
        sigma_distance: float = 1.0,
        scene_weight_hidden: int = 32,
        enable_distance: bool = True,
        enable_similarity: bool = True,
        enable_road: bool = True,
        enable_urban: bool = True,
        enable_learned: bool = True,
        enable_scene_weights: bool = True,
    ):
        super().__init__()
        self.num_blocks = num_blocks
        self.grid_size = grid_size
        self.num_tokens = grid_size * grid_size

        from models.gcm.grm import GeographicRelationMatrix
        self.grm = GeographicRelationMatrix(
            embed_dim=embed_dim,
            gis_channels=gis_channels,
            gis_feature_dim=gis_feature_dim,
            grid_size=grid_size,
            sigma_distance=sigma_distance,
            scene_weight_hidden=scene_weight_hidden,
            enable_distance=enable_distance,
            enable_similarity=enable_similarity,
            enable_road=enable_road,
            enable_urban=enable_urban,
            enable_learned=enable_learned,
            enable_scene_weights=enable_scene_weights,
        )

        self.blocks = nn.ModuleList([
            GCMTransformerBlock(
                embed_dim=embed_dim,
                num_heads=num_heads,
                num_semantic_heads=num_semantic_heads,
                mlp_ratio=mlp_ratio,
                dropout=dropout,
                gate_init=gate_init,
                enable_scene_weights=enable_scene_weights,
            )
            for _ in range(num_blocks)
        ])

        self.norm = nn.LayerNorm(embed_dim)

    def forward(
        self,
        x: torch.Tensor,
        gis_features: torch.Tensor,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> Tuple[torch.Tensor, List[Dict[str, torch.Tensor]]]:
        B, N, C = x.shape
        grg, priors = self.grm(x, gis_features, gis_embeddings)

        all_attn_maps = []
        for block in self.blocks:
            x, attn_maps = block(x, grg, priors)
            all_attn_maps.append(attn_maps)

        x = self.norm(x)
        return x, all_attn_maps
