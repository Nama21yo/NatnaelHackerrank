import math


class Polygon:
    def __init__(self, no_of_sides, *sides):
        self.no_of_sides = no_of_sides
        self.sides =  sides[:no_of_sides]

class Triangle(Polygon):
    def __init__(self, no_of_sides, *sides):
        super().__init__(self, no_of_sides, *sides)
    

    def area(self):
        a, b ,c = self.sides
        s = sum(self.sides) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))