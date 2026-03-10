from document import Document

class Corpus:
    def __init__(self, nom: str):
        self.nom = nom
        self.document: list[Document] = []

    def ajouter(self, texte: Document) -> None:
        self.document.append(texte)
    
    def total_mots(self) -> int:
        return sum(l.nombre_mots() for l in self.document)

    def rechercher(self, mot_cle: str) -> list[Document]:
        return [l for l in self.document if mot_cle in l.titre]
    
    def __len__(self)-> int:
        return len(self.document)
    
    def __getitem__(self, index: int) -> Document:
        return self.document[index]
    
    def __contains__(self, titre: str) -> bool:
        return any(t.titre == titre for t in self.document)
    
    def __iter__(self):
        return iter(self.document)
    
    def __add__(self, other: "Corpus") -> "Corpus":
        nouveau = Corpus(f"{self.nom} + {other.nom}")
        for t in self.document:
            nouveau.ajouter(t)
        for t in other.textes:
            nouveau.ajouter(t)
        return nouveau

    def afficher_resumes(self) -> None:
        for doc in self:
            print(f"{doc.titre} : {doc.resume()}")

if __name__ == "__main__":
    pass