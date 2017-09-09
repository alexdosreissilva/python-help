# coding=UTF-8

fila = [10, 20, 30, 40, 50]
fila.append(60)
print(fila)
print(fila.pop(0))
print(fila)
print(fila.pop(0))
print(fila)
print(fila.pop(0))
print(fila)

#Pilha
def ola():
    print("Olá, ")
    mundo()

def mundo():
    print("mundo!")

def olamundo():
    ola()

olamundo()
