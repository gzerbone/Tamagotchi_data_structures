import os
from array import array
from random import randint

from numpy import bool_

from Binary_tree import *
from quicksort import QuickSort
from spritess import *

#from Stack import *


class Tamagotchi():
    def __init__(self, nome: str = None, personagem: int = None):
        # Composição de classes
        if personagem == 1:
            self.virtual_pet = Febrix()
        elif personagem == 2:
            self.virtual_pet = Fantasminha()
        elif personagem == 3:
            self.virtual_pet = Pacman()

        self.__personagem = personagem
        self.__nome = nome
        self.__level = 0
        self.__xp = 0
        self.__alimentacao = 30
        self.__felicidade = 90
        self.__saude = 90
        self.__higiene = 90
        self.__energia = 90

    @property
    def personagem(self):
        return self.__personagem

    @property
    def nome(self):
        return self.__nome

    @property
    def level(self):
        return self.__level

    @property
    def alimentacao(self):
        return self.__alimentacao

    @property
    def felicidade(self):
        return self.__felicidade

    @property
    def saude(self):
        return self.__saude

    @property
    def higiene(self):
        return self.__higiene

    @property
    def energia(self):
        return self.__energia

    @property
    def xp(self):
        return self.__xp

    '''
    Tal função abre o arquivo para leitura, verifica os atributos que estão salvos e coloca-os em seus respectivos lugares.
    Vale ressaltar que foi-se usado funções nativas de bibliotecas do python que, nesse caso, retornam listas.
    '''

    def setterDados(self) -> None:

        arquivo = open("bancoDados.dat", "r")
        conteudo = arquivo.read()
        # armazena o conteudo na variavel self.listaConteudo e retorna uma lista(str) dividida pelo separador -
        listaConteudo = conteudo.split('-')

        self.__personagem = int(listaConteudo[0])
        self.__nome = str(listaConteudo[1])
        self.__level = int(listaConteudo[2])
        self.__xp = int(listaConteudo[3])
        self.__alimentacao = int(listaConteudo[4])
        self.__felicidade = int(listaConteudo[5])
        self.__saude = int(listaConteudo[6])
        self.__higiene = int(listaConteudo[7])
        self.__energia = int(listaConteudo[8])
        arquivo.close()

    '''
    A função salvarDados() tem como objetivo armazenar os dados no arquivo "dado.dat" num formato específico. 

    EX do formato impresso no arquivo:
    Personagem@NomeDoPersonagem@nível@Qtdd_xp@Alimentação@Felicidade@Saude@Higiene@Energia

    Os "@" serviram para dividir cada item da "self.listaConteudo[]"
    '''

    def salvarDados(self):
        arquivo = open("bancoDados.dat", "w")
        tree = Arvore_Binaria()

        self.n1 = Node(self.__personagem)
        self.n2 = Node(self.__nome)
        self.n3 = Node(self.__level)
        self.n4 = Node(self.__xp)
        self.n5 = Node(self.__alimentacao)
        self.n6 = Node(self.__felicidade)
        self.n7 = Node(self.__saude)
        self.n8 = Node(self.__higiene)
        self.n9 = Node(self.__energia)

        vet = [self.n1, self.n2, self.n3, self.n4,
               self.n5, self.n6, self.n7, self.n8, self.n9]

        for i in vet:
            tree.tree_in_order(i, arquivo)

        arquivo.close()

    '''
    Função que aumentará o XP do jogador e, consequentemente, seu level(definido como MAX = 10). O limite do Xp é 100 e
    a cada vez que for atingido, sobe 1 unidade no level e retorna a 0 xp, prosseguindo o ciclo.
    '''

    def subirXP(self) -> None:
        limite = 100
        level_max = 10
        if self.level < level_max:  # verifica se o level atual é menor que o level 10, para não deixar ultrapassar
            self.__xp += 25
            if self.__xp >= limite:
                self.__level += 1
                self.__xp = 0

    """
    A função verificaEstadoAtual() retorna False se algum dos seus "estados de saúde" forem zerados
    """

    def verificarVida(self) -> bool:
        if (self.__alimentacao <= 0) or (self.__felicidade <= 0) or (self.__saude <= 0) or (self.__higiene <= 0) or (self.__energia <= 0):
            return False  # caso algum dos atributos tenha zerado, retorna false
        else:
            return True

    """
    Função que auxilia no controle da alimentação do personagem
    """

    def alimentar(self) -> None:
        if self.alimentacao == 90:
            print(f'{self.nome} não está com fome')
        else:
            self.alteraAtributos('alimentacao')
            self.subirXP()

    """
    Função que auxilia no controle da felicidade do personagem
    """

    def brincar(self) -> None:
        if self.felicidade == 90:
            print(f'{self.nome} ja brincou demais por hoje, tente mais tarde!')
        else:
            self.alteraAtributos('felicidade')
            self.subirXP()

    """
    Função que auxilia no controle de saúde do personagem
    """

    def curar(self) -> None:
        if self.saude >= 70:
            print(f'{self.nome} não precisa de medicamentos, ele está saudável')
        else:
            self.alteraAtributos('saude')
            self.subirXP()

    """
    Função que auxilia no controle da higiene do personagem
    """

    def limpar(self) -> None:
        if self.higiene >= 75:
            print(f'{self.nome} já está limpo, poupe a água do planeta! :)')
        else:
            self.alteraAtributos('higiene')
            self.subirXP()

    """
    Função que auxilia no controle dq energia do personagem
    """

    def dormir(self) -> None:
        if self.energia >= 80:
            print(f'{self.nome} não está com sono, aproveite-o e entretenha-o!')
        else:
            self.alteraAtributos('energia')
            self.subirXP()

    '''
    Função para apagar dados do arquivo e reinicia-lo, como se tivesse morrido realmente
    '''

    def morrer(self) -> None:
        arquivo = open("bancoDados.dat", "w")
        arquivo.close()
        exit('Game-Over, Jogador!')

    '''
    Tal função recebe uma string com um dos respectivos atributos a serem alterados[alimentaçao, felicidade, saude, higiene ou energia]
    e inicialmente irá fazer algumas verificações. 1°: Verá se o Tamagotchi atingiu algum atributo == 0, significando
    que ele tem de morrer. 2°:Caso ele permaneça vivo, verificará se o atributo está superior a 100 e, caso isso ocorra, a função não permitirá 
    que o atributo ultrapasse de 100. Por fim, se não entrar nessa condição, diminuirá/aumentará as variáveis dos estado de acordo com a ação.
    '''

    def alteraAtributos(self, atributo: str) -> None:
        if atributo == 'alimentacao':
            if self.verificarVida() == False:
                self.morrer()
            elif self.alimentacao >= 90:
                self.alimentacao == 90
            else:
                print(f'{self.nome} está se alimentando...')
                self.__alimentacao += 10
                self.__energia -= 20
                self.__higiene -= 30
                self.__saude -= 10

        elif atributo == 'felicidade':
            if self.verificarVida() == False:
                self.morrer()
            elif self.felicidade >= 90:
                self.felicidade == 90
            else:
                print(f'{self.nome} está se divertindo muito nesse momento!')
                self.__felicidade += 10
                self.__saude -= 10
                self.__energia -= 20
                self.__higiene -= 20

        elif atributo == 'saude':
            if self.verificarVida() == False:
                self.morrer()
            elif self.saude >= 90:
                self.saude == 90
            else:
                print(
                    f'É sempre bom cuidar de quem você ama, {self.nome} está sendo medicado')
                self.__saude += 10
                self.__alimentacao -= 10
                self.__energia += 5

        elif atributo == 'higiene':
            if self.verificarVida() == False:
                self.morrer()
            elif self.higiene >= 90:
                self.higiene == 90
            else:
                print('Hora do Banho! Elimine todos os germes existentes.')
                self.__higiene = 80
                self.__alimentacao -= 5
                self.__energia -= 20

        elif atributo == 'energia':
            if self.verificarVida() == False:
                self.morrer()
            elif self.energia >= 90:
                self.energia == 90
            else:
                print(f'Shhhhh... {self.nome} está dormindo, faça silêncio!')
                self.__energia = 90
                self.__felicidade -= 30
                self.__alimentacao -= 30

    '''
    Função que será chamada para mostrar ao usuário, todos os dados, até então, de seu progresso no game.
    '''

    def imprimirDados(self):

        ListaAtributos = [self.alimentacao, self.felicidade,
                          self.saude, self.higiene, self.energia]

        ListaStrings = ["{}%-ALIMENTAÇÃO".format(ListaAtributos[0]),
                        "{}% - FELICIDADE".format(ListaAtributos[1]),
                        "{}%-SAÚDE".format(ListaAtributos[2]),
                        "{}%-HIGIENE".format(ListaAtributos[3]),
                        "{}% - ENERGIA".format(ListaAtributos[4])]

        for i in range(5):
            QuickSort(ListaAtributos)
            QuickSort(ListaStrings)

        print(ListaStrings)

    """
    Função que auxilia o menu de ações localizado na "main.py", na qual imprime o personagem escolhido e interaje com ele.
    """

    def eventos(self, opcao=0) -> None:
        if opcao == 1:
            self.virtual_pet.imprimeAcao(opcao)
            self.alimentar()
            self.imprimirDados()
        elif opcao == 2:
            self.virtual_pet.imprimeAcao(opcao)
            self.brincar()
            self.imprimirDados()
        elif opcao == 3:
            self.virtual_pet.imprimeAcao(opcao)
            self.curar()
            self.imprimirDados()
        elif opcao == 4:
            self.virtual_pet.imprimeAcao(opcao)
            self.limpar()
            self.imprimirDados()
        elif opcao == 5:
            self.virtual_pet.imprimeAcao(opcao)
            self.dormir()
            self.imprimirDados()
        elif opcao == 0:
            exit('Programa Finalizado com sucesso!')


if __name__ == "__main__":
    aux = Tamagotchi('joao', 3)
    #new = Arvore_Binaria()
    # new.teste()
    aux.salvarDados()
    aux.imprimirDados()
