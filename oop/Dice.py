import random
class Dice:
    def __init__(self, s):
        self.sides = s
    
    def roll_dice(self):
        return random.randint(1, self.sides)

d1 = Dice(6)
print(d1.roll_dice())

d2 = Dice(12)
print(d2.roll_dice())