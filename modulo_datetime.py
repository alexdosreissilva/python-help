# coding=UTF-8

from datetime import date

hj = date.today()
print(hj)
print(hj.day)
print(hj.month)
print(hj.year)

print("")

futuro = date.fromordinal(hj.toordinal() + 7)
print(futuro)

print("")

diferenca = futuro - hj
print(diferenca.days)

print("")

dias = ('Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo')
print("Hoje é", dias[hj.weekday()])
