class Student:
    def __init__(self, sId, name, rollNo):
        self.__sId = sId
        self.name = name
        self.rollNo = rollNo

    def get_sId(self):
        return "Student id: " + str(self.__sId)
    
    def display_student_info(self):
        print(f"Student Id: {self.sId}\nName: {self.name}\nRoll No: {self.rollNo}")
    
student1 = Student(653627, "Lavkush", 24)
print(student1.get_sId())