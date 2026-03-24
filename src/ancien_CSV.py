from corpus import *
from texte import *
from abc import ABC, abstractmethod

# Ancien module (ne pas modifier !)
class LecteurCSV:
    def lire_lignes(self, chemin: str) -> list[dict]:
        import csv
        with open(chemin) as f: 
            return list(csv.DictReader(f))
        
# Notre interface
class ChargeurTextes(ABC):
    @abstractmethod
    def charger(self, source: str) -> list["Texte"]: ...
# L'Adapter : traduit l'ancien vers le nouveau
class AdaptateurCSV(ChargeurTextes):
    def __init__(self, lecteur: LecteurCSV):
        self._lecteur = lecteur
    def charger(self, source: str) -> list["Texte"]:
        return [Texte(l["titre"], l["auteur"], l["texte"])
                for l in self._lecteur.lire_lignes(source)]
    
