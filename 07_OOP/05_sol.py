
class Teacher:
    def __init__(self, marks):
        self.marks = marks
    
    def display_student_info(self):
        print(f"Marks: {self.marks}")

class Student(Teacher):
    def __init__(self, sId, name, rollNo, marks):
        super().__init__(marks)
        self.sId = sId
        self.name = name
        self.rollNo = rollNo
    
    def display_student_info(self):
        print(f"Student Id: {self.sId}\nName: {self.name}\nRoll No: {self.rollNo}")

teacher1 = Teacher(600)
student1 = Student(653627, "Lavkush", 24, 400)
student1.display_student_info()
teacher1.display_student_info()