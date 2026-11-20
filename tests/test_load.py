
from rag.ingestion.document_loader import DocumentLoader
loader = DocumentLoader()

documents = loader.load("content/contact.md")

for document in documents:
    print(document.content)
    print(document.metadata)