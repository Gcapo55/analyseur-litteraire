import pytest
from corpus import Corpus
from texte import Texte
from exportateurs import *
from exceptions import *
from ancien_CSV import *


def test_lire_lignes() -> list[dict]:
    
    assert LecteurCSV().lire_lignes("./tests/ratings.csv")  == [{'Date': '2024-12-18', 'Name': 'All Quiet on the Western Front', 'Year': '2022', 'Letterboxd URI': 'https://boxd.it/H08', 'Rating': '4.5'}, {'Date': '2024-12-18', 'Name': 'Spider-Man: Across the Spider-Verse', 'Year': '2023', 'Letterboxd URI': 'https://boxd.it/kSz4', 'Rating': '4'}, {'Date': '2024-12-18', 'Name': 'The Hateful Eight', 'Year': '2015', 'Letterboxd URI': 'https://boxd.it/8gw8', 'Rating': '3'}, {'Date': '2024-12-18', 'Name': '12 Years a Slave', 'Year': '2013', 'Letterboxd URI': 'https://boxd.it/2D2e', 'Rating': '4'}, {'Date': '2024-12-18', 'Name': 'Zero Fucks Given', 'Year': '2021', 'Letterboxd URI': 'https://boxd.it/vqk8', 'Rating': '5'}, {'Date': '2024-12-18', 'Name': 'Cherry', 'Year': '2021', 'Letterboxd URI': 'https://boxd.it/jRhm', 'Rating': '5'}, {'Date': '2024-12-18', 'Name': 'Interstellar', 'Year': '2014', 'Letterboxd URI': 'https://boxd.it/4VZ8', 'Rating': '4'}, {'Date': '2024-12-18', 'Name': 'The Zone of Interest', 'Year': '2023', 'Letterboxd URI': 'https://boxd.it/gJsA', 'Rating': '4'}, {'Date': '2024-12-18', 'Name': 'The Square', 'Year': '2017', 'Letterboxd URI': 'https://boxd.it/e5YW', 'Rating': '4'}]
