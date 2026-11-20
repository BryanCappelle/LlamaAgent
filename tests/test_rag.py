# tests/test_rag.py
from app.rag import search

questions = [
    "Quelles technologies utilises-tu ?",
    "Parle-moi de tes projets",
    "Quelle musique fais-tu ?",
    "Comment te contacter ?",
    "Qui es-tu ?",
]
for q in questions:
    print(f"\n## {q}")
    for c in search(q):
        print(f"  [{c['source']}] {c['text'][:80]}...")