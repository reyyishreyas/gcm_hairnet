# GCM-HAIRNet

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10%2B-blue" alt="Python"/>
  <img src="https://img.shields.io/badge/PyTorch-2.0%2B-red" alt="PyTorch"/>
  <img src="https://img.shields.io/badge/License-MIT-green" alt="License"/>
  <img src="https://img.shields.io/badge/Status-Production-brightgreen" alt="Status"/>
</p>

**GCM-HAIRNet** is a multi-modal deep learning architecture for geospatial hazard risk prediction. It fuses satellite imagery with multi-channel GIS raster data through a novel **Geographic Context Module (GCM)** built on semantic geographic attention.

> **Test R² = 0.95381 | MSE = 0.00339 | MAE = 0.03952** on held-out cities (Jammu, Shimla, Srinagar, Guwahati, Thiruvananthapuram).

---

## Key Results

### Fusion Study (Table 7)

| Model | Test MSE | Test MAE | Test R² |
|-------|----------|----------|---------|
| **GCM-HAIRNet (Addition)** | **0.00339** | **0.03952** | **0.95381** |
| Bilinear | 0.00408 | 0.04605 | 0.94441 |
| Concatenation | 0.01450 | 0.06890 | 0.80252 |
| GIS-Only | 0.02194 | 0.08011 | 0.70133 |
| Image-Only | 0.02738 | 0.11606 | 0.62714 |

### Controlled Baselines (Table 8)

| Module | Test MSE | Test MAE | Test R² |
|--------|----------|----------|---------|
| **GCM-HAIRNet** | **0.00339** | **0.03952** | **0.95381** |
| **Controlled GCM** | **0.01396** | **0.06852** | **0.80987** |
| Non-Local | 0.02130 | 0.10153 | 0.70993 |
| ViT | 0.02188 | 0.10046 | 0.70209 |
| MHA | 0.02781 | 0.13637 | 0.62140 |
| Swin | 0.02831 | — | — |
| GraphSAGE | 0.03480 | 0.14879 | 0.52617 |

---

## Architecture

```
Inputs
├── Image:        (B, 3, 256, 256)
└── GIS Raster:   (B, 18, 32, 32)

Encoders
├── SwinTransformerEncoder (pretrained Swin-V2)
│   └── Output: (B, 256, 128)
└── GISEncoder (3-layer CNN)
    └── Output: (B, 256, 64)

Fusion: AdditionFusion
├── Linear(128→128) + Linear(64→128) + LayerNorm
└── Element-wise addition → (B, 256, 128)

GCM Pipeline
├── Conv2d(146→512) + LayerNorm → (B, 512, 16, 16)
├── GeographicRelationMatrix (5 priors + SceneWeightPredictor)
│   ├── Distance, Similarity, Road, Urban, Learned
│   └── GRG = α·D + β·S + γ·R + δ·U + ε·L
├── GCMTransformer × 4 blocks (8 heads, embed_dim=512)
└── Conv2d(512→128) → (B, 128, 16, 16)

GraphRelationModule (3 layers)
└── Output: (B, 256, 128)

Decoder (UPerNet-style)
├── 3× ConvTranspose2d upsample
└── Conv2d(16→1) → (B, 1, 256, 256)
```

**Total Parameters:** ~111M

See [`docs/ARCHITECTURE.md`](docs/ARCHITECTURE.md) for full details.

---

## Installation

### Option 1: Conda (recommended)

```bash
conda env create -f environment.yml
conda activate gcm-hairnet
pip install -e .
```

### Option 2: pip

```bash
pip install -r requirements.txt
pip install -e .
```

### Verify installation

```bash
python -c "import torch; print(torch.__version__); from models import build_model; print('OK')"
```

---

## Dataset

The dataset is **not included** in this repository. Download the processed data from Google Drive and place it in `data/processed/`:

**[Download Dataset (Google Drive)](https://drive.google.com/drive/folders/PLACEHOLDER_LINK_HERE)**  

After downloading, extract the contents so that the directory structure matches:

```
data/processed/
├── images/     # 256×256 satellite/aerial images (.npy)
├── gis/        # 32×32×18 GIS raster features (.npy)
├── labels/     # 256×256 risk maps (.npy)
├── metadata/   # Per-city metadata (JSON)
└── splits.json # Train/val/test splits
```

**Splits:** 58 train / 6 val / 5 test cities

---

## Quick Start

### 1. Train the proposed model (GCM-HAIRNet)

```bash
python scripts/train.py \
  --config gcm_ablation/full_gcm \
  --root-dir ./data/processed \
  --device cuda
```

Checkpoints are saved to `checkpoints/gcm_ablation/full_gcm/` by default.

### 2. Train fusion baselines

```bash
for config in baseline_image_only baseline_gis_only baseline_concat baseline_addition \
               baseline_gated baseline_cross_attention baseline_multihead_cross_attention baseline_bilinear; do
    python scripts/train.py --config $config --root-dir ./data/processed --device cuda
done
```

### 3. Train controlled relation-module baselines

```bash
for config in baselines/baseline_gcm baselines/baseline_vit baselines/baseline_swin \
               baselines/baseline_graphsage baselines/baseline_mha baselines/baseline_nonlocal; do
    python scripts/train.py --config $config --root-dir ./data/processed --device cuda
done
```

### 4. Run inference

```bash
python scripts/inference.py \
  --config inference \
  --checkpoint ./checkpoints/gcm_ablation/full_gcm/best.pt \
  --split test \
  --output-dir ./outputs/inference
```

### 5. Evaluate all models and generate figures

```bash
# Test all trained models
python scripts/evaluate_all_baselines.py

# Generate risk maps for all models
python scripts/generate_all_risk_maps.py \
  --root-dir ./data/processed \
  --output-dir ./outputs/experiments \
  --splits val test

# Generate comparison figures
python scripts/generate_per_city_comparison.py
```

### 6. Run the full experiment suite (train + evaluate + figures)

```bash
python scripts/run_experiments.py \
  --root-dir ./data/processed \
  --device cuda \
  --output-dir ./outputs
```

---

## Repository Structure

```
├── configs/                     # YAML experiment configs
│   ├── train.yaml               # Canonical training config
│   ├── default.yaml             # Default hyperparameters
│   ├── baselines/               # Baseline model configs (GCM, ViT, Swin, etc.)
│   ├── gcm_ablation/            # GCM component ablation configs
│   └── baseline_*.yaml          # Fusion study configs (concat, addition, etc.)
├── models/                      # Model implementations
│   ├── gcm_hairnet.py           # Main GCM-HAIRNet model
│   ├── baselines/               # Baseline variants (ViT, Swin, GraphSAGE, etc.)
│   ├── encoders/                # SwinV2 and GIS encoders
│   ├── fusion/                  # Addition, Concat, Bilinear (Table 7)
│   ├── gcm/                     # Geographic Context Module (priors, transformer)
│   ├── decoder/                 # UPerNet-style decoder
│   └── relation/                # Relation modules (MHA, Non-Local, etc.)
├── engine/                      # Trainer, Validator, Tester, Inferencer
├── losses/                      # Combined loss (MSE + L1 + Huber + SSIM)
├── metrics/                     # Regression and classification metrics
├── datasets/                    # Dataset loading and transforms
├── utils/                       # Config manager, checkpointing, seeding, logging
├── visualization/               # Risk map and attention map utilities
├── scripts/                     # Entry-point scripts
│   ├── train.py                 # Train any model from a config
│   ├── test.py                  # Test a trained model
│   ├── inference.py             # Run inference and save predictions
│   ├── validate.py              # Validate a checkpoint
│   ├── ablation.py              # Run GCM ablation study
│   ├── crossval.py              # K-fold cross-validation
│   ├── evaluate_all_baselines.py # Evaluate all trained baselines
│   ├── run_experiments.py       # Master script: train + evaluate all experiments
│   ├── generate_all_risk_maps.py # Generate risk maps for all models
│   └── generate_per_city_comparison.py # Generate comparison figures
├── docs/
│   ├── ARCHITECTURE.md          # Full architecture specification
│   ├── ablation.md              # Ablation study details
│   ├── dataset.md               # Dataset construction details
│   └── training.md              # Training protocol details
├── outputs/experiments/         # All experiment outputs (gitignored)
│   ├── results/                 # Canonical CSV, comparison figures
│   ├── fusion/                  # Per-model predictions and risk maps
│   ├── baseline/                # Baseline predictions and risk maps
│   └── ablation/                # Ablation JSON metrics
├── checkpoints/                 # Model weights (gitignored)
├── data/                        # Dataset (gitignored, download below)
├── environment.yml              # Conda environment
├── requirements.txt             # pip dependencies
├── CITATION.cff                 # Citation metadata
├── LICENSE                      # MIT License
└── CONTRIBUTING.md              # Contribution guidelines
```

---

## Reproduction

All experiments use the **same training protocol** for fair comparison:

| Parameter | Value |
|-----------|-------|
| Optimizer | AdamW |
| Learning Rate | 1e-4 |
| Weight Decay | 1e-4 |
| Betas | [0.9, 0.999] |
| Scheduler | CosineAnnealingLR (T_max=100, warmup=5) |
| Loss | MSE=1.0 + L1=0.5 + Huber=0.5 + Focal=0.0 |
| Batch Size | 16 train / 32 val |
| Max Epochs | 100 |
| Early Stopping | patience=15, monitor=val_loss |
| Gradient Clipping | 1.0 |
| Seed | 42 |
| Deterministic | true |

### Reproduce all experiments

The single command below trains every fusion variant, baseline, and ablation, then evaluates and saves all results:

```bash
python scripts/run_experiments.py \
  --root-dir ./data/processed \
  --device cuda \
  --output-dir ./outputs
```

To skip training and only evaluate existing checkpoints:

```bash
python scripts/run_experiments.py \
  --root-dir ./data/processed \
  --device cuda \
  --output-dir ./outputs \
  --skip-train
```

### Reproduce specific experiments

```bash
# Fusion study only
for config in baseline_image_only baseline_gis_only baseline_concat baseline_addition \
               baseline_gated baseline_cross_attention baseline_multihead_cross_attention baseline_bilinear; do
    python scripts/train.py --config $config --root-dir ./data/processed --device cuda
done

# Controlled baselines only
for config in baselines/baseline_gcm baselines/baseline_vit baselines/baseline_swin \
               baselines/baseline_graphsage baselines/baseline_mha baselines/baseline_nonlocal; do
    python scripts/train.py --config $config --root-dir ./data/processed --device cuda
done

# GCM ablations only
for config in gcm_ablation/full_gcm gcm_ablation/no_distance gcm_ablation/no_similarity \
               gcm_ablation/no_road gcm_ablation/no_urban gcm_ablation/no_learned \
               gcm_ablation/no_scene_weights gcm_ablation/no_gcm gcm_ablation/no_gct \
               gcm_ablation/no_gct_no_gcm; do
    python scripts/train.py --config $config --root-dir ./data/processed --device cuda
done
```

### Evaluate and generate figures

```bash
# Test all models
python scripts/evaluate_all_baselines.py

# Generate risk maps
python scripts/generate_all_risk_maps.py \
  --root-dir ./data/processed \
  --output-dir ./outputs/experiments \
  --splits val test

# Generate comparison figures
python scripts/generate_per_city_comparison.py
```

---

## Results

All results are in [`outputs/experiments/results/`](outputs/experiments/results/):

- `experiment_results.csv` — Canonical results table
- `comparison_test_sorted.png` — All models sorted by R²
- `fusion_comparison_test.png` — Fusion study comparison
- `baseline_comparison_test.png` — Baseline comparison
- `metrics_table_test.png` — Metrics summary table

Per-model predictions and risk maps are in [`outputs/experiments/{model}/{split}/`](outputs/experiments/).

---

## Citation

```bibtex
@software{gcmhairnet2025,
  title = {GCM-HAIRNet: Geographic Context Multi-Modal Hazard Risk Network},
  author = {Anonymous},
  year = {2025},
  url = {https://github.com/anon/GCM-HAIRNet},
  version = {1.0.0}
}
```

---

## License

MIT — see [`LICENSE`](LICENSE)

---

## Contact

For questions about the architecture or reproduction, open a GitHub issue.
