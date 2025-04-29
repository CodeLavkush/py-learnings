class Student:
    def __init__(self, sId, name, rollNo):
        self.sId = sId
        self.name = name
        self.rollNo = rollNo
    
    def display_student_info(self):
        print(f"Student Id: {self.sId}\nName: {self.name}\nRoll No: {self.rollNo}")

    @staticmethod
    def info():
        print("He is an briliant student!!")
    
student1 = Student(653627, "Lavkush", 24)
student1.display_student_info()
student1.info()
Student.info()