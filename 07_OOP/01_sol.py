class Student:
    def __init__(self, sId, name, rollNo):
        self.sId = sId
        self.name = name
        self.rollNo = rollNo
    
student1 = Student(653627, "Lavkush", 24)
print("Name:", student1.name)
print("Roll No.", student1.rollNo)