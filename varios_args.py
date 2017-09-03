# coding=UTF-8

def func(x, *args):
    print(x)
    print(args)

func(1, 2, 3, 4, 5)

def soma(*args):
    result = 0
    for elem in args:
        result += elem
    return result

print(soma(1, 2, 3, 4, 5))

def func2(a, b, c, d):
    print(a, b)

l = [1, 2, 3, 4]
func2(*l)
