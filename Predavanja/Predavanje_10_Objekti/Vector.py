from math import sqrt

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other): #za sestevanje
        return Vector(self.x + other.x, self.y + other.y)

    def __neg__(self): # za negacijo vektorjev
        return Vector(-self.x, -self.y)

    def __sub__(self, other): #za odstevanje
        return self + -other

    def __str__(self): # za default print
        return f"[{self.x}, {self.y}]"

    def __abs__(self):
        return sqrt(self.x ** 2 + self.y ** 2)

a = Vector(3, 6)
b = Vector(6, 10)
c = a + b
print(abs(c))