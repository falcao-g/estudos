class Programa:
    def __init__(self, nome, ano):
        #usa-se somente um _ para atributos privados, pois por convenção esse atributo não pode ser acessado fora da classe
        #o atributo privado de "verdade" seria com dois _, mas isso faz o name mangling que pode atrabalhar com o código
        #pois nesse exemplo o atributo nome ficaria _Programa__nome
        self._nome = nome.title()
        self._likes = 0

        self.ano = ano

    #define um getter para os likes, usando property, para que o resto do código não precise mudar
    @property
    def likes(self):
        return self._likes

    #unica forma de modificar o atributo likes
    def dar_like(self):
        self._likes += 1

    #define um getter para o nome, usando property, para que o resto do código não precise mudar
    @property
    def nome(self):
        return self._nome

    #define um setter para o nome, garantindo que sempre o nome seja titulizado
    @nome.setter
    def nome(self, novo_nome):
        self.__nome = novo_nome.title()

    #representação textual da classe, o que aparecerá quando usar o print
    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.likes} Likes'

#Classe Filme e Série herdam os atributos, propriedades e métodos da classe Programa
class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        #chamamos o inicializados da classe mãe, para não precisarmos definir os valores genéricos em todas as classes filhas, só os especifícos
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.duracao} min - {self.likes} Likes'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self.nome} - {self.ano} - {self.temporadas} temporadas - {self.likes} Likes'

class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    #duck typing, usamos o método getitem para a classe poder ser iterada e o len para podermos usar o len(), isso faz com que
    #tenhamos vantagens da lista sem ter que herdar a classe, o que traria metodos e propriedades que não precisamos
    def __getitem__(self, item):
        return self._programas[item]

    def __len__(self):
        return len(self._programas)

    @property
    def listagem(self):
        return self._programas

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('Todo mundo em pânico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)

vingadores.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()

filmes_e_series = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

print(f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

#polimorfismo, como a classe filha herda os atributos e métodos da classe mãe,
#podemos usar o mesmo método para acessar os atributos e métodos da classe mãe e
#caso definimos um método específico para a classe filha, ele será executado
#e não o da classe mãe
for programa in playlist_fim_de_semana:
    print(programa)