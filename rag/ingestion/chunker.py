class Chunker:

    def __init__(self, chunk_size=500, overlap=75):
        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(self, document: Document) -> list[Document]:
        # Découpage du contenu
        # Conservation des métadonnées
        # Génération des chunks
        pass