
class Teacher:
    total = 0
    def __init__(self, marks):
        self.marks = marks
        Teacher.total += 1
    
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


print(Student.total)
print(Teacher.total)