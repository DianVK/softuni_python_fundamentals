count_plants = int(input())
all_plants = {}
for _ in range(count_plants):
    plant,rarity = input().split("<->")
    if plant in all_plants:
        all_plants[plant]['rarity'] = rarity
        continue
    all_plants[plant] = all_plants.get(plant, {'rarity': rarity, 'rating': []})

command = input()
while command != "Exhibition":
    command = command.split()
    action = command[0]
    current_plant = command[1]
    if current_plant not in all_plants:
        print("error")
        command = input()
        continue
    if action == "Rate:":
        rating = int(command[3])
        all_plants[current_plant]['rating'].append(rating)
    elif action == "Update:":
        new_rarity = int(command[3])
        all_plants[current_plant]['rarity'] = new_rarity
    elif action == "Reset:":
        all_plants[current_plant]['rating'] = []
    command = input()


print(f"Plants for the exhibition:")
for plant in all_plants:
    rarity = all_plants[plant]['rarity']
    rating = 0
    if len(all_plants[plant]['rating']):
        rating = sum(all_plants[plant]['rating']) / len(all_plants[plant]['rating'])
    print(f"- {plant}; Rarity: {rarity}; Rating: {rating:.2f}")