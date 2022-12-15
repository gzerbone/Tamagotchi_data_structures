class Node:
    def __init__(self, dado=None):
        self.dado = dado
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.dado)
