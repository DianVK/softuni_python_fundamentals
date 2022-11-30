count_students = int(input())
students_database = {}

for student in range(count_students):
    student_name = input()
    student_grade = float(input())
    if student_name not in students_database:
        students_database[student_name] = []
    students_database[student_name].append(student_grade)

for student,grade in students_database.items():
    average_grade = sum(grade) / len(grade)
    if average_grade >= 4.50:
        print(f"{student} -> {average_grade:.2f}")