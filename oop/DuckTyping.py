def PetLover(pet):
    pet.talk()
    if hasattr(pet, 'walk'):
        pet.walk()

class Duck:
    def talk(self):
        print("Duck is Talking")
    def walk(self):
        print("Duck is Walking")
        

class Dog:
    def talk(self):
        print("Dog is Talking")
    def walk(self):
        print("Dog is Walking")

class Cat:
    def talk(self):
        print("Cat is Talking")


d = Duck()
PetLover(d)

c = Cat()
PetLover(c)