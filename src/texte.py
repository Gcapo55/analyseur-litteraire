"""
Solution Exercice 5 -- Composition, Exceptions & Bonnes Pratiques
"""

from __future__ import annotations

from collections import Counter

from exceptions import TexteVideError


class Texte:
    def __init__(self, titre: str, auteur: str, contenu: str, annee: int = 0) -> None:
        if not contenu or not contenu.strip():
            raise TexteVideError(f"Le texte '{titre}' a un contenu vide.")
        self._titre = titre
        self._auteur = auteur
        self._contenu = contenu
        self._annee = annee

    @property
    def titre(self) -> str:
        return self._titre

    @property
    def auteur(self) -> str:
        return self._auteur

    @property
    def contenu(self) -> str:
        return self._contenu

    def nombre_mots(self) -> int:
        return len(self._contenu.split())

    def frequences(self) -> dict[str, int]:
        return dict(Counter(self._contenu.lower().split()))

    def __str__(self) -> str:
        return f"{self._titre} ({self._auteur}, {self._annee})"
