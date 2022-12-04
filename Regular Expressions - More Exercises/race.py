import re
names_of_racers = input().split(", ")

name_pattern = re.compile(r'(?P<name>[a-zA-Z]+)')
km_pattern = re.compile(r'(?P<km>[0-9]+)')
racers = {}

command = input()

while command != "end of race":
    match_names = name_pattern.finditer(command)
    match_km = km_pattern.finditer(command)
    current_name = "".join([match["name"]for match in match_names])
    current_km = "".join([match["km"] for match in match_km])
    km_value = sum(map(int, current_km))
    if current_name in names_of_racers:
        racers[current_name] = racers.get(current_name, 0) + km_value

    command = input()

for counter, (name,km) in enumerate(sorted(racers.items(), key=lambda points: -points[1]), 1):
    position = ''
    if counter == 1:
        position = "st"
    elif counter == 2:
        position = "nd"
    elif counter == 3:
        position = "rd"
    else:
        break
    print(f"{counter}{position} place: {name}")