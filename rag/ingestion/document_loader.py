from .document import Document
from .parsers import *
from pathlib import Path

class DocumentLoader:

    def __init__(self):
        self.parsers = {
            ".txt": TextParser(),
            ".md": TextParser()
        }

    def load(self, path: str) -> list[Document]:
        file_path = Path(path)

        if file_path.is_dir():
            print("DIR")
            return self._load_directory(file_path)
        
        if not file_path.exists():
            raise FileNotFoundError(path)

        return self._load_file(file_path)

    def _load_file(self, file_path: Path) -> list[Document]:
        parser = self.parsers.get(file_path.suffix.lower())

        if parser is None:
            raise ValueError(f"Unsupported file format: {file_path.suffix}")

        return parser.parse(file_path)

    def _load_directory(self, directory: Path) -> list[Document]:
        documents = []
        for file_path in sorted(directory.glob("*")):  # glob("*") : un seul niveau
            if file_path.is_file() and file_path.suffix.lower() in self.parsers:
                documents.extend(self._load_file(file_path))
        return documents