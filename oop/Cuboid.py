class Rectangle:
    def __init__(self, l, b):
        self.length = l
        self.breadth = b
    # Getter and Setters
    def getLength(self):
        return self.length
    def setLength(self, l):
        self.length = l
    def getBreadth(self):
        return self.breadth 
    def setBreadth(self, b):
        self.breadth = b
    
    # Instance methods
    def area(self):
        return self.length * self.breadth
    def perimeter(self):
        return 2 * (self.length * self.breadth)
    # Method Overriding
    def whoami(self):
        print("I am a Rectangle")


class Cuboid(Rectangle):
    # static Variable
    countCuboid = 0
    # The fields with instance variables
    def __init__(self , l, b, h):
        self.height = h
        # like java the parent class isn't called implicitly/automatically
        super().__init__(l, b)
        # You can also intialize it in like the normal way
        # self.length = l
        # self.breadth = b 
        Cuboid.countCuboid += 1
    
    # Accessor and Mutators
    def getHeight(self):
        return self.height
    def setHeight(self, h):
        self.height = h
    
    # The methods
    def baseArea(self):
        return self.length * self.breadth
    def totalArea(self):
        return 2 * (self.length * self.breadth + self.breadth * self.height + self.height * self.length)
    def volume(self):
        return self.length * self.breadth * self.height

    #! Method Overriding
    def whoami(self):
        print("I am a Cuboid")
        super().whoami() # for calling the parent class
    
    @classmethod # Annotation/Decorator in other language
    def displayCountCuboid(cls):
        print(cls.countCuboid)

    @staticmethod 
    def isCube(length, breadth, height):
        return length == breadth == height

c1 = Cuboid(10,5,3)
# print(c1.getLength())
print(c1.volume())
# c1.setLength(12)
print(c1.perimeter())


c2 = Cuboid(20,10,5)
print(c2.volume())