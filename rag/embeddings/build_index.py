import json
import re
from pathlib import Path

import numpy as np
from fastembed import TextEmbedding
from dataclasses import asdict
from rag.ingestion.document_loader import DocumentLoader
from rag.preprocessing.normalizer import TextNormalizer
from rag.preprocessing.chunking.markdown_section_chunker import MarkdownSectionChunker


MODEL = "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"

ROOT = Path(__file__).parent.parent.parent       # racine du projet (LlamaAgent/)
CONTENT_DIR = ROOT / "content"               # tes fichiers .md
INDEX_DIR = Path(__file__).parent / "index"  # embedding/index/ (généré)



loader = DocumentLoader()
normalizer = TextNormalizer()
chunker = MarkdownSectionChunker(100, 20)

def main():
    chunks = []
    for doc in loader.load(CONTENT_DIR):
        doc.content = normalizer.normalize(doc.content)
        for chunk in chunker.split(doc):
            chunks.append(chunk)

    if not chunks:
        raise SystemExit(f"Aucun extrait trouvé dans {CONTENT_DIR}")

    model = TextEmbedding(MODEL)
    vectors = np.array(
        list(model.embed([c.content for c in chunks])),
        dtype=np.float32,
    )
    # Normalisation : le produit scalaire devient alors égal à la similarité cosinus
    vectors /= np.linalg.norm(vectors, axis=1, keepdims=True)

    INDEX_DIR.mkdir(exist_ok=True)
    np.save(INDEX_DIR / "vectors.npy", vectors)
    (INDEX_DIR / "chunks.json").write_text(
        json.dumps([asdict(c) for c in chunks], ensure_ascii=False, indent=2, default=str),
        encoding="utf-8"
    )
    print(f"{len(chunks)} extraits indexés, dimension {vectors.shape[1]}")


if __name__ == "__main__":
    main()