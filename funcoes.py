# coding=UTF-8

def func(x, y):
    return x*y, x+y

mult, soma = func(2, 3)
print(mult)
print(soma)

def func2(x, y):
    return x+y, x-y, x*y, x/y, x%y, "hello"

som, sub, mul, divi, rest, string = func2(3, 3)
print(som)
print(sub)
print(mul)
print(divi)
print(rest)
print(string)
