def plunder(current_town, people_killed, gold_stolen):
    cities_info[current_town]['gold'] -= gold_stolen
    cities_info[current_town]['people'] -= people_killed
    print(f"{current_town} plundered! {gold_stolen} gold stolen, {people_killed} citizens killed.")
    if cities_info[current_town]['gold'] == 0 or cities_info[current_town]['people'] == 0:
        del cities_info[current_town]
        print(f"{current_town} has been wiped off the map!")


def prosper(current_town, gold_attained):
    if gold_attained < 0:
        print("Gold added cannot be a negative number!")
        return
    cities_info[current_town]['gold'] += gold_attained
    print(f"{gold_attained} gold added to the city treasury. {current_town} now has"
          f" {cities_info[current_town]['gold']} gold.")


cities_info = {}
information = input()
while information != "Sail":
    town, people, gold = [int(item) if item.isdigit() else item for item in information.split("||")]
    cities_info[town] = cities_info.get(town, {'people': 0, 'gold': 0})
    cities_info[town]['people'] += people
    cities_info[town]['gold'] += gold
    information = input()

command = input()
while command != "End":
    action, town, *info = [int(item) if item[-1].isdigit() else item for item in command.split("=>")]
    if action == "Plunder":
        plunder(town, *info)
    elif action == "Prosper":
        prosper(town, *info)
    command = input()

if cities_info:
    print(f"Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:")
    for town, value in cities_info.items():
        print(f"{town} -> Population: {value['people']} citizens, Gold: {value['gold']} kg")
elif not cities_info:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")