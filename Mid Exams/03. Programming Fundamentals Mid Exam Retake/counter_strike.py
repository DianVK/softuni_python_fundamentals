initial_energy = int(input())
wins = 0
distance = input()

while distance != "End of battle":
    distance = int(distance)
    if initial_energy >= distance:
        initial_energy -= distance
        wins += 1
        if wins % 3 == 0:
            initial_energy += wins
    elif initial_energy < distance:
        break
    distance = input()

if distance == "End of battle":
    print(f"Won battles: {wins}. Energy left: {initial_energy}")
elif initial_energy < distance:
    print(f"Not enough energy! Game ends with {wins} won battles and {initial_energy} energy")