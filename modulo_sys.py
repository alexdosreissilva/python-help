# coding=UTF-8

import sys

def erro(msg):
    print("Erro:", msg)
    sys.exit(1)

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def quadrado(x):
    return x ** 2

if __name__ == "__main__":
    print(inc(10))
    print(dec(10))
    print(quadrado(5))
