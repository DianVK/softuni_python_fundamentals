level_of_fire = input().split("#")
amount_of_water = int(input())
high_points = 0
medium_points = 0
low_points = 0
cells = []
effort = 0
for index in level_of_fire:
    index = index.split(" = ")
    type_level = index[0]
    points_level = int(index[1])
    if amount_of_water >= points_level:
        if type_level == "High" and (81 <= points_level <= 125):
            cells.append(points_level)
            amount_of_water -= points_level
            effort += points_level*0.25
        if type_level == "Medium" and (51 <= points_level <= 80):
            cells.append(points_level)
            amount_of_water -= points_level
            effort += points_level * 0.25
        if type_level == "Low" and (1 <= points_level <= 50):
            cells.append(points_level)
            amount_of_water -= points_level
            effort += points_level * 0.25

print(f"Cells:")
for cell in range(len(cells)):
    current_cell = cells[cell]
    print(f" - {current_cell}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(cells)}")