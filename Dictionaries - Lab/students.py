command = input()
students = dict()
while command[0].isupper():
    name,student_id,course = command.split(":")
    if course not in students:
        students[course] = dict()
    students[course][name] = student_id
    command = input()

command = command.replace("_", " ")

for name_and_id in students[command]:
    print(f"{name_and_id} - {students[command][name_and_id]}")