class Angle:
    def __init__(self, degree):
        self.degree = degree
    
    def __add__(self, angle): # +
        return Angle(self.degree + angle.degree)
    def __str__(self): # print()
        return 'Degree: ' + str(self.degree)
    
a1 = Angle(30)
a2 = Angle(45)

a3 = a1 + a2

print(a3)