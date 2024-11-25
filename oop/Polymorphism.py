def Driver(car):
    car.drive()

class Nissan:
    def drive(self):
        print("Nissan is Driving")

class Toyota:
    def drive(self):
        print("Toyota is Driving")

n = Nissan()
Driver(n)
t = Toyota()
Driver(t)
