from node import Node

#from spritess import *


class Arvore_Binaria:
    def __init__(self, dado=None):
        node = Node(dado)
        self.root = node            # raiz vai ser o dado

    # percorre a esquerda -> visita a raiz -> percorre a direita
    def tree_in_order(self, node=None, arquivo=None):
        if node is None:
            node = self.root        # o nó será a raiz (BASE)

        if node.left:               # se nao for vazio
            self.tree_in_order(node.left)

        arquivo.write(str(node))
        arquivo.write('-')

        if node.right:
            self.tree_in_order(node.right)
