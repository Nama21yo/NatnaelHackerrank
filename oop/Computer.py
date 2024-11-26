class Computer:
    def __init__(self, name, CPU, OS):
        self.name = name
        self.cpu = self.CPU(CPU)
        self.os = self.OS(OS)
    def __str__(self):
        return 'Name: ' + self.name + '\nCPU:' + self.CPU.get_make() + '\nOS: ' + self.OS.get_name()
    
    class CPU:
        def __init__(self, make):
            self.make = make
        
        def get_make(self):
            return self.make
    class OS:
        def __init__(self, name):
            self.name = name
        
        def get_name(self):
            return self.name