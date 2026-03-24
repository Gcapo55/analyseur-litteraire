from texte import Texte


def test_frequences():

    t1 = Texte("Germinal", "Émile Zola", "La mine était noire et profonde", 1885)
    assert t1.frequences() == {
        "la": 1,
        "mine": 1,
        "était": 1,
        "noire": 1,
        "et": 1,
        "profonde": 1,
    }

