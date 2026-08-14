import os
import tempfile
from pathlib import Path

import numpy as np
import pytest
import torch

from datasets import GCMHAIRNetDataset


class TestGCMHAIRNetDataset:
    @pytest.fixture
    def temp_data_dir(self):
        with tempfile.TemporaryDirectory() as tmpdir:
            root = Path(tmpdir)
            (root / "images").mkdir()
            (root / "gis").mkdir()
            (root / "labels").mkdir()
            (root / "metadata").mkdir()
            splits = {"train": ["city1"], "val": ["city2"], "test": ["city3"]}
            import json
            with open(root / "splits.json", "w") as f:
                json.dump(splits, f)

            np.save(root / "images" / "city1_image.npy", np.random.rand(256, 256, 3).astype(np.float32))
            np.save(root / "gis" / "city1_gis.npy", np.random.rand(32, 32, 18).astype(np.float32))
            np.save(root / "labels" / "city1_risk.npy", np.random.rand(32, 32).astype(np.float32))
            yield str(root)

    def test_dataset_loads_train_split(self, temp_data_dir):
        dataset = GCMHAIRNetDataset(root_dir=temp_data_dir, split="train")
        assert len(dataset) == 1

    def test_dataset_loads_val_split(self, temp_data_dir):
        dataset = GCMHAIRNetDataset(root_dir=temp_data_dir, split="val")
        assert len(dataset) == 1

    def test_dataset_loads_test_split(self, temp_data_dir):
        dataset = GCMHAIRNetDataset(root_dir=temp_data_dir, split="test")
        assert len(dataset) == 1

    def test_dataset_getitem(self, temp_data_dir):
        dataset = GCMHAIRNetDataset(root_dir=temp_data_dir, split="train")
        sample = dataset[0]
        assert "image" in sample
        assert "gis" in sample
        assert "label" in sample
        assert "city_name" in sample
        assert sample["image"].shape[0] == 3
        assert sample["gis"].shape[0] == 18

    def test_invalid_split_raises(self, temp_data_dir):
        with pytest.raises(ValueError):
            GCMHAIRNetDataset(root_dir=temp_data_dir, split="invalid")
