def create_dragon(colour, dragon_name, dmg, hp, defense, all_dragons_dict):
    all_dragons_dict[colour] = all_dragons_dict.get(colour, {})
    all_dragons_dict[colour][dragon_name] = {'dmg': dmg,'hp': hp,'defense' : defense}
    return all_dragons_dict


def show_results(all_dragons):
    for color in all_dragons:
        average_dmg, average_hp, average_def = 0,0,0
        for dragon_name in all_dragons[color]:
            average_hp += all_dragons[color][dragon_name]['hp']
            average_dmg += all_dragons[color][dragon_name]['dmg']
            average_def += all_dragons[color][dragon_name]['defense']
        all_dragons_per_color = len(all_dragons[color])
        print(f"{color}::({average_dmg / all_dragons_per_color:.2f}/{average_hp / all_dragons_per_color:.2f}/"
              f"{average_def / all_dragons_per_color:.2f})")
        for dragon_name in sorted(all_dragons[color]):
            print(f"-{dragon_name} -> damage: {all_dragons[color][dragon_name]['dmg']},"
                  f" health: {all_dragons[color][dragon_name]['hp']},"
                  f" armor: {all_dragons[color][dragon_name]['defense']}")


types_dragons = {}
count_dragons = int(input())
for dragon in range(count_dragons):
    current_type, name, damage, health, armor = [int(item) if item.isdigit() else item for item in input().split()]
    if health == "null":
        health = 250
    if damage == "null":
        damage = 45
    if armor == "null":
        armor = 10
    create_dragon(current_type, name, damage, health, armor, types_dragons)

show_results(types_dragons)


