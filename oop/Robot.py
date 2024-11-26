class Robot:
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print("Hi! I am a Robot")

class PoliceRobot(Robot):
    # It will go to the upper init  
    def say_hi(self):
        print(f"Hi! I am {self.name}. I am a Police Robot")

          