import pytest
import torch

from models.gcm import (
    SpatialDistancePrior,
    FeatureSimilarityPrior,
    RoadConnectivityPrior,
    UrbanSimilarityPrior,
    LearnedRelation,
    SceneWeightPredictor,
    GeographicRelationMatrix,
    SemanticGeographicAttention,
    GCMBlock,
    GCMTransformer,
)
from models.graph_relation import GraphRelationModule


class TestSpatialDistancePrior:
    def test_output_shape(self):
        prior = SpatialDistancePrior(grid_size=16, sigma=1.0)
        D = prior(batch_size=2)
        assert D.shape == (2, 256, 256)

    def test_symmetric(self):
        prior = SpatialDistancePrior(grid_size=16, sigma=1.0)
        coords = prior.coords
        dist = torch.cdist(coords, coords, p=2)
        dist = dist / (2 * prior.sigma**2)
        D_raw = torch.exp(-dist)
        assert torch.allclose(D_raw, D_raw.T, atol=1e-5)

    def test_row_sum(self):
        prior = SpatialDistancePrior(grid_size=16, sigma=1.0)
        D = prior(batch_size=1).squeeze(0)
        row_sums = D.sum(dim=-1)
        assert torch.allclose(row_sums, torch.ones_like(row_sums), atol=1e-5)


class TestFeatureSimilarityPrior:
    def test_output_shape(self):
        prior = FeatureSimilarityPrior(feature_dim=64)
        gis_emb = torch.randn(2, 256, 64)
        S = prior(gis_emb)
        assert S.shape == (2, 256, 256)

    def test_diagonal(self):
        prior = FeatureSimilarityPrior(feature_dim=64)
        gis_emb = torch.randn(2, 256, 64)
        S = prior(gis_emb)
        diagonal = torch.diagonal(S, dim1=-2, dim2=-1)
        assert torch.allclose(diagonal, torch.ones_like(diagonal), atol=1e-5)


class TestRoadConnectivityPrior:
    def test_output_shape(self):
        prior = RoadConnectivityPrior(grid_size=16)
        gis_feat = torch.randn(2, 18, 16, 16)
        R = prior(gis_feat)
        assert R.shape == (2, 256, 256)

    def test_diagonal_zero(self):
        prior = RoadConnectivityPrior(grid_size=16)
        gis_feat = torch.randn(2, 18, 16, 16)
        R = prior(gis_feat)
        diagonal = torch.diagonal(R, dim1=-2, dim2=-1)
        assert torch.allclose(diagonal, torch.zeros_like(diagonal), atol=1e-5)


class TestUrbanSimilarityPrior:
    def test_output_shape(self):
        prior = UrbanSimilarityPrior(gis_channels=18, latent_dim=16)
        gis_feat = torch.randn(2, 18, 16, 16)
        U = prior(gis_feat)
        assert U.shape == (2, 256, 256)


class TestLearnedRelation:
    def test_output_shape(self):
        lr = LearnedRelation(embed_dim=512, rank=64)
        tokens = torch.randn(2, 256, 512)
        L = lr(tokens)
        assert L.shape == (2, 256, 256)


class TestSceneWeightPredictor:
    def test_output_shape_and_sum(self):
        swp = SceneWeightPredictor(gis_channels=18, hidden_dim=64, scene_hidden=32, output_dim=5)
        gis_feat = torch.randn(2, 18, 32, 32)
        weights = swp(gis_feat)
        assert weights.shape == (2, 5)
        assert torch.allclose(weights.sum(dim=-1), torch.ones(2), atol=1e-5)


class TestGeographicRelationMatrix:
    def test_output_shape(self):
        grm = GeographicRelationMatrix(
            embed_dim=512,
            gis_channels=18,
            gis_feature_dim=64,
            grid_size=16,
            enable_scene_weights=True,
        )
        tokens = torch.randn(2, 256, 512)
        gis_features = torch.randn(2, 18, 16, 16)
        gis_embeddings = torch.randn(2, 256, 64)
        G, priors = grm(tokens, gis_features, gis_embeddings)
        assert G.shape == (2, 256, 256)
        assert "grg" in priors
        assert "scene_weights" in priors

    def test_ablation_flags(self):
        grm = GeographicRelationMatrix(
            embed_dim=512,
            gis_channels=18,
            gis_feature_dim=64,
            grid_size=16,
            enable_distance=False,
            enable_similarity=False,
            enable_road=False,
            enable_urban=False,
            enable_learned=False,
            enable_scene_weights=False,
        )
        tokens = torch.randn(2, 256, 512)
        gis_features = torch.randn(2, 18, 32, 32)
        G, priors = grm(tokens, gis_features)
        assert G.shape == (2, 256, 256)


class TestSemanticGeographicAttention:
    def test_output_shape(self):
        attn = SemanticGeographicAttention(embed_dim=512, num_heads=8, num_semantic_heads=5)
        x = torch.randn(2, 256, 512)
        grg = torch.randn(2, 256, 256)
        priors = {
            "distance": torch.randn(2, 256, 256),
            "similarity": torch.randn(2, 256, 256),
            "road": torch.randn(2, 256, 256),
            "urban": torch.randn(2, 256, 256),
            "learned": torch.randn(2, 256, 256),
            "grg": grg,
        }
        out, maps = attn(x, grg, priors)
        assert out.shape == (2, 256, 512)
        assert len(maps) == 5


class TestGCMBlock:
    def test_output_shape(self):
        block = GCMBlock({
            "embed_dim": 512,
            "num_heads": 8,
            "num_blocks": 2,
            "num_semantic_heads": 5,
            "mlp_ratio": 4.0,
            "dropout": 0.1,
            "gate_init": 0.1,
            "gis_channels": 18,
            "gis_feature_dim": 64,
            "grid_size": 16,
            "sigma_distance": 1.0,
            "scene_weight_hidden": 32,
            "enable_distance": True,
            "enable_similarity": True,
            "enable_road": True,
            "enable_urban": True,
            "enable_learned": True,
            "enable_scene_weights": True,
        })
        tokens = torch.randn(2, 256, 512)
        gis_features = torch.randn(2, 18, 16, 16)
        out, attn_maps = block(tokens, gis_features)
        assert out.shape == (2, 256, 512)

    def test_disable_modules(self):
        block = GCMBlock({
            "embed_dim": 512,
            "num_heads": 8,
            "num_blocks": 1,
            "num_semantic_heads": 5,
            "mlp_ratio": 4.0,
            "dropout": 0.1,
            "gate_init": 0.1,
            "gis_channels": 18,
            "gis_feature_dim": 64,
            "grid_size": 16,
            "sigma_distance": 1.0,
            "scene_weight_hidden": 32,
            "enable_distance": False,
            "enable_similarity": False,
            "enable_road": False,
            "enable_urban": False,
            "enable_learned": False,
            "enable_scene_weights": False,
        })
        tokens = torch.randn(2, 256, 512)
        gis_features = torch.randn(2, 18, 16, 16)
        out, _ = block(tokens, gis_features)
        assert out.shape == (2, 256, 512)


class TestGCMTransformer:
    def test_output_shape(self):
        transformer = GCMTransformer(
            embed_dim=512,
            num_heads=8,
            num_blocks=4,
            num_semantic_heads=5,
            gis_channels=18,
            gis_feature_dim=64,
            grid_size=16,
        )
        tokens = torch.randn(2, 256, 512)
        gis_features = torch.randn(2, 18, 16, 16)
        out, all_maps = transformer(tokens, gis_features)
        assert out.shape == (2, 256, 512)
        assert len(all_maps) == 4


class TestGraphRelationModule:
    def test_output_shape(self):
        module = GraphRelationModule(
            {"hidden_dim": 128, "num_relations": 4, "num_layers": 3, "dropout": 0.1}
        )
        tokens = torch.randn(2, 256, 128)
        out = module(tokens)
        assert out.shape == (2, 256, 128)

    def test_mismatch_input_raises(self):
        module = GraphRelationModule(
            {"hidden_dim": 128, "num_relations": 4, "num_layers": 2, "dropout": 0.1}
        )
        tokens = torch.randn(2, 256, 64)
        with pytest.raises(ValueError):
            module(tokens)

    def test_intermediate_features(self):
        module = GraphRelationModule(
            {"hidden_dim": 64, "num_relations": 2, "num_layers": 2, "dropout": 0.0}
        )
        tokens = torch.randn(2, 64, 64)
        feats = module.get_intermediate_features(tokens)
        assert "grm_input" in feats
        assert "grm_output" in feats
        assert feats["grm_output"].shape == (2, 64, 64)

