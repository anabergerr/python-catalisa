import pytest
from scripts.musica import Musica


def test_tocar_musica():
    musica = Musica("Prata", "pumapjl", 2)
    assert musica.tocar() == "Tocando Prata  pumapjl"
