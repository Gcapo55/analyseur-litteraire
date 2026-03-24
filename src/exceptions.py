"""
Solution Exercice 5 -- Composition, Exceptions & Bonnes Pratiques
"""


class AnalyseurError(Exception):
    """Classe de base pour les erreurs de l'analyseur."""


class TexteVideError(AnalyseurError):
    """Levée quand le contenu d'un texte est vide."""


class FormatInconnuError(AnalyseurError):
    """Levée quand un format d'export n'est pas supporté."""
