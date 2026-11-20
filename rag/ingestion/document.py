from dataclasses import dataclass
from .document_metadata import DocumentMetadata

@dataclass
class Document:
    id: str
    content: str
    metadata: DocumentMetadata
