import re
from pathlib import Path
from uuid import uuid4

from rag.ingestion.document import Document
from .chunk import Chunk, ChunkMetadata
from .chunker import Chunker


class MarkdownSectionChunker(Chunker):
    """Une section (## ou ###) = un chunk. Les sections longues sont redécoupées
    par mots, avec le titre répété en tête de chaque morceau."""

    def __init__(self, max_words: int = 180, overlap_words: int = 30):
        if max_words <= 0:
            raise ValueError("max_words must be positive")
        if overlap_words < 0 or overlap_words >= max_words:
            raise ValueError("overlap_words must be between 0 and max_words")
        self.max_words = max_words
        self.overlap_words = overlap_words

    def split(self, document: Document) -> list[Chunk]:
        content = document.content
        source = Path(document.metadata.source).stem

        # positions de chaque titre ## ou ###
        starts = [m.start() for m in re.finditer(r"^#{2,3} ", content, re.MULTILINE)]
        if not starts or starts[0] != 0:
            starts.insert(0, 0)  # le texte avant le premier titre forme sa propre section
        starts.append(len(content))

        chunks = []
        for start, end in zip(starts, starts[1:]):
            section = content[start:end].strip()
            if len(section) < 40:  # titre seul, fragment vide
                continue

            title, _, body = section.partition("\n")
            for piece in self._windows(body):
                chunks.append(
                    Chunk(
                        id=str(uuid4()),
                        content=f"{title}\n{piece}".strip(),
                        metadata=ChunkMetadata(
                            document_id=document.id,
                            chunk_index=len(chunks),
                            start_index=start,  # en caractères (pas en tokens)
                            end_index=end,
                            page=document.metadata.page,
                            source=source,
                        ),
                    )
                )
        return chunks

    def _windows(self, body: str) -> list[str]:
        words = body.split()
        if len(words) <= self.max_words:
            return [body.strip()]

        step = self.max_words - self.overlap_words
        windows = []
        for i in range(0, len(words), step):
            windows.append(" ".join(words[i : i + self.max_words]))
            if i + self.max_words >= len(words):  # évite un dernier chunk doublon
                break
        return windows