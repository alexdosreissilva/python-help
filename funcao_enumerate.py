# coding=UTF-8

l = ['hello', 'world', 'hi', 'earth']

for word in l:
    print(word)

print("")

for i in range(0, len(l)):
    print(l[i])

print("")

i = 0
while i < len(l):
    print(l[i])
    i += 1

print("")

for i, word in enumerate(l):
    print(i, word)

print("")

def posicoesQueIniciamCom(lista, letra='a'):
    result = []
    for i, palavra in enumerate(lista):
        if palavra.startswith(letra):
            result.append(i)
    return result

nomes = ['abc', 'hua', 'aaa', 'asdfg', 'bnm']
print(posicoesQueIniciamCom(nomes))
