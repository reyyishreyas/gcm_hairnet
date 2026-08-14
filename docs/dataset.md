# Dataset Documentation

## Overview

The dataset is located in `data/processed/` and must not be modified during training or evaluation.

## Structure

```
data/processed/
  images/        - Satellite/aerial images (256x256x3 .npy)
  gis/           - GIS features (32x32x18 .npy)
  labels/        - Risk maps (32x32 .npy)
  metadata/      - Per-city metadata JSON files
  splits.json    - Train/val/test splits
```

## Splits

The dataset is pre-split into train/val/test sets by city:

- **Train**: 58 cities
- **Val**: 6 cities
- **Test**: 5 cities

## Normalization

Normalization statistics are stored in `data/normalization_stats.json` and should be applied during preprocessing.

## Loading

Use `GCMHAIRNetDataset` from `datasets/` to load the data. The dataset automatically:
- Reads `splits.json` for train/val/test splits
- Loads `.npy` files for images, GIS, and labels
- Applies optional transforms
- Returns batched tensors via `collate_fn`

## Reproducibility

The dataset loading is deterministic given a fixed random seed. Do not shuffle or modify the `.npy` files.
