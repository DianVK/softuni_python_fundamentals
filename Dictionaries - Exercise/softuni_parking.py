count_people = int(input())
database = {}

for person in range(count_people):
    action_info = input().split()
    action = action_info[0]
    if action == "register":
        person_name = action_info[1]
        car_number = action_info[2]
        if person_name not in database:
            database[person_name] = car_number


    elif action == "unregister":
        person_name = action_info[1]
        pass