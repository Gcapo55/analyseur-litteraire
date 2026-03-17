from texte import Texte

class Corpus:
    def __init__(self, nom: str):
        self.nom = nom
        self._textes = []

    def ajouter(self, texte: Texte):
        self._textes.append(texte)

    def trouver(self, titre: str):
        for texte in self._textes:
            if texte.titre == titre:
                return texte
        return None

    def total_mots(self):
        dictionnaire = {}
        for textes in self._textes:
            dictionnaire[textes.titre] = textes.nombre_mots()
        return dictionnaire
    
if __name__ == "__main__":
    # Création d'un Texte
    bonjour = Texte("Bonjour", "Bonouj", 1856, "Bonjour le monde")
    ciao = Texte("Ciao", "moi", 3483, "ciao tout le monde")

    # Création d'un Corpus
    mon_corpus = Corpus("Test")

    # Ajout du texte
    mon_corpus.ajouter(bonjour)
    mon_corpus.ajouter(ciao)
    print(mon_corpus.trouver("Bonjour"))
