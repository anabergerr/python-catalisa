from .musica import Musica

class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = list()

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def tocar_tudo(self):
        return [musica.tocar() for musica in self.musicas]



