# coding=UTF-8

from string import maketrans

entrada = 'abcdefghijklmnopqrstuvwxyz'
saida = 'cdefghijklmnopqrstuvwxyzab'

def cifra_de_cesar(texto):
    tabela = maketrans(entrada, saida)
    return texto.translate(tabela)

print cifra_de_cesar('hello world')
