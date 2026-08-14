from pathlib import Path
from typing import Any, Dict, List, Optional


class ExperimentManager:
    def __init__(self, config: Any, root_dir: str = "./outputs"):
        self.config = config
        self.root_dir = root_dir
        self.experiment_name = config.get("experiment", {}).get("name", "experiment")
        self.run_dir = self._create_run_dir()

    def _create_run_dir(self) -> str:
        import datetime
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        run_name = f"{self.experiment_name}_{timestamp}"
        run_dir = str(Path(self.root_dir) / run_name)
        return run_dir

    def get_output_dir(self, subdir: str = "") -> str:
        output_dir = Path(self.run_dir) / subdir
        output_dir.mkdir(parents=True, exist_ok=True)
        return str(output_dir)

    def save_config(self, config: Dict[str, Any]) -> str:
        import yaml
        config_path = Path(self.run_dir) / "config.yaml"
        with open(config_path, "w") as f:
            yaml.dump(config, f, default_flow_style=False, sort_keys=False)
        return str(config_path)

    def log_metric(self, name: str, value: float, step: int) -> None:
        import json
        metrics_file = Path(self.run_dir) / "metrics.json"
        metrics = {}
        if metrics_file.exists():
            with open(metrics_file, "r") as f:
                metrics = json.load(f)
        if name not in metrics:
            metrics[name] = []
        metrics[name].append({"step": step, "value": value})
        with open(metrics_file, "w") as f:
            json.dump(metrics, f, indent=2)
