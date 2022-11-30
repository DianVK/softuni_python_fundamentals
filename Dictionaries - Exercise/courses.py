courses = {}
command = input()
while command != "end":
    course_name,student_name = command.split(" : ")
    if course_name not in courses:
        courses[course_name] = []
    courses[course_name].append(student_name)

    command = input()

for course in courses.items():
    current_course = course[0]
    current_students = course[1]
    count_students_in_course = 0
    print(f"{current_course}: {len(current_students)}")
    for students in range(len(current_students)):

        print(f"-- {current_students[students]}")