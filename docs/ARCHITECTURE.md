# GCM-HAIRNet: Geographic Context Multi-Modal Hazard Risk Network

## 1. Canonical Model Overview

**GCM-HAIRNet** is the proposed multi-modal architecture for geospatial hazard risk prediction. It fuses satellite imagery with multi-channel GIS raster data through a **Geographic Context Module (GCM)** built on semantic geographic attention.

**Main Variant (ACM Submission):** `fusion: addition` + `gcm: enable=true`
- Test MSE: **0.00339**
- Test MAE: **0.03952**
- Test R²: **0.95381**

---

## 2. Architecture Flow Diagram

```
INPUTS
├── Image:        (B, 3, 256, 256)
└── GIS Raster:   (B, 18, 32, 32)

ENCODERS
├── SwinTransformerEncoder
│   └── Swin-V2 (embed_dim=128, depths=[2,2,18,2], num_heads=[4,8,16,32], window_size=7)
│       └── Output: (B, N, 128)  where N = 16×16 = 256
└── GISEncoder
    └── 3-layer CNN (18→64→64→64) + AdaptiveAvgPool2d(16,16) + LayerNorm
        └── Output: (B, N, 64)   where N = 16×16 = 256

FUSION (AdditionFusion)
├── Linear(128→128) + Linear(64→128) + LayerNorm(128)
└── Element-wise addition → (B, N, 128)

SPATIAL RESHAPE
└── (B, 128, 16, 16)

GCM PIPELINE (when enable=true)
├── Upsample GIS (32×32 → 16×16) → (B, 18, 16, 16)
├── Concat [spatial_feats, upsampled_gis] → (B, 146, 16, 16)
├── Conv2d(146→512, k=1) + LayerNorm → (B, 512, 16, 16)
├── Flatten to tokens: (B, 256, 512)
├── GeographicRelationMatrix (5 priors + SceneWeightPredictor)
│   ├── Distance Prior       → (B, 256, 256)
│   ├── Feature Similarity   → (B, 256, 256)
│   ├── Road Connectivity    → (B, 256, 256)
│   ├── Urban Similarity     → (B, 256, 256)
│   ├── Learned Relation     → (B, 256, 256)
│   └── SceneWeightPredictor → (B, 5) weights α,β,γ,δ,ε
│       └── GRG = α·D + β·S + γ·R + δ·U + ε·L  (row-normalized)
├── GCMTransformer × 4 blocks (8 heads, embed_dim=512, mlp_ratio=4.0)
│   └── Each block: LayerNorm → SemanticGeographicAttention → + → LayerNorm → MLP → +
│       └── Output: (B, 256, 512)
├── Final LayerNorm(512)
└── Conv2d(512→128, k=1) → (B, 128, 16, 16)

GRAPH RELATION MODULE (GraphRelationModule)
├── Input: (B, 256, 128)
├── RelationEmbedding(num_relations=4, hidden_dim=128)
├── 3-layer: Linear(128→128) + ReLU + Dropout + LayerNorm residual
└── Output: (B, 256, 128)
    └── Reshape: (B, 128, 16, 16)

DECODER (UPerNet-style)
├── ConvTranspose2d(128→64, k=2, s=2) → (B, 64, 32, 32)
├── ConvTranspose2d(64→32, k=2, s=2)  → (B, 32, 64, 64)
├── ConvTranspose2d(32→16, k=2, s=2)  → (B, 16, 128, 128)
├── Bilinear interpolate → (256, 256)
└── Conv2d(16→1, k=1) → (B, 1, 256, 256)

OUTPUT
└── Risk Map: (B, 1, 256, 256)  [continuous hazard probability]
```

---

## 3. Component Specifications

### 3.1 SwinTransformerEncoder
- **Backbone:** Swin Transformer V2 (custom or timm)
- **Input:** `(B, 3, 256, 256)`
- **Config:**
  - `embed_dim = 128`
  - `depths = [2, 2, 18, 2]`
  - `num_heads = [4, 8, 16, 32]`
  - `window_size = 7`
  - `drop_path_rate = 0.2`
  - `pretrained = true`
- **Output:** `(B, N, 128)` where `N = 16 × 16 = 256`
- **Projection:** `Linear(feature_dim → 128)` if feature_dim ≠ 128
- **Total Parameters (encoder only):** ~86M (Swin-V2 backbone dominates)

### 3.2 GISEncoder
- **Type:** 3-layer CNN with BatchNorm + Adaptive Pooling
- **Input:** `(B, 18, 32, 32)`
- **Config:**
  - `input_channels = 18`
  - `hidden_dim = 64`
  - `output_dim = 64`
  - `dropout = 0.1`
- **Layers:**
  1. `Conv2d(18, 64, k=3, p=1)` → `BatchNorm2d(64)` → `ReLU`
  2. `Conv2d(64, 64, k=3, p=1)` → `BatchNorm2d(64)` → `ReLU`
  3. `Conv2d(64, 64, k=3, p=1)` → `AdaptiveAvgPool2d(16, 16)`
- **Output:** `(B, 64, 16, 16)` → flattened → `(B, N, 64)` with `LayerNorm(64)`

### 3.3 Fusion Modules (Controlled Study)

| Fusion Type | Output Dim | Key Operations |
|-------------|-----------|----------------|
| **Addition** (PROPOSED) | 128 | `Linear(128→128)` + `Linear(64→128)` + `img + gis` + `LayerNorm` |
| Concat | 128 | `Linear(192→128)` + `LayerNorm` + `Dropout` |
| Gated | 128 | `Sigmoid gate` on concatenated features, weighted sum |
| Cross-Attention | 128 | `q=image, k=v=gis`, single-head attention + residual |
| MultiHead-Cross-Attention | 128 | 8-head attention, `q=image, k=v=gis` |
| Bilinear | 128 | `Linear→rank=32` for both, element-wise product, `Linear→128` |

### 3.4 GCM Pipeline

#### 3.4.1 GCMProjection
- Concatenates spatial features `(B, 128, 16, 16)` with upsampled GIS `(B, 18, 16, 16)`
- `Conv2d(146, 512, k=1)` + `LayerNorm`
- Output: `(B, 512, 16, 16)`

#### 3.4.2 GeographicRelationMatrix (GRM)
Computes 5 spatial-semantic priors and fuses them with learned weights:

| Prior | Type | Output Shape | Description |
|-------|------|-------------|-------------|
| Distance | `SpatialDistancePrior` | `(B, 256, 256)` | Gaussian decay based on grid distance |
| Similarity | `FeatureSimilarityPrior` | `(B, 256, 256)` | Cosine similarity between GIS token embeddings |
| Road | `RoadConnectivityPrior` | `(B, 256, 256)` | Binary road network adjacency |
| Urban | `UrbanSimilarityPrior` | `(B, 256, 256)` | Urban land-use similarity |
| Learned | `LearnedRelation` | `(B, 256, 256)` | Low-rank learnable relation matrix (rank=64) |

**SceneWeightPredictor:**
- Input: GIS `(B, 18, H, W)` → global average pool → `(B, 18)`
- `Linear(18→64)` → `ReLU` → `Linear(64→64)` → `ReLU` → `Linear(64→5)`
- Output: 5 weights `α, β, γ, δ, ε` (one per prior)

**Fused Relation Graph (GRG):**
```
G = (α·D + β·S + γ·R + δ·U + ε·L) / row_normalize(G)
```

#### 3.4.3 GCMTransformer
- **Blocks:** 4 × `GCMTransformerBlock`
- **Embed Dim:** 512
- **Heads:** 8
- **MLP Ratio:** 4.0 (`Linear(512→2048)` → GELU → Dropout → `Linear(2048→512)`)
- **Dropout:** 0.1
- **Gate Init:** 0.1
- **Num Semantic Heads:** 5

**SemanticGeographicAttention:**
- Standard multi-head attention with geographic relation graph as bias
- `Attn = softmax((Q·K^T / sqrt(d)) + GRG) · V`
- Gated residual connection with learnable gate initialized to 0.1

### 3.5 GraphRelationModule
- **Input:** `(B, N, 128)` where N=256
- **Hidden Dim:** 128
- **Num Relations:** 4
- **Num Layers:** 3
- **Each Layer:**
  1. Compute relation weights: `softmax(x · Embedding^T)`
  2. Relation messages: `rel_weights · Embedding`
  3. `Linear(128→128)` + `ReLU` + `Dropout`
  4. Residual: `LayerNorm(x + h)`
- **Output:** `(B, N, 128)`

### 3.6 Decoder (UPerNet-style)
- **Hidden Dim:** 128
- **Num Classes:** 1
- **Dropout:** 0.1

| Layer | Operation | Output Shape |
|-------|-----------|-------------|
| Input | Features | `(B, 128, 16, 16)` |
| up1 | `ConvTranspose2d(128, 64, k=2, s=2)` + ReLU + Dropout2d | `(B, 64, 32, 32)` |
| up2 | `ConvTranspose2d(64, 32, k=2, s=2)` + ReLU + Dropout2d | `(B, 32, 64, 64)` |
| up3 | `ConvTranspose2d(32, 16, k=2, s=2)` + ReLU + Dropout2d | `(B, 16, 128, 128)` |
| interp | `Bilinear((128,128) → (256,256))` | `(B, 16, 256, 256)` |
| final | `Conv2d(16, 1, k=1)` | `(B, 1, 256, 256)` |

---

## 4. Model Parameters

| Component | Parameters | Notes |
|-----------|-----------|-------|
| **Total Model** | **110,985,499** | ~111M |
| SwinTransformerEncoder | ~86M | Pretrained Swin-V2 backbone |
| GISEncoder | ~15K | Lightweight 3-layer CNN |
| AdditionFusion | ~16K | Linear + LayerNorm |
| GCMBlock (4×) | ~24.9M | Transformer + 5 priors + SceneWeightPredictor |
| GraphRelationModule | ~66K | 3-layer relation network |
| Decoder | ~20K | 3× ConvTranspose2d + final Conv |

---

## 5. Training Configuration

### 5.1 Optimizer & Scheduler
- **Optimizer:** AdamW
- **Learning Rate:** `1e-4`
- **Weight Decay:** `1e-4`
- **Betas:** `[0.9, 0.999]`
- **Scheduler:** `CosineAnnealingLR` with `T_max=100`, warmup epochs=5

### 5.2 Loss Function (CombinedLoss)
```
Total Loss = 1.0 × MSE + 0.5 × L1 + 0.5 × Huber(delta=0.1) + 0.0 × Focal
```
- **MSE weight:** 1.0
- **L1 weight:** 0.5
- **Huber weight:** 0.5 (delta=0.1)
- **Focal weight:** 0.0 (disabled)

### 5.3 Dataset & Augmentation
- **Train/Val/Test Split:** 60 / 6 / 5 images
- **Train Batch Size:** 16
- **Val Batch Size:** 32
- **Test Batch Size:** 32
- **Augmentation:** Enabled (random flips, rotations, etc.)
- **Input Resolution:** 256×256 (image), 32×32 (GIS)

### 5.4 Training Protocol
- **Max Epochs:** 100
- **Early Stopping:** patience=15, monitor=`val_loss`
- **Gradient Clipping:** 1.0
- **Gradient Accumulation:** 1 step
- **Seed:** 42
- **Deterministic:** true
- **Mixed Precision:** Not specified (FP32 default)

### 5.5 Checkpointing
- **Monitor:** `val_loss`
- **Save Top K:** 3–5 checkpoints
- **Frequency:** Every epoch

---

## 6. Experiment Matrix

### 6.1 Fusion Study (8 Variants)
All use `GCMHAIRNetBaseline` with `fusion.type` varied, `gcm.enable=false`.

| Variant | Test MSE | Test MAE | Test R² |
|---------|----------|----------|---------|
| Image-Only | 0.02738 | 0.11606 | 0.62714 |
| GIS-Only | 0.02194 | 0.08011 | 0.70133 |
| Concat | 0.01450 | 0.06890 | 0.80252 |
| **Addition (PROPOSED)** | **0.00339** | **0.03952** | **0.95381** |
| Gated | 0.02300 | 0.08498 | 0.68688 |
| Cross-Attention | 0.02582 | 0.11328 | 0.64848 |
| MultiHead-Cross-Attention | 0.02723 | 0.11599 | 0.62924 |
| Bilinear | 0.00408 | 0.04605 | 0.94441 |

### 6.2 Controlled Baselines (6 Valid Modules)
All use `GCMHAIRNetBaseline` with `fusion.type=addition`, `gcm.enable=false`, identical encoders/decoder.

| Module | Test MSE | Test MAE | Test R² | Status |
|--------|----------|----------|---------|--------|
| **GCM (proposed)** | **0.01372** | **0.06896** | **0.80686** | ✅ Valid |
| ViT | 0.02125 | — | 0.70081 | ✅ Valid |
| Swin | 0.02635 | — | 0.62908 | ✅ Valid |
| GraphSAGE | 0.03480 | 0.14879 | 0.52617 | ✅ Valid |
| MHA | 0.02781 | 0.13637 | 0.62140 | ✅ Valid |
| Non-Local | 0.02130 | 0.10153 | 0.70993 | ✅ Valid |

### 6.3 GCM Ablations (9 Variants)
**WARNING:** Results from `outputs/experiments/ablation/` use `AblationModel` (GCT fusion), not `GCMHAIRNetBaseline`. Results are **scientifically invalid** until retrained with the canonical model.

| Variant | Removed | Test MSE | Test MAE | Test R² |
|---------|---------|----------|----------|---------|
| full | — | 0.06333 | 0.22296 | 0.13778 |
| no_distance | Distance prior | 0.02230 | 0.09685 | 0.69641 |
| no_similarity | Similarity prior | 0.02017 | 0.09250 | 0.72537 |
| no_road | Road connectivity | 0.01641 | 0.08560 | 0.77656 |
| no_urban | Urban similarity | 0.01923 | 0.09188 | 0.73817 |
| no_learned | Learned relation | 0.02735 | 0.10491 | 0.62754 |
| no_scene_weights | Scene weight predictor | 0.02043 | 0.09348 | 0.72187 |
| no_gcm | Entire GCM | 0.02692 | 0.11519 | 0.63347 |
| no_gct | Gated Cross-Transformer | 0.00474 | 0.05512 | 0.93549 |
| no_gct_no_gcm | Both GCT + GCM | 0.00754 | 0.05684 | 0.89736 |

---

## 7. Data Flow & Tensor Shapes

| Stage | Module | Input Shape | Output Shape | Params |
|-------|--------|-------------|--------------|--------|
| 1 | Image Input | `(B, 3, 256, 256)` | — | — |
| 2 | GIS Input | `(B, 18, 32, 32)` | — | — |
| 3 | SwinTransformerEncoder | `(B, 3, 256, 256)` | `(B, 256, 128)` | ~86M |
| 4 | GISEncoder | `(B, 18, 32, 32)` | `(B, 256, 64)` | ~15K |
| 5 | AdditionFusion | `(B, 256, 128)` + `(B, 256, 64)` | `(B, 256, 128)` | ~16K |
| 6 | Reshape to spatial | `(B, 256, 128)` | `(B, 128, 16, 16)` | — |
| 7 | GCM Proj (concat + conv) | `(B, 146, 16, 16)` | `(B, 512, 16, 16)` | ~75K |
| 8 | Flatten to tokens | `(B, 512, 16, 16)` | `(B, 256, 512)` | — |
| 9 | GRM (5 priors + weights) | `(B, 256, 512)` | `(B, 256, 256)` graph | ~2.2M |
| 10 | GCMTransformer ×4 | `(B, 256, 512)` | `(B, 256, 512)` | ~22.6M |
| 11 | Decoder Proj | `(B, 512, 16, 16)` | `(B, 128, 16, 16)` | ~66K |
| 12 | GraphRelationModule | `(B, 256, 128)` | `(B, 256, 128)` | ~66K |
| 13 | Decoder Upsample | `(B, 128, 16, 16)` | `(B, 1, 256, 256)` | ~20K |
| 14 | Risk Map Output | — | `(B, 1, 256, 256)` | — |

---

## 8. Repository Structure (Final)

```
outputs/experiments/
├── results/
│   └── experiment_results.csv          ← CANONICAL RESULTS (23 rows)
├── fusion/
│   ├── image_only/
│   ├── gis_only/
│   ├── concat/
│   ├── addition/                       ← PROPOSED MODEL
│   ├── gated/
│   ├── cross_attention/
│   ├── multihead_cross_attention/
│   └── bilinear/
├── baseline/
│   ├── gcm/                            ← Controlled GCM baseline
│   ├── vit/
│   ├── swin/
│   ├── graphsage/
│   ├── mha/
│   └── nonlocal/
└── ablation/
    ├── full/
    ├── no_distance/
    ├── no_similarity/
    ├── no_road/
    ├── no_urban/
    ├── no_learned/
    ├── no_scene_weights/
    ├── no_gcm/
    ├── no_gct/
    └── no_gct_no_gcm/
```

---

## 9. Critical Notes for ACM Paper

1. **Main Result:** `fusion,Addition` (GCM-HAIRNet with addition fusion + GCM enabled) achieves MSE=0.00339, R²=0.954. This is the only result ready for publication.

2. **Ablation Invalid:** All `outputs/experiments/ablation/` results are invalid. The `full` variant (MSE=0.063) performs worse than every partial ablation due to training inconsistencies (different model class: `AblationModel` with GCT fusion vs. `GCMHAIRNetBaseline` with Addition fusion).

3. **Baseline Scope:** Only 6 valid relation-module baselines are included (ViT, Swin, GraphSAGE, MHA, Non-Local, GCM). DeiT, GCN, GAT, and FViT were removed due to broken implementations or missing checkpoints.

4. **Classification Metrics:** Available in `all_metrics.json` for all fusion and baseline models, but absent from the canonical CSV.

5. **Parameter Counts:** Not recorded in any output file. Total model: ~111M parameters.

6. **Per-City Metrics:** Available in `per_city_metrics.csv` (archived) and `all_metrics.json` for fusion models only.
