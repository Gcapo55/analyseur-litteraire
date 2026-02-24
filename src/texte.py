class Texte:
    def __init__(self, titre: str, auteur: str, annee: int, contenu: str):
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.contenu = contenu
    @property
    def titre(self) -> str :
        return self._titre
    
    @titre.setter
    def titre(self, nouveau: str):
        if nouveau == "":
            raise ValueError("Le nom est vide.")
        self._titre = nouveau
    
    def nombre_mots(self) -> int:
        return len(self.contenu.split())
    def mots_uniques(self) -> set[str]:
        return set(self.contenu.split())
    def frequences(self) -> dict[str, int]:
        freqs = {}
        for mot in self.contenu.split():
            if mot in freqs:
                freqs[mot] += 1
            else:
                freqs[mot] = 1
        return freqs


