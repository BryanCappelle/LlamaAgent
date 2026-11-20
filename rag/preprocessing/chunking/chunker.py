from abc import ABC, abstractmethod
from rag.ingestion.document import Document
from .chunk import Chunk


class Chunker(ABC):

    @abstractmethod
    def split(self, document: Document) -> list[Chunk]:
        pass