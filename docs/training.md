# Training Documentation

## Setup

```bash
pip install -r requirements.txt
```

## Training

```bash
python scripts/train.py --config train --root-dir ./data/processed
```

## Configuration

Training hyperparameters are managed via YAML files in `configs/`:

- `configs/train.yaml` - Training-specific overrides
- `configs/default.yaml` - Default configuration
- `configs/model.yaml` - Model architecture settings
- `configs/dataset.yaml` - Dataset settings

## Checkpointing

Checkpoints are saved to `checkpoints/gcm/` by default:
- `best.pt` - Best model based on monitored metric
- `last.pt` - Most recent checkpoint
- `epoch_XXXX.pt` - Epoch-specific checkpoints

## Logging

Logs are written to `logs/` via TensorBoard:
```bash
tensorboard --logdir logs
```

## Resuming Training

```bash
python scripts/train.py --config train --checkpoint ./checkpoints/gcm/last.pt
```

## Reproducibility

Set `experiment.seed` and `experiment.deterministic` in config for reproducible results.
