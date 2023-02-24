class Filme:
    def __init__(self, nome, ano, duracao):
            self.nome = nome.title()
            self.ano = ano
            self.duracao = duracao
            self.likes = 0
    def dar_like(self):
        self.likes += 1


class Serie:
    def __init__(self, nome, ano, temporadas):
            self.nome = nome.title()
            self.ano = ano
            self.temporadas = temporadas
            self.likes = 0
    def dar_like(self):
        self.likes += 1

vingadores = Filme('Vingadores:Guerra Infinita', 2018, 160)
vingadores.dar_like()
print (f'Nome: {vingadores.nome} - Ano: {vingadores.ano} - Duração: {vingadores.duracao} minutos. - Likes: {vingadores.likes}')


Atlanta = Serie('Atlanta', 2018, 2)
Atlanta.dar_like()
Atlanta.dar_like()
print(f'Nome: {Atlanta.nome} - Ano: {Atlanta.ano} - Temporadas: {Atlanta.temporadas} - Likes {Atlanta.likes}')