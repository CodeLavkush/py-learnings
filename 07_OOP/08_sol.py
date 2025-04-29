class Student:
    def __init__(self, sId, name, rollNo):
        self.__sId = sId
        self.name = name
        self.rollNo = rollNo

    @property
    def sId(self):
        return self.__sId
    
student1 = Student(653627, "Lavkush", 24)
print("Name:", student1.name)
print("Roll No.", student1.sId)