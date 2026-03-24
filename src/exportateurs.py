"""
Solution Exercice 5 -- Composition, Exceptions & Bonnes Pratiques
"""


from texte import Texte


class ExportateurHTML:
    """Exporte un texte au format HTML."""

    def exporter(self, texte: Texte) -> str:
        freq = texte.frequences()
        top10 = sorted(freq.items(), key=lambda x: -x[1])[:10]
        items = "".join(f"  <li>{mot}: {count}</li>\n" for mot, count in top10)
        return (
            f"<h1>{texte.titre}</h1>\n"
            f"<p><em>{texte.auteur}</em></p>\n"
            f"<p>{texte.contenu[:200]}...</p>\n"
            f"<h2>Fréquences</h2>\n<ul>\n{items}</ul>"
        )


class ExportateurCSV:
    """Exporte les fréquences au format CSV."""

    def exporter(self, texte: Texte) -> str:
        lignes = ["mot,frequence"]
        for mot, count in sorted(texte.frequences().items(), key=lambda x: -x[1]):
            lignes.append(f"{mot},{count}")
        return "\n".join(lignes)

