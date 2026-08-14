# Contributing to GCM-HAIRNet

Thank you for your interest in contributing! This document provides guidelines for contributing to this research repository.

## Code of Conduct

Be respectful, inclusive, and constructive. We welcome contributions from everyone.

## How to Contribute

### Reporting Bugs

- Use the GitHub issue tracker
- Describe the expected vs actual behavior
- Include reproduction steps, environment details, and logs

### Proposing Features

- Open an issue first to discuss the proposed change
- Explain the use case and expected impact

### Pull Requests

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature`
3. Install dev dependencies: `pip install -r requirements-dev.txt`
4. Make your changes and ensure tests pass: `pytest tests/`
5. Format code: `black . && isort .`
6. Lint: `flake8 .`
7. Commit with a clear message
8. Push and open a PR against `main`

## Development Setup

```bash
# Clone
git clone https://github.com/anon/GCM-HAIRNet.git
cd GCM-HAIRNet

# Create environment
conda env create -f environment.yml
conda activate gcm-hairnet

# Install package
pip install -e .

# Run tests
pytest tests/ -v
```

## Reproducing Paper Results

See the [Reproduction Guide](docs/SUMMARY.md#reproduction) for exact commands.

## Citation

If this work contributes to your research, please cite it:

```bibtex
@software{gcmhairnet2025,
  title = {GCM-HAIRNet: Geographic Context Multi-Modal Hazard Risk Network},
  author = {Anonymous},
  year = {2025},
  url = {https://github.com/anon/GCM-HAIRNet},
  version = {1.0.0}
}
```

## License

By contributing, you agree that your contributions will be licensed under the MIT License.
