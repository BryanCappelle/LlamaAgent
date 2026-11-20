from rag.ingestion.document_loader import DocumentLoader
from rag.preprocessing.normalizer import TextNormalizer
from rag.preprocessing.chunking.fix_sized_chunker import FixedSizeChunker

loader = DocumentLoader()
normalizer = TextNormalizer()

document = loader.load("content/stack.md")

chunker = FixedSizeChunker(
    chunk_size=50,
    overlap=15
)

chunks = []

for doc in document:
    doc.content = normalizer.normalize(doc.content)
    chunks.extend(chunker.split(doc))

print(f"Nombre de chunks : {len(chunks)}")
print(chunks[0])