# coding=UTF-8

class Ponto(object):
    def __init__(self, x, y):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        if x > 0:
            self.__x = x

    def set_y(self, y):
        if y > 0:
            self.__y = y

    x = property(fget=get_x, fset=set_x)
    y = property(fget=get_y, fset=set_y)

p = Ponto(2, 3)
#print(p.__x)

#print(p._Ponto__x)
#print(p._Ponto__y)

#print(p.get_x())
#p.set_x(10)

p.x = -1000
print(p.x)
print(p.y)
