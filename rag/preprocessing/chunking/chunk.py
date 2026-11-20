from dataclasses import dataclass
from typing import Any
from .chunk_metadata import ChunkMetadata
@dataclass
class Chunk:
    id: str
    content: str
    metadata: ChunkMetadata

    @property
    def size(self) -> int:
        return len(self.content)
