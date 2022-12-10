def plunder():
    global cities_info
    cities_info[town]['population'] -= people
    cities_info[town]['gold'] -= gold
    print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
    if cities_info[town]['population'] <= 0 or cities_info[town]['gold'] <= 0:
        print(f"{town} has been wiped off the map!")
        del cities_info[town]


def prosper():
    global cities_info
    if gold > 0:
        cities_info[town]['gold'] += gold
        print(f"{gold} gold added to the city treasury. {town} now has {cities_info[town]['gold']} gold.")
    else:
        print("Gold added cannot be a negative number!")



command = input()
cities_info = {

}
while command != "Sail":
    cities,population,gold = [int(item) if item.isdigit() else item for item in command.split("||")]
    if cities not in cities_info:
        cities_info[cities] = cities_info.get(cities, {'population': population,'gold': gold})
    elif cities in cities_info:
        cities_info[cities]['population'] += population
        cities_info[cities]['gold'] += gold

    command = input()
events = input()
while events != "End":
    current_event = events.split("=>")
    action = current_event[0]
    if action == "Plunder":
        town,people,gold = current_event[1],int(current_event[2]),int(current_event[3])
        plunder()
    elif action == "Prosper":
        town,gold = current_event[1],int(current_event[2])
        prosper()
    events = input()
print(f"Ahoy, Captain! There are {len(cities_info)} wealthy settlements to go to:")
for el in cities_info:
    print(f"{el} -> Population: {cities_info[el]['population']} citizens, Gold: {cities_info[el]['gold']} kg")