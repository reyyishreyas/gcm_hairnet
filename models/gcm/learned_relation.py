import torch
import torch.nn as nn
import torch.nn.functional as F


class LearnedRelation(nn.Module):
    def __init__(self, embed_dim: int = 512, rank: int = 64, eps: float = 1e-8):
        super().__init__()
        self.rank = rank
        self.eps = eps
        self.relation_encoder = self._build_encoder(embed_dim)

    def _build_encoder(self, embed_dim: int):
        return nn.Sequential(
            nn.Linear(embed_dim, embed_dim),
            nn.ReLU(),
            nn.Linear(embed_dim, embed_dim // 2),
            nn.ReLU(),
            nn.Linear(embed_dim // 2, embed_dim // 4),
            nn.ReLU(),
            nn.Linear(embed_dim // 4, self.rank),
        )

    def forward(self, tokens: torch.Tensor) -> torch.Tensor:
        actual_dim = tokens.shape[-1]
        if self.relation_encoder[0].in_features != actual_dim:
            self.relation_encoder = self._build_encoder(actual_dim).to(tokens.device)
            self.reset_relu_flags = True
        E = self.relation_encoder(tokens)
        E = F.normalize(E, dim=-1, eps=self.eps)
        L = torch.bmm(E, E.transpose(1, 2))
        L = L / (L.max(dim=-1, keepdim=True)[0] + self.eps)
        return L
