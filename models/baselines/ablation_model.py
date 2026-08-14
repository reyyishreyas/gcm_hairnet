from typing import Dict

import torch
import torch.nn as nn

from ..base import BaseModel
from ..encoders.swin import SwinTransformerEncoder
from ..encoders.gis_encoder import GISEncoder
from ..fusion.gct import GatedCrossAttention
from .fusion import (
    ConcatFusion,
    AdditionFusion,
    GatedFusion,
    CrossAttentionFusion,
    MultiHeadCrossAttentionFusion,
    BilinearFusion,
)
from ..graph_relation import GraphRelationModule
from ..decoder.risk_decoder import Decoder


class AblationModel(BaseModel):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.image_encoder = SwinTransformerEncoder(config.get("image_encoder", {}))
        self.gis_encoder = GISEncoder(config.get("gis_encoder", {}))
        self.hidden_dim = config.get("decoder", {}).get("hidden_dim", 128)

        gct_config = dict(config.get("gct", {}))
        gct_config.setdefault("gis_input_dim", self.gis_encoder.output_dim)
        self.use_gct = config.get("gct", {}).get("enable", True)
        self.fusion_type = config.get("gct", {}).get("type", "gated_cross_attention")

        if self.use_gct and self.fusion_type == "gated_cross_attention":
            self.fusion = GatedCrossAttention(gct_config)
        else:
            self.fusion = None
            self.simple_fusion = self._build_simple_fusion(config.get("fusion", {}))

        gcm_config = config.get("gcm", {})
        self.use_gcm = gcm_config.get("enable", True)
        if self.use_gcm:
            from models.gcm.gcm_block import GCMBlock
            self.gcm = GCMBlock(gcm_config)
            self.gcm_proj = nn.Conv2d(
                self.image_encoder.embed_dim + self.gis_encoder.input_channels,
                gcm_config.get("embed_dim", 512),
                kernel_size=1,
            )
            self.decoder_proj = nn.Conv2d(
                gcm_config.get("embed_dim", 512),
                self.hidden_dim,
                kernel_size=1,
            )

        self.grm = GraphRelationModule(config.get("grm", {}))
        self.decoder = Decoder(config.get("decoder", {}))

    def _build_simple_fusion(self, fusion_config: Dict):
        fusion_type = fusion_config.get("type", "concat")
        dropout = fusion_config.get("dropout", 0.1)
        img_dim = self.image_encoder.embed_dim
        gis_dim = self.gis_encoder.output_dim

        if fusion_type == "concat":
            return ConcatFusion(img_dim, gis_dim, self.hidden_dim, dropout)
        elif fusion_type == "addition":
            return AdditionFusion(img_dim, gis_dim, self.hidden_dim, dropout)
        elif fusion_type == "gated":
            return GatedFusion(img_dim, gis_dim, self.hidden_dim, dropout)
        elif fusion_type == "cross_attention":
            return CrossAttentionFusion(img_dim, gis_dim, self.hidden_dim, dropout)
        elif fusion_type == "multihead_cross_attention":
            return MultiHeadCrossAttentionFusion(img_dim, gis_dim, self.hidden_dim, fusion_config.get("num_heads", 8), dropout)
        elif fusion_type == "bilinear":
            return BilinearFusion(img_dim, gis_dim, self.hidden_dim, fusion_config.get("rank", 32), dropout)
        else:
            return ConcatFusion(img_dim, gis_dim, self.hidden_dim, dropout)

    def forward(self, image: torch.Tensor, gis: torch.Tensor) -> torch.Tensor:
        image_feats = self.image_encoder(image)
        gis_feats = self.gis_encoder(gis)

        if self.fusion is not None:
            fused_feats = self.fusion(image_feats, gis_feats)
        else:
            fused_feats = self.simple_fusion(image_feats, gis_feats)

        B, N, C = fused_feats.shape
        H = W = int(N ** 0.5)
        spatial_feats = fused_feats.transpose(1, 2).reshape(B, C, H, W)

        if self.use_gcm:
            upsampled_gis = nn.functional.interpolate(gis, size=(H, W), mode="bilinear", align_corners=False)
            concat_feats = torch.cat([spatial_feats, upsampled_gis], dim=1)
            projected = self.gcm_proj(concat_feats)
            projected = nn.functional.layer_norm(projected, projected.shape[1:])
            B, C, H, W = projected.shape
            tokens = projected.flatten(2).transpose(1, 2)
            gis_for_priors = nn.functional.interpolate(gis, size=(H, W), mode="bilinear", align_corners=False)
            gis_embeddings = None
            if hasattr(self.gis_encoder, "encoder"):
                with torch.no_grad():
                    gis_embeddings = self.gis_encoder(gis_for_priors)
            tokens, _ = self.gcm(tokens, gis_for_priors, gis_embeddings)
            spatial_feats = tokens.transpose(1, 2).reshape(B, C, H, W)
            spatial_feats = self.decoder_proj(spatial_feats)

        B, C, H, W = spatial_feats.shape
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

        if self.fusion is not None:
            features["gct"] = self.fusion.get_intermediate_features(image_feats, gis_feats) if hasattr(self.fusion, "get_intermediate_features") else {"gct_output": self.fusion(image_feats, gis_feats)}
            fused_feats = features["gct"]["gct_output"] if "gct_output" in features["gct"] else self.fusion(image_feats, gis_feats)
        else:
            features["fusion"] = {"fusion_output": self.simple_fusion(image_feats, gis_feats)}
            fused_feats = features["fusion"]["fusion_output"]

        B, N, C = fused_feats.shape
        H = W = int(N ** 0.5)
        spatial_feats = fused_feats.transpose(1, 2).reshape(B, C, H, W)

        if self.use_gcm:
            upsampled_gis = nn.functional.interpolate(gis, size=(H, W), mode="bilinear", align_corners=False)
            concat_feats = torch.cat([spatial_feats, upsampled_gis], dim=1)
            projected = self.gcm_proj(concat_feats)
            projected = nn.functional.layer_norm(projected, projected.shape[1:])
            B, C, H, W = projected.shape
            tokens = projected.flatten(2).transpose(1, 2)
            features["gcm_input"] = tokens
            gis_for_priors = nn.functional.interpolate(gis, size=(H, W), mode="bilinear", align_corners=False)
            gis_embeddings = None
            if hasattr(self.gis_encoder, "encoder"):
                with torch.no_grad():
                    gis_embeddings = self.gis_encoder(gis_for_priors)
            gcm_out, gcm_attn_maps = self.gcm(tokens, gis_for_priors, gis_embeddings)
            features["gcm_output"] = gcm_out
            features["gcm_attention"] = gcm_attn_maps
            spatial_feats = gcm_out.transpose(1, 2).reshape(B, C, H, W)
            spatial_feats = self.decoder_proj(spatial_feats)

        features["graph_relation_input"] = spatial_feats.flatten(2).transpose(1, 2)
        refined_tokens = self.grm(features["graph_relation_input"])
        features["graph_relation_output"] = refined_tokens
        B, C, H, W = spatial_feats.shape
        spatial_feats = refined_tokens.transpose(1, 2).reshape(B, C, H, W)

        features["decoder_input"] = spatial_feats
        features["decoder"] = self.decoder.get_intermediate_features(spatial_feats, (256, 256))
        return features
