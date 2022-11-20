people = int(input())
max_people = 4
current_state = [int(num) for num in input().split()]

for el in range(len(current_state)):
    if people >= 4:
        if current_state[el] == 0:
            current_state[el] += 4
            people -= 4
        else:
            c_num = max_people - int(current_state[el])
            current_state[el] += c_num
            people -= c_num
    else:
        current_state[el] += people
        people = 0

check_nums = [int(num) for num in current_state if num != 4]

if people == 0 and check_nums:
    print("The lift has empty spots!")
    print(*current_state, sep=" ")
if people != 0 and not check_nums:
    print(f"There isn't enough space! {people} people in a queue!")
    print(*current_state, sep=" ")
if people == 0 and not check_nums:
    print(*current_state, sep=" ")
