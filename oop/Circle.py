import math
class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * math.pow(self.radius, 2)
    
    def cirumference(self):
        return 2 * math.pi * self.radius

c1 = Circle(7)

print(c1.area())
print(c1.cirumference())