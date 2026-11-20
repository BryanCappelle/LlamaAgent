from ..document import Document
from .document_parser import DocumentParser
from ..document_metadata import DocumentMetadata
from pathlib import Path
from uuid import uuid4
class TextParser(DocumentParser):

    def parse(self, path: Path) -> list[Document]:
        content = path.read_text(encoding="utf-8")

        return [
            Document(
                id=uuid4(),
                content=content.strip(),
                metadata= DocumentMetadata(
                    path.name,
                    path.suffix[1:]
                )
            )
        ]