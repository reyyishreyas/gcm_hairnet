from typing import Dict

from .base import BaseModel
from .encoders.swin import SwinTransformerEncoder
from .encoders.gis_encoder import GISEncoder
from .fusion.gct import GatedCrossAttention
from .gcm.grm import GeographicRelationMatrix
from .graph_relation import GraphRelationModule
from .decoder.risk_decoder import Decoder
from .gcm_hairnet import GCMHAIRNet
from .baselines.tiny_cnn import TinyRiskCNN
from .baselines.baseline_model import BaselineModel
from .baselines.ablation_model import AblationModel
from .baselines.gcm_hairnet_baseline import GCMHAIRNetBaseline
from .baselines.modality_models import ImageOnlyModel, GISOnlyModel


def build_model(config: Dict):
    model_name = config.get("name", "GCM-HAIRNet")
    if model_name == "GCM-HAIRNet":
        return GCMHAIRNet(config)
    elif model_name == "TinyRiskCNN":
        return TinyRiskCNN(config)
    elif model_name == "BaselineModel":
        return BaselineModel(config)
    elif model_name == "AblationModel":
        return AblationModel(config)
    elif model_name == "GCMHAIRNetBaseline":
        return GCMHAIRNetBaseline(config)
    elif model_name == "ImageOnlyModel":
        return ImageOnlyModel(config)
    elif model_name == "GISOnlyModel":
        return GISOnlyModel(config)
    else:
        raise ValueError(f"Unknown model: {model_name}")


__all__ = [
    "BaseModel",
    "SwinTransformerEncoder",
    "GISEncoder",
    "GatedCrossAttention",
    "GeographicRelationMatrix",
    "GraphRelationModule",
    "Decoder",
    "GCMHAIRNet",
    "TinyRiskCNN",
    "BaselineModel",
    "AblationModel",
    "GCMHAIRNetBaseline",
    "ImageOnlyModel",
    "GISOnlyModel",
    "build_model",
]
