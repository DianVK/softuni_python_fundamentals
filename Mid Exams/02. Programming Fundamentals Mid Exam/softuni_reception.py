first_empl = int(input())
second_empl = int(input())
third_empl = int(input())
students = int(input())
total_empl = first_empl + second_empl + third_empl

hour_counter = 0

while students > 0:
    if hour_counter % 4 == 0:
        hour_counter += 1
    students -= total_empl
    if students <= 0:
        break
    hour_counter += 1

print(f"Time needed: {hour_counter}h.")