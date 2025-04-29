student_score = 101

if student_score >= 101:
    print("Please verify score again!")
    exit()

if student_score < 60:
    print(f"Score: {student_score}")
    print("Grade: F")
elif student_score < 70:
    print(f"Score: {student_score}")
    print("Grade: D")
elif student_score < 80:
    print(f"Score: {student_score}")
    print("Grade: C")
elif student_score < 90:
    print(f"Score: {student_score}")
    print("Grade: B")
else:
    print(f"Score: {student_score}")
    print("Grade: A")
