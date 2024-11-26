import math


class Shape:
    def __init__(self, name):
        self.name = name
    def area():
        pass

class Rectangle(Shape):
    def __init__(self, l , b):
        self.length = l
        self.breadth = b
    def area(self):
        return self.length * self.breadth

class Circle(Shape):
    def __init__(self,r):
        self.radius = r
    def area(self):
        return math.pi * (self.radius ** 2)