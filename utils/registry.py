from typing import Any, Dict, Optional


class Registry:
    _instances: Dict[str, "Registry"] = {}

    def __init__(self, name: str):
        self.name = name
        self._registry: Dict[str, Any] = {}

    @classmethod
    def get(cls, name: str) -> Optional["Registry"]:
        return cls._instances.get(name)

    @classmethod
    def register(cls, name: str) -> "Registry":
        if name not in cls._instances:
            cls._instances[name] = Registry(name)
        return cls._instances[name]

    def add(self, key: str, value: Any) -> None:
        self._registry[key] = value

    def get_item(self, key: str, default: Any = None) -> Any:
        return self._registry.get(key, default)

    def keys(self) -> list:
        return list(self._registry.keys())

    def __contains__(self, key: str) -> bool:
        return key in self._registry


MODEL_REGISTRY = Registry.register("model")
LOSS_REGISTRY = Registry.register("loss")
METRIC_REGISTRY = Registry.register("metric")
