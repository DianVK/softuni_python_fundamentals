def plunder():
    pass
def prosper():
    pass

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
print(cities_info)
events = input()
while events != "End":
    #•	"Plunder=>{town}=>{people}=>{gold}"
    current_event = events.split("=>")
    action = current_event[0]
    if action == "Plunder":
        town,people,gold = current_event[1],int(current_event[2]),int(current_event[3])
        plunder()
    elif action == "Prosper":
        town,gold = current_event[1],int(current_event[2])
        prosper()
    events = input()