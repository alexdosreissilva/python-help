#coding=UTF-8

x = 10

if x >= 0:
    y = 1
else:
    y = -1
print(y)

y = 1 if x >= 0 else -1
print(y)

def f(x):
    return 1 if x >= 0 else -1

print(f(x))
