# coding=UTF-8

class Pilha(object):
    def __init__(self):
        self.dados = []

    def empilha(self, elemento):
        self.dados.append(elemento)

    def desempilha(self):
        return self.dados.pop()

    def vazia(self):
        return len(self.dados) == 0
