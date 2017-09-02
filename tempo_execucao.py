# coding=UTF-8

import timeit

def soma1(x, y):
    return sum(range(x, y+1))

def soma2(x, y):
    soma = 0
    for i in range(x, y+1):
        soma += i
    return soma

t = timeit.Timer("soma1(1, 1000)", "from __main__ import soma1")
print(t.repeat())

t = timeit.Timer("soma2(1, 1000)", "from __main__ import soma2")
print(t.repeat())
