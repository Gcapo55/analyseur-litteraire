"""
Solution Exercice 5 -- Composition, Exceptions & Bonnes Pratiques
"""


from exceptions import TexteVideError
from exportateurs import ExportateurCSV, ExportateurHTML
from texte import Texte


class Corpus:
    def __init__(self, nom: str) -> None:
        self._nom = nom
        self._textes: list[Texte] = []

    def ajouter(self, texte: Texte) -> None:
        self._textes.append(texte)

    def total_mots(self) -> int:
        return sum(t.nombre_mots() for t in self._textes)

    def exporter_tout(self, exportateur: ExportateurHTML | ExportateurCSV) -> list[str]:
        """Exporte tous les textes avec l'exportateur donné (composition)."""
        return [exportateur.exporter(t) for t in self._textes]

    def __len__(self) -> int:
        return len(self._textes)

    def __iter__(self):
        return iter(self._textes)


# --- Tests ---
if __name__ == "__main__":
    import pytest

    # Test exception
    try:
        Texte("Vide", "Auteur", "")
    except TexteVideError as e:
        print(f"TexteVideError OK : {e}")

    # Test composition
    t1 = Texte("Germinal", "Zola", "La mine était noire et la mine était profonde")
    corpus = Corpus("XIXe")
    corpus.ajouter(t1)

    print("\n--- HTML ---")
    print(ExportateurHTML().exporter(t1))
    print("\n--- CSV ---")
    print(ExportateurCSV().exporter(t1))
