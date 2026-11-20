from abc import ABC, abstractmethod
from pathlib import Path
from ..document import Document
class DocumentParser(ABC):

    @abstractmethod
    def parse(self, path: Path) -> list[Document]:
        pass