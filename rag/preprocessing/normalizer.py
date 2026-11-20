
import re
import unicodedata


class TextNormalizer:

    def normalize(self, text: str) -> str:
        # Normalisation Unicode
        text = unicodedata.normalize("NFC", text)

        # Uniformisation des retours à la ligne
        text = text.replace("\r\n", "\n").replace("\r", "\n")

        # Suppression des espaces et tabulations inutiles
        text = re.sub(r"[ \t]+", " ", text)

        # Suppression des espaces en début et fin de ligne
        text = re.sub(r" *\n *", "\n", text)

        # Limitation des lignes vides successives
        text = re.sub(r"\n{3,}", "\n\n", text)

        return text.strip()
