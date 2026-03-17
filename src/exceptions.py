from corpus import Corpus

class ErreurCorpus(Exception):
    """Exception de base pour les operations sur un corpus."""

class DocumentIntrouvable(ErreurCorpus):
    def __init__(self, titre: str):
        self.titre = titre
        super().__init__(f"Document introuvable : {titre}")

class FormatInconnuError(ErreurCorpus):
    pass

# Utilisation
if __name__ == "__main__":
    from texte import Texte
    bonjour = Texte("Bonjour", "Bonouj", 1856, "Bonjour le monde")
    ciao = Texte("Ciao", "moi", 3483, "ciao tout le monde")

    # Création d'un Corpus
    mon_corpus = Corpus("Test")

    # Ajout du texte
    mon_corpus.ajouter(bonjour)
    mon_corpus.ajouter(ciao)
    try:
        doc = mon_corpus.trouver("Germinal")
    except DocumentIntrouvable as e:
        print(f"Erreur : {e}")
        print(f"Titre cherche : {e.titre}")
    except ErreurCorpus:
        print("Autre erreur de corpus")