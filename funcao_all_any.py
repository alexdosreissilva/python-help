# coding=UTF-8

import math
import operator

lista = [2, 6, 4, 7, -2]

if all(i % 2 == 0 for i in lista):
    print("Todos são pares.")
else:
    print("Tem algum impar.")

print("")

if not any(i <= 0 for i in lista ):
    print("Todos são positivos.")
else:
    print("Tem algum negativo.")

print("")

lista1 = [1, 4, 9, 16, 25]
lista2 = map(math.sqrt, lista1)
print(list(lista2))

print("")

print(any(map(operator.eq, [1, 2, 3, 4, 5], [1, 4, 2, 3, 5])))
