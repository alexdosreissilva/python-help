# coding=UTF-8

import math

try:
    n = input("Informe um numero: ")
    print(math.sqrt(int(n)))
except ValueError:
    print("Atenção! Não é possível calcular a raiz quadrada de um número negativo!")

