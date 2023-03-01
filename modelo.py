#classe mãe
class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    def __str__(self):
        return f'Nome: {self.nome} Likes: {self.likes}'

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def imprime(self):
        print(f'{self._nome} - {self.ano}- {self._likes} likes')

#classe filha herdando nome e ano e criando o atributo duração
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self.nome} - {self.duracao} min - Likes: {self.likes}'

    #sobrescrevendo o metodo imprime
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.duracao} min - {self._likes} likes')

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self.nome} - {self.temporadas} temporadas - Likes: {self.likes}'

    #sobrescrevendo o metodo imprime
    def imprime(self):
        print(f'{self._nome} - {self.ano} - {self.temporadas} temporadas - {self._likes} likes')

class Playlist(list):
    def __init__(self, nome, programas):
        self.nome = nome
        super().__init__(programas)



#criando objeto
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('demolidor', 2016, 2)


#criando objeto
vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
#'dando' likes p/ teste
atlanta.dar_likes()
vingadores.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
#criando lista
filmes_e_series= [vingadores, atlanta, demolidor, tmep]

pl_fim_de_semana = Playlist('Fim de Semana', filmes_e_series)



print(f'Tamanho do Playlist: {len(pl_fim_de_semana)}')

#procura na lista pl_fim_de_semana se dentro de cada objeto há o atributo 'duracao'
for programa in pl_fim_de_semana:
    print(programa)