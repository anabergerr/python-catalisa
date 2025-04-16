from musica import Musica


class Playlist:
    def __init__(self, nome):
        self.nome = nome
        self.musicas = list()

    def adicionar_musica(self, musica):
        self.musicas.append(musica)

    def tocar_tudo(self):
        return [musica.tocar() for musica in self.musicas]


minha_playlist = Playlist("Musicas para relaxar")

m1 = Musica("Coracao Pirata", "Roupa Nova", 5)
m2 = Musica("Projecao", "Mc Luanna", 2)

minha_playlist.adicionar_musica(m1)
minha_playlist.adicionar_musica(m2)

print(minha_playlist.tocar_tudo())
