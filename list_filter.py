# coding=UTF-8

lista = [8, 9, -1, -3, 3, -5, -4, 5, -4, 2, 5, 91, -11, 5, 10, 93, -75]
def maior_que_zero(num):
    if num > 0:
        return True
    else:
        return False
lista_valida = filter(maior_que_zero, lista)
print(list(lista_valida))

palavras = ['teste', 'assistente', 'estou', 'aqui', 'onde', 'ouro', 'adeus']
def f(p):
    return p.startswith('a') or p.startswith('e')
print(list(filter(f, palavras)))
