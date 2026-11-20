import tiktoken
from uuid import uuid4

from pathlib import Path
from rag.ingestion.document import Document
from .chunk import Chunk, ChunkMetadata
from .chunker import Chunker


class FixedSizeChunker(Chunker):

    def __init__(self, chunk_size: int = 500, overlap: int = 75):
        if chunk_size <= 0:
            raise ValueError("chunk_size must be positive")

        if overlap < 0 or overlap >= chunk_size:
            raise ValueError("overlap must be between 0 and chunk_size")

        self.chunk_size = chunk_size
        self.overlap = overlap
        self.tokenizer = tiktoken.get_encoding("cl100k_base")

    def split(self, document: Document) -> list[Chunk]:

        tokens = self.tokenizer.encode(document.content)

        chunks = []
        step = self.chunk_size - self.overlap

        for index, start in enumerate(range(0, len(tokens), step)):

            end = min(start + self.chunk_size, len(tokens))

            chunk_content = self.tokenizer.decode(tokens[start:end])

            chunks.append(
                Chunk(
                    id=str(uuid4()),
                    content=chunk_content,
                    metadata=ChunkMetadata(
                        document_id=document.id,
                        chunk_index=index,
                        start_index=start,
                        end_index=end,
                        page=document.metadata.page,
                        source=Path(document.metadata.name).stem
                    )
                )
            )

        return chunks