from typing import Dict, Optional, Tuple

import torch
import torch.nn as nn

from .distance_prior import SpatialDistancePrior
from .feature_similarity import FeatureSimilarityPrior
from .learned_relation import LearnedRelation
from .road_connectivity import RoadConnectivityPrior
from .scene_weight_predictor import SceneWeightPredictor
from .urban_similarity import UrbanSimilarityPrior


class GeographicRelationMatrix(nn.Module):
    def __init__(self, config: Optional[Dict] = None, **kwargs):
        super().__init__()
        if config is None:
            config = kwargs
        else:
            config = dict(config)
            config.update(kwargs)
        embed_dim = config.get("embed_dim", 512)
        gis_channels = config.get("gis_channels", 18)
        gis_feature_dim = config.get("gis_feature_dim", 64)
        grid_size = config.get("grid_size", 16)
        sigma_distance = config.get("sigma_distance", 1.0)
        scene_weight_hidden = config.get("scene_weight_hidden", 32)
        enable_distance = config.get("enable_distance", True)
        enable_similarity = config.get("enable_similarity", True)
        enable_road = config.get("enable_road", True)
        enable_urban = config.get("enable_urban", True)
        enable_learned = config.get("enable_learned", True)
        enable_scene_weights = config.get("enable_scene_weights", True)

        self.num_tokens = grid_size * grid_size
        self.sigma_distance = sigma_distance
        self.scene_weight_hidden = scene_weight_hidden
        self.enable_distance = enable_distance
        self.enable_similarity = enable_similarity
        self.enable_road = enable_road
        self.enable_urban = enable_urban
        self.enable_learned = enable_learned
        self.enable_scene_weights = enable_scene_weights

        if self.enable_distance:
            self.distance_prior = SpatialDistancePrior(grid_size=grid_size, sigma=sigma_distance)
        if self.enable_similarity:
            self.similarity_prior = FeatureSimilarityPrior(feature_dim=gis_feature_dim)
        if self.enable_road:
            self.road_prior = RoadConnectivityPrior(grid_size=grid_size)
        if self.enable_urban:
            self.urban_prior = UrbanSimilarityPrior(gis_channels=gis_channels, latent_dim=16)
        if self.enable_learned:
            self.learned_relation = LearnedRelation(embed_dim=embed_dim, rank=64)
        if self.enable_scene_weights:
            self.scene_weight_predictor = SceneWeightPredictor(
                gis_channels=gis_channels,
                hidden_dim=64,
                scene_hidden=scene_weight_hidden,
                output_dim=5,
            )
            self.register_parameter("alpha", nn.Parameter(torch.tensor(0.2)))
            self.register_parameter("beta", nn.Parameter(torch.tensor(0.2)))
            self.register_parameter("gamma", nn.Parameter(torch.tensor(0.2)))
            self.register_parameter("delta", nn.Parameter(torch.tensor(0.2)))
            self.register_parameter("epsilon", nn.Parameter(torch.tensor(0.2)))
        else:
            self.alpha = nn.Parameter(torch.tensor(0.2))
            self.beta = nn.Parameter(torch.tensor(0.2))
            self.gamma = nn.Parameter(torch.tensor(0.2))
            self.delta = nn.Parameter(torch.tensor(0.2))
            self.epsilon = nn.Parameter(torch.tensor(0.2))

    def forward(
        self,
        tokens: torch.Tensor,
        gis_features: Optional[torch.Tensor] = None,
        gis_embeddings: Optional[torch.Tensor] = None,
    ) -> Tuple[torch.Tensor, Dict[str, torch.Tensor]]:
        if gis_features is None:
            gis_features = torch.zeros(tokens.shape[0], 18, 16, 16, device=tokens.device)
        B = tokens.shape[0]
        N = tokens.shape[1]
        actual_grid_size = int(N ** 0.5)
        priors = {}
        embed_dim = tokens.shape[-1]
        device = tokens.device

        if self.enable_distance:
            if hasattr(self, "distance_prior") and self.distance_prior.num_tokens == N:
                D = self.distance_prior(B)
            else:
                D = SpatialDistancePrior(grid_size=actual_grid_size, sigma=self.sigma_distance).to(device)(B)
            priors["distance"] = D
        else:
            D = torch.zeros(B, N, N, device=device)

        if self.enable_similarity and gis_embeddings is not None:
            if gis_embeddings.dim() == 3:
                B, N, C = gis_embeddings.shape
                side = int(N ** 0.5)
                gis_embeddings_4d = gis_embeddings.transpose(1, 2).reshape(B, C, side, side)
            else:
                gis_embeddings_4d = gis_embeddings
            if gis_embeddings_4d.shape[2] != actual_grid_size or gis_embeddings_4d.shape[3] != actual_grid_size:
                gis_embeddings_4d = torch.nn.functional.interpolate(gis_embeddings_4d, size=actual_grid_size, mode="bilinear", align_corners=False)
            S = self.similarity_prior(gis_embeddings_4d)
            priors["similarity"] = S
        else:
            S = torch.zeros_like(D)

        if self.enable_road:
            gis_for_road = torch.nn.functional.interpolate(gis_features, size=actual_grid_size, mode="bilinear", align_corners=False)
            R = self.road_prior(gis_for_road)
            priors["road"] = R
        else:
            R = torch.zeros_like(D)

        if self.enable_urban:
            gis_for_urban = torch.nn.functional.interpolate(gis_features, size=actual_grid_size, mode="bilinear", align_corners=False)
            U = self.urban_prior(gis_for_urban)
            priors["urban"] = U
        else:
            U = torch.zeros_like(D)

        if self.enable_learned:
            L = self.learned_relation(tokens)
            priors["learned"] = L
        else:
            L = torch.zeros_like(D)

        if self.enable_scene_weights:
            weights = self.scene_weight_predictor(gis_features)
            alpha = weights[:, 0].view(B, 1, 1)
            beta = weights[:, 1].view(B, 1, 1)
            gamma = weights[:, 2].view(B, 1, 1)
            delta = weights[:, 3].view(B, 1, 1)
            epsilon = weights[:, 4].view(B, 1, 1)
            priors["scene_weights"] = weights
        else:
            alpha = self.alpha.view(1, 1, 1)
            beta = self.beta.view(1, 1, 1)
            gamma = self.gamma.view(1, 1, 1)
            delta = self.delta.view(1, 1, 1)
            epsilon = self.epsilon.view(1, 1, 1)

        G = alpha * D + beta * S + gamma * R + delta * U + epsilon * L
        G = G / (G.sum(dim=-1, keepdim=True) + 1e-8)
        priors["grg"] = G

        return G, priors

    def get_intermediate_features(self, feats: torch.Tensor, gis_features: Optional[torch.Tensor] = None) -> Dict[str, torch.Tensor]:
        features = {"grm_input": feats}
        features["grm_output"] = self.forward(feats, gis_features)[0]
        return features
