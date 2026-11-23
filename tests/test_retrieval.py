# tests/test_retrieval.py
import os
from pathlib import Path


from rag.retrieval.retriever import Retriever

MODEL = os.environ["EMBEDDING_MODEL"]
retriever = Retriever(Path(__file__).parent.parent / "rag/embeddings/index", MODEL)  # adapte le chemin à ton arborescence

questions = [
    "Quelles technologies utilises-tu ?",
    "Parle-moi de tes projets",
    "Quelle musique fais-tu ?",
    "Comment te contacter ?",
    "Qui es-tu ?",
    "Quel est ton salaire ?",   # hors sujet : on veut peu ou pas de résultat
    "Quelle est la capitale du Japon ?",
]

for q in questions:
    print(f"\n## {q}")
    for r in retriever.search(q, min_score=0.0):  # seuil à 0 pour voir tous les scores
        print(f"  {r['score']:.2f} [{r['source']}] {r['text'][:70]!r}")