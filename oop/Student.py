class Student:
    def __init__(self, name , idno, dorm):
        self.name = name
        self.ugr = idno
        self.dorm = dorm
    
    def get_name(self):
        return  self.name
    def get_ugr(self):
        return self.ugr

    def get_dorm(self):
        return self.dorm
    def set_dorm(self, new_dorm):
        self.dorm = new_dorm 