from typing import Dict, Optional, Tuple

import torch
import torch.nn as nn

from .gcm_transformer import GCMTransformer


class GCMBlock(nn.Module):
    def __init__(self, config: Dict):
        super().__init__()
        self.gcm_transformer = GCMTransformer(
            embed_dim=config.get("embed_dim", 512),
            num_heads=config.get("num_heads", 8),
            num_blocks=config.get("num_blocks", 4),
            num_semantic_heads=config.get("num_semantic_heads", 5),
            mlp_ratio=config.get("mlp_ratio", 4.0),
            dropout=config.get("dropout", 0.1),
            gate_init=config.get("gate_init", 0.1),
            gis_channels=config.get("gis_channels", 18),
            gis_feature_dim=config.get("gis_feature_dim", 64),
            grid_size=config.get("grid_size", 16),
            sigma_distance=config.get("sigma_distance", 1.0),
            scene_weight_hidden=config.get("scene_weight_hidden", 32),
            enable_distance=config.get("enable_distance", True),
            enable_similarity=config.get("enable_similarity", True),
            enable_road=config.get("enable_road", True),
            enable_urban=config.get("enable_urban", True),
            enable_learned=config.get("enable_learned", True),
            enable_scene_weights=config.get("enable_scene_weights", True),
        )

    def forward(
        self,
        x: torch.Tensor,
        gis_features: torch.Tensor,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> Tuple[torch.Tensor, list]:
        return self.gcm_transformer(x, gis_features, gis_embeddings)
