def potion(healing, health):
    if health + healing > 100:
        healing = 100 - health
        health = 100
    elif health + healing <= 100:
        health = health + healing
    print(f"You healed for {healing} hp.")
    print(f"Current health: {health} hp.")
    return health


def chest(coins):
    print(f"You found {coins} bitcoins.")
    return coins


def getting_attacked(monster, damage_received, hp, count_room):
    hp -= damage_received
    if hp > 0:
        print(f"You slayed {monster}.")
    elif hp <= 0:
        print(f"You died! Killed by {monster}.")
        print(f"Best room: {count_room}")
    return hp


dungeon_rooms = input().split("|")
hp = 100
bitcoins = 0
for count, room in enumerate(dungeon_rooms, 1):
    room = room.split()
    action = room[0]
    amount = int(room[1])
    if action != "potion" and action != "chest":
        hp = getting_attacked(action, amount, hp, count)
        if hp <= 0:
            break
    elif action == "potion":
        hp = potion(amount, hp)
    elif action == "chest":
        bitcoins += chest(amount)

if hp > 0:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {hp}")