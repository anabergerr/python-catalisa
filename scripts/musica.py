class Musica:
    def __init__(self, titulo, artista, duracao):
        self.titulo = titulo
        self.artista = artista
        self.duracao = duracao

    def __str__(self):
        return f"Nome da musica {self.titulo} - {self.artista}"

    def tocar(self) -> str:
        return f"Tocando {self.titulo}  {self.artista}"

    def __tocar_privado(self):
        print("tocando musica privada")


class MusicaPremium(Musica):
    def __init__(self, titulo, artista, duracao, qualidade):
        super().__init__(titulo, artista, duracao)
        self.qualide = qualidade

    def tocar(self):
        return f"Tocando {self.titulo} de {self.artista} em {self.qualide}"
