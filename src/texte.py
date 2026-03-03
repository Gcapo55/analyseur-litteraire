from collections import Counter

class Texte:
    def __init__(self, titre: str, auteur: str, contenu: str, annee: int):
        self._titre = titre
        self.auteur = auteur
        self.contenu = contenu
        self.annee = annee

    def __str__ (self) -> str:
        return f"{self.titre} ({self.auteur}, {self.annee})"
    
    def __repr__ (self) -> str:
        return f"Texte(titre={self.titre!r}, auteur={self.auteur!r}, année={self.annee})"
    
    def __eq__ (self, other) -> bool:
        if not isinstance(other, Texte):
            return NotImplemented
        return (self.titre == other.titre and self.auteur == other.auteur)
    
    def __lt__ (self, other):
        if not isinstance(other, Texte):
            return NotImplemented
        return self.annee < other.annee

    @property
    def titre(self) -> str:
        return self._titre
    @titre.setter
    def titre(self, nouveau: str) -> None:
        if not nouveau.strip():
            raise ValueError("Le titre est vide, ou il y a des espace au début/à la fin")
        self._titre = nouveau.strip()


    def nombre_mots(self) -> int:
        return sum(len(texte.split()) for texte in self.contenu)

    def mots_uniques(self) -> set[str]: #set -> que les éléments uniques
        cnt = Counter(self.contenu.split())
        mots_unic = []
        for word in cnt:
            if cnt[word] == 1:
                mots_unic.append(word)
        return set(mots_unic)
    
    def frequences(self) -> dict[str, int]:
        cnt = Counter(self.contenu.split())
        return cnt
    

if __name__ == "__main__":
    pass
