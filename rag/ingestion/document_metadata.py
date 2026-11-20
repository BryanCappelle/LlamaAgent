from dataclasses import dataclass
from typing import Optional

@dataclass
class DocumentMetadata:
    source: str
    file_type: str
    page: Optional[int] = None