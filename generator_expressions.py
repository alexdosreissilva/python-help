# coding=UTF-8

lista = (x**2 for x in range(1, 1000001))
print(lista)

#lista_02 = [x**2 for x in range(1, 1000001)]
#print(lista_02)

print("")

# Generator
def eh_primo(n):
    qtd_divisores = 0
    diviso = 1
    while diviso <= n:
        if n % diviso == 0:
            qtd_divisores += 1
        diviso += 1

    if qtd_divisores == 2:
        return True
    else:
        return False

def primos(n):
    lista = []
    i = 0
    while len(lista) < n:
        if eh_primo(i):
            lista.append(i)
        i += 1
    return lista

#for i in primos(1000):
#    print(i,)

def primos_gen(n):
    i = 1
    count = 0
    while count < n:
        if eh_primo(i):
            count += 1
            yield i
        i += 1

x = primos_gen(100)
print(type(x))

print(x.__next__())
print(x.__next__())
print(x.__next__())
print(x.__next__())

print("")

def func():
    yield 1
    yield 2
    yield 3
x = func()
print(x.__next__())
print(x.__next__())
print(x.__next__())

print("")

for i in func():
    print(i)
