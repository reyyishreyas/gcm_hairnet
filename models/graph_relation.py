from typing import Dict

import torch
import torch.nn as nn


class GraphRelationModule(nn.Module):
    def __init__(self, config: Dict):
        super().__init__()
        self.hidden_dim = config.get("hidden_dim", 128)
        self.num_relations = config.get("num_relations", 4)
        self.num_layers = config.get("num_layers", 3)
        self.dropout = config.get("dropout", 0.1)

        self.relation_embeddings = nn.Embedding(self.num_relations, self.hidden_dim)
        self.layers = nn.ModuleList()
        for _ in range(self.num_layers):
            self.layers.append(
                nn.ModuleList(
                    [
                        nn.Linear(self.hidden_dim, self.hidden_dim),
                        nn.LayerNorm(self.hidden_dim),
                        nn.Dropout(self.dropout),
                    ]
                )
            )
        self.norm = nn.LayerNorm(self.hidden_dim)

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        if x.shape[-1] != self.hidden_dim:
            raise ValueError(
                f"GraphRelationModule expected input with {self.hidden_dim} features, "
                f"but got tensor with {x.shape[-1]} features."
            )
        for proj, norm, drop in self.layers:
            rel_weights = torch.softmax(
                torch.matmul(x, self.relation_embeddings.weight.T), dim=-1
            )
            rel_messages = torch.matmul(rel_weights, self.relation_embeddings.weight)
            h = proj(x + rel_messages)
            h = torch.nn.functional.relu(h)
            h = drop(h)
            x = norm(x + h)
        return self.norm(x)

    def get_intermediate_features(self, x: torch.Tensor) -> Dict[str, torch.Tensor]:
        features = {"grm_input": x}
        features["grm_output"] = self.forward(x)
        return features
