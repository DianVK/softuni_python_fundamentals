from math import ceil
students = int(input())
total_lectures = int(input())
bonus = int(input())
best_student = 0
best_student_attendances = 0
for student in range(1, students + 1):
    count_attendances = int(input())
    total_bonus = count_attendances / total_lectures * (5 + bonus)
    if total_bonus > best_student:
        best_student = total_bonus
        best_student_attendances = count_attendances
    elif total_bonus < best_student:
        number_to_round = total_bonus


print(f"Max Bonus: {ceil(best_student)}.")
print(f"The student has attended {best_student_attendances} lectures.")
#Round the bonus points at the end to the nearest larger number.


