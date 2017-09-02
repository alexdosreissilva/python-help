# coding=UTF-8

from string import maketrans

entrada = 'ABTESIOZ'
saida = '48735102'
tabela = maketrans(entrada, saida)
s = raw_input('Digite uma frase para ser convertida para leet:')
print s.translate(tabela)
