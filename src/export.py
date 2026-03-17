from collections import Counter

class Document:
    def __init__(self, titre: str, auteur: str, contenu: str, annee: int):
        self.titre = titre
        self.auteur = auteur
        self.contenu = contenu
        self.annee = annee


class Analyser:
    def frequences(self) -> dict[str, int]:
        cnt = Counter(self.contenu.split())
        return cnt
    
class ExporterHTML:
    def export(self):
        return f"<h1>{self.titre}</h1><p>{self.contenu}</p>"

class ExporterCSV:
    def export(self):
        return "\n".join(f"{m},{c}" for m, c in Analyser.frequences(self).items())
    
class Sauvegarder:
    def sauver(self, chemin):
        with open(chemin, "w") as f: f.write(self.txt)

texte = Document("Germinal", "Zola", "Bla bla les mineurs meurent", 1885)

#print(Analyser.frequences(texte))

#print(ExporterHTML.export(texte))

#print(ExporterCSV.export(texte))