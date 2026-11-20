from dataclasses import dataclass
from typing import Optional

@dataclass
class ChunkMetadata:
    document_id: str
    chunk_index: int
    start_index: int
    end_index: int
    page: Optional[int] = None
    source: Optional[str] = None