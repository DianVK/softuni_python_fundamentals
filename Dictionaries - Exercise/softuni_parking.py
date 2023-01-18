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
            print(f"{person_name} registered {car_number} successfully")
        else:
            print(f"ERROR: already registered with plate number {car_number}")

    elif action == "unregister":
        person_name = action_info[1]
        if person_name not in database:
            print(f"ERROR: user {person_name} not found")
        else:
            print(f"{person_name} unregistered successfully")
            del (database[person_name])

for user, car_num in database.items():
    print(f"{user} => {car_num}")
