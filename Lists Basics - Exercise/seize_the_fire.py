<<<<<<< Updated upstream
level_of_fire = input().split("#")
amount_of_water = int(input())
effort = 0
cells = []
total_fire = 0
for index in level_of_fire:
    isvalid = False
    current_index = index.split()
    temperature_number = int(current_index[2])
    type_temperature = current_index[0]
    if temperature_number > amount_of_water:
        continue
    if type_temperature == "High":
        if 81 <= temperature_number <= 125:
            isvalid = True
    elif type_temperature == "Medium":
        if 51 <= temperature_number <= 80:
            isvalid = True
    if type_temperature == "Low":
        if 1 <= temperature_number <= 50:
            isvalid = True
    if isvalid:
        amount_of_water -= temperature_number
        effort += temperature_number * 0.25
        cells.append(temperature_number)
        total_fire += temperature_number

print("Cells:")
for cell in cells:
    print(f" - {cell}")
=======
level_of_fire = input().split("#")
amount_of_water = int(input())
effort = 0
cells = []
total_fire = 0
for index in level_of_fire:
    isvalid = False
    current_index = index.split()
    temperature_number = int(current_index[2])
    type_temperature = current_index[0]
    if temperature_number > amount_of_water:
        continue
    if type_temperature == "High":
        if 81 <= temperature_number <= 125:
            isvalid = True
    elif type_temperature == "Medium":
        if 51 <= temperature_number <= 80:
            isvalid = True
    if type_temperature == "Low":
        if 1 <= temperature_number <= 50:
            isvalid = True
    if isvalid:
        amount_of_water -= temperature_number
        effort += temperature_number * 0.25
        cells.append(temperature_number)
        total_fire += temperature_number

print("Cells:")
for cell in cells:
    print(f" - {cell}")
>>>>>>> Stashed changes
print(f"Effort: {effort:.2f}\nTotal Fire: {total_fire}")