courses = input()
courses_info = {}

while courses != "end":
    course_name, student_name = courses.split(" : ")
    courses_info[course_name] = courses_info.get(course_name,  {})
    courses_info[course_name][student_name] = student_name

    courses = input()

for key, value in courses_info.items():
    print(f"{key}: {len(courses_info[key])}")
    for name in courses_info[key]:
        print(f"-- {courses_info[key][name]}")