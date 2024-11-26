def my_pet(pet):
    pet.info()
    pet.make_sound()

class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"Name: {self.name} \n age: {self.age}")
    def make_sound(self):
        print("Meow Meow!")

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def info(self):
        print(f"Name: {self.name} \n age: {self.age}")
    def make_sound(self):
        print("Woow woow!")
    