from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel
from ..encoders.swin import SwinTransformerEncoder
from ..encoders.gis_encoder import GISEncoder
from ..graph_relation import GraphRelationModule
from ..decoder.risk_decoder import Decoder
from .fusion import (
    ConcatFusion,
    AdditionFusion,
    GatedFusion,
    CrossAttentionFusion,
    MultiHeadCrossAttentionFusion,
    BilinearFusion,
)


class BaselineModel(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.image_encoder = SwinTransformerEncoder(config.get("image_encoder", {}))
        self.gis_encoder = GISEncoder(config.get("gis_encoder", {}))
        self.hidden_dim = config.get("decoder", {}).get("hidden_dim", 128)

        fusion_config = config.get("fusion", {})
        fusion_type = fusion_config.get("type", "concat")
        dropout = fusion_config.get("dropout", 0.1)

        if fusion_type == "concat":
            self.fusion = ConcatFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                dropout=dropout,
            )
        elif fusion_type == "addition":
            self.fusion = AdditionFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                dropout=dropout,
            )
        elif fusion_type == "gated":
            self.fusion = GatedFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                dropout=dropout,
            )
        elif fusion_type == "cross_attention":
            self.fusion = CrossAttentionFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                dropout=dropout,
            )
        elif fusion_type == "multihead_cross_attention":
            self.fusion = MultiHeadCrossAttentionFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                num_heads=fusion_config.get("num_heads", 8),
                dropout=dropout,
            )
        elif fusion_type == "bilinear":
            self.fusion = BilinearFusion(
                image_dim=self.image_encoder.embed_dim,
                gis_dim=self.gis_encoder.output_dim,
                output_dim=self.hidden_dim,
                rank=fusion_config.get("rank", 32),
                dropout=dropout,
            )
        else:
            raise ValueError(f"Unknown fusion type: {fusion_type}")

        self.grm = GraphRelationModule(config.get("grm", {}))
        self.decoder = Decoder(config.get("decoder", {}))

    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        image_feats = self.image_encoder(image)
        gis_feats = self.gis_encoder(gis)
        fused = self.fusion(image_feats, gis_feats)

        B, N, C = fused.shape
        H = W = int(N ** 0.5)
        spatial_feats = fused.transpose(1, 2).reshape(B, C, H, W)

        tokens = spatial_feats.flatten(2).transpose(1, 2)
        refined_tokens = self.grm(tokens)
        spatial_feats = refined_tokens.transpose(1, 2).reshape(B, C, H, W)

        output = self.decoder(spatial_feats, spatial_size=(256, 256))
        return output

    def get_intermediate_features(self, image: torch.Tensor, gis: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {}
        features["image_encoder"] = self.image_encoder.get_intermediate_features(image)
        features["gis_encoder"] = self.gis_encoder.get_intermediate_features(gis)
        image_feats = features["image_encoder"]["final"]
        gis_feats = features["gis_encoder"]["final"]
        features["fusion"] = self.fusion(image_feats, gis_feats)
        features["fusion_input"] = {"image": image_feats, "gis": gis_feats}

        B, N, C = features["fusion"].shape
        H = W = int(N ** 0.5)
        spatial_feats = features["fusion"].transpose(1, 2).reshape(B, C, H, W)
        features["graph_relation_input"] = spatial_feats.flatten(2).transpose(1, 2)
        refined_tokens = self.grm(features["graph_relation_input"])
        features["graph_relation_output"] = refined_tokens
        spatial_feats = refined_tokens.transpose(1, 2).reshape(B, C, H, W)
        features["decoder_input"] = spatial_feats
        features["decoder"] = self.decoder.get_intermediate_features(spatial_feats, (256, 256))
        return features
