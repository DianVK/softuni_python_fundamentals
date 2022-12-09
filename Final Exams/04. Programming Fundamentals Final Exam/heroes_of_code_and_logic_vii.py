def cast_spell():
    pass
def take_dmg():
    pass
def recharge():
    pass
def heal():
    pass
heroes = {}
#"{hero name} {HP} {MP}"
count_heroes = int(input())
for hero in range(count_heroes):
    #hero_info = input().split()
    # hero_name = hero_info[0]
    # hero_hp = int(hero_info[1])
    # hero_mp = int(hero_info[2])
    hero_info = input()
    heron_name, hero_hp, hero_mp = [int(item) if item.isdigit() else item for item in hero_info.split()]
    heroes[heron_name] = heroes.get(heron_name, {'hero_hp': hero_hp, 'hero_mp': hero_mp})
print(heroes)

command = input()
while command !="End":
    current_command = command.split(" - ")
    action = current_command[0]
    if action == "CastSpell":
        cast_spell()
    elif action == "TakeDamage":
        take_dmg()
    elif action == "Recharge":
        recharge()
    elif action == "Heal":
        heal()


    command = input()