# Ablation Study Documentation

## Running Ablations

```bash
python scripts/ablation.py --config train --checkpoint ./checkpoints/gcm/best.pt
```

## Configuration

Ablation settings in `configs/default.yaml`:

```yaml
ablation:
  modules: ["swin", "gis_encoder", "gct", "grm", "decoder"]
  strategy: "replace_with_identity"
```

## Outputs

Results are saved to `outputs/tables/ablation_results.json` and `checkpoints/ablation/`.

## Strategies

- `replace_with_identity` - Replace module output with zeros to measure contribution
- `replace_with_mean` - Replace with mean feature vector

## Metrics

Ablation results include:
- Validation loss per ablated module
- Relative performance drop compared to full model
