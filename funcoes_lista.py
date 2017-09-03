# coding=UTF-8

from functools import reduce
import operator
import math

lista1 = [1, 4, 9, 16, 25]

lista2 = map(math.sqrt, lista1)
print(list(lista2))

print("")

lista2 = [math.sqrt(x) for x in lista1]
print(lista2)

print("")

valores = [1, 2, 3, 4, 5]
soma = reduce(operator.add, valores)
print(soma)

print("")

print(sum(valores))

print("")

def maior_que_zero(x):
    return x > 0

valores = [10, 4, -1, 3, 5, -9, -11]
print(list(filter(maior_que_zero, valores)))

print("")

print([x for x in valores if x > 0])

print("")

valores = [10, 4, -1, 3, 5, -9, -11]
print(list(filter(lambda x: x > 0, valores)))

print("")

valores = [1, 2, 3, 4, 5]
soma = reduce(lambda x, y: x + y, valores)
print(soma)
