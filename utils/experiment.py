import os
from pathlib import Path
from typing import Any, Dict, Optional

import yaml

from .config import Config, merge_configs


class ConfigManager:
    def __init__(self, root_dir: Optional[str] = None):
        self.root_dir = Path(root_dir) if root_dir else Path.cwd()
        self.configs_dir = self.root_dir / "configs"

    def load(self, config_name: str, overrides: Optional[Dict[str, Any]] = None) -> Config:
        config_path = self.configs_dir / f"{config_name}.yaml"
        if not config_path.exists():
            raise FileNotFoundError(f"Config file not found: {config_path}")
        config = Config(config_path=str(config_path))
        if overrides:
            merged = merge_configs(config.to_dict(), overrides)
            config = Config(config_dict=merged)
        return config

    def load_defaults(self, overrides: Optional[Dict[str, Any]] = None) -> Config:
        return self.load("default", overrides)
