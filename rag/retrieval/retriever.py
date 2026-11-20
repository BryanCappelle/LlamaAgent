import json
from pathlib import Path

import numpy as np
from fastembed import TextEmbedding

from rag.preprocessing.normalizer import TextNormalizer


class Retriever:
    def __init__(self, index_dir: Path, model_name: str):
        self.chunks = json.loads((index_dir / "chunks.json").read_text(encoding="utf-8"))
        self.vectors = np.load(index_dir / "vectors.npy")
        if len(self.chunks) != len(self.vectors):
            raise ValueError("Index incohérent : relance la construction")
        self.model = TextEmbedding(model_name)
        self.normalizer = TextNormalizer()  # même nettoyage que pour les documents

    def search(self, query: str, k: int = 3, min_score: float = 0.3) -> list[dict]:
        q = np.array(list(self.model.embed([self.normalizer.normalize(query)]))[0], dtype=np.float32)
        q /= np.linalg.norm(q)
        scores = self.vectors @ q
        top = np.argsort(scores)[::-1][:k]
        return [
            {"text": self.chunks[i]["content"], "source": self.chunks[i]["metadata"].get("source"), "score": float(scores[i])}
            for i in top
            if scores[i] >= min_score
        ]