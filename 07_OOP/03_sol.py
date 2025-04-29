
class Teacher:
    def __init__(self, marks):
        self.marks = marks

class Student(Teacher):
    def __init__(self, sId, name, rollNo, marks):
        super().__init__(marks)
        self.sId = sId
        self.name = name
        self.rollNo = rollNo
    
    def display_student_info(self):
        print(f"Student Id: {self.sId}\nName: {self.name}\nRoll No: {self.rollNo}\nMarks: {self.marks}")
    
student1 = Student(653627, "Lavkush", 24, 400)
student1.display_student_info()