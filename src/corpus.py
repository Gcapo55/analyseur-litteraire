from texte import Texte

class Corpus:
    def __init__(self, nom: str):
        self.nom = nom
        self.textes: list[Texte] = []

    def ajouter(self, texte: Texte) -> None:
        self.textes.append(texte)
    
    def total_mots(self) -> int:
        return sum(l.nombre_mots() for l in self.textes)

    def rechercher(self, mot_cle: str) -> list[Texte]:
        return [l for l in self.textes if mot_cle in l.titre]
    
    def __len__(self)-> int:
        return len(self.textes)
    
    def __getitem__(self, index: int) -> Texte:
        return self.textes[index]
    
    def __contains__(self, titre: str) -> bool:
        return any(t.titre == titre for t in self.textes)
    
    def __iter__(self):
        return iter(self.textes)
    
    def __add__(self, other: "Corpus") -> "Corpus":
        nouveau = Corpus(f"{self.nom} + {other.nom}")
        for t in self.textes:
            nouveau.ajouter(t)
        for t in other.textes:
            nouveau.ajouter(t)
        return nouveau

if __name__ == "__main__":
    t1 = Texte("Texte1", "Moi", "Un texte quelconque oui oui", 2012)
    t2 = Texte("Texte2", "Toi", "contenu vide", 1989)
    t3 = Texte("Texte3", "Nous", "contenu vide très vide", 1909)

    corpus1= Corpus("Corpus 1")
    
    corpus1.ajouter(t1)
    corpus1.ajouter(t2)
    corpus1.ajouter(t3)

    for t in corpus1:
        print(t)