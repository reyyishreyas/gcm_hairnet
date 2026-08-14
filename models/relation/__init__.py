from typing import Optional

import torch
import torch.nn as nn

from .vit import ViTRelationModule
from .swin import SwinRelationModule
from .graphsage import GraphSAGERelationModule
from .mha import MHARelationModule
from .non_local import NonLocalRelationModule


class RelationModule(nn.Module):
    def __init__(self, hidden_dim: int = 128, num_heads: int = 8, dropout: float = 0.1):
        super().__init__()
        self.hidden_dim = hidden_dim
        self.num_heads = num_heads
        self.dropout = dropout

    def forward(
        self,
        x: torch.Tensor,
        gis_features: Optional[torch.Tensor] = None,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> torch.Tensor:
        raise NotImplementedError

    def get_intermediate_features(self, x: torch.Tensor, gis_features=None, gis_embeddings=None) -> dict:
        return {"input": x, "output": self.forward(x, gis_features, gis_embeddings)}


def build_relation_module(config: dict) -> nn.Module:
    rel_type = config.get("type", "gcm")
    hidden_dim = config.get("hidden_dim", 128)
    num_heads = config.get("num_heads", 8)
    dropout = config.get("dropout", 0.1)

    if rel_type == "vit":
        return ViTRelationModule(hidden_dim, num_heads, dropout, num_layers=config.get("num_layers", 4))
    elif rel_type == "swin":
        return SwinRelationModule(hidden_dim, num_heads, dropout, num_layers=config.get("num_layers", 4))
    elif rel_type == "graphsage":
        return GraphSAGERelationModule(hidden_dim, dropout, num_layers=config.get("num_layers", 3))
    elif rel_type == "mha":
        return MHARelationModule(hidden_dim, num_heads, dropout, num_layers=config.get("num_layers", 4))
    elif rel_type == "nonlocal":
        return NonLocalRelationModule(hidden_dim, num_heads, dropout, num_layers=config.get("num_layers", 4))
    elif rel_type == "gcm":
        from ..gcm.gcm_block import GCMBlock
        gcm_config = dict(config)
        gcm_config.pop("type", None)
        gcm_config.pop("hidden_dim", None)
        gcm_config.pop("num_heads", None)
        gcm_config.setdefault("embed_dim", hidden_dim * 4 if hidden_dim > 128 else 512)
        gcm_config.setdefault("num_blocks", config.get("num_blocks", 4))
        gcm_config.setdefault("num_semantic_heads", 5)
        gcm_config.setdefault("mlp_ratio", 4.0)
        gcm_config.setdefault("dropout", dropout)
        gcm_config.setdefault("gate_init", 0.1)
        gcm_config.setdefault("gis_channels", 18)
        gcm_config.setdefault("gis_feature_dim", 64)
        gcm_config.setdefault("grid_size", 16)
        gcm_config.setdefault("sigma_distance", 1.0)
        gcm_config.setdefault("scene_weight_hidden", 32)
        gcm_config.setdefault("enable", True)
        gcm_config.setdefault("enable_distance", True)
        gcm_config.setdefault("enable_similarity", True)
        gcm_config.setdefault("enable_road", True)
        gcm_config.setdefault("enable_urban", True)
        gcm_config.setdefault("enable_learned", True)
        gcm_config.setdefault("enable_scene_weights", True)
        return GCMBlock(gcm_config)
    else:
        raise ValueError(f"Unknown relation module type: {rel_type}")


__all__ = [
    "RelationModule",
    "build_relation_module",
    "ViTRelationModule",
    "SwinRelationModule",
    "GraphSAGERelationModule",
    "MHARelationModule",
    "NonLocalRelationModule",
]
