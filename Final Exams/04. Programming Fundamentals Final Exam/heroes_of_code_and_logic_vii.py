def cast_spell():
    global heroes
    if heroes[current_hero_name]['hero_mp'] >= mp_needed:
        heroes[current_hero_name]['hero_mp'] -= mp_needed
        print(f"{current_hero_name} has successfully cast {spell_name} and now has {heroes[current_hero_name]['hero_mp']} MP!")
    else:
        print(f"{current_hero_name} does not have enough MP to cast {spell_name}!")


def take_dmg():
    global heroes
    heroes[current_hero_name]['hero_hp'] -= damage
    if heroes[current_hero_name]['hero_hp'] > 0:
        print(f"{current_hero_name} was hit for {damage} HP by {attacker} and now has {heroes[current_hero_name]['hero_hp']} HP left!")
    else:
        print(f"{current_hero_name} has been killed by {attacker}!")

def recharge():
    global heroes
    if heroes[current_hero_name]['hero_mp'] + amount <= 200:
        heroes[current_hero_name]['hero_mp'] += amount
        print(f"{current_hero_name} recharged for {amount} MP!")
    else:
        diff = 200 - heroes[current_hero_name]['hero_mp']
        heroes[current_hero_name]['hero_mp'] = 200
        print(f"{current_hero_name} recharged for {diff} MP!")
def heal():
    global heroes
    if heroes[current_hero_name]['hero_hp'] + amount <= 100:
        heroes[current_hero_name]['hero_hp'] += amount
        print(f"{current_hero_name} healed for {amount} HP!")
    else:
        diff = 100 - heroes[current_hero_name]['hero_hp']
        heroes[current_hero_name]['hero_hp'] = 100
        print(f"{current_hero_name} healed for {diff} HP!")

heroes = {}

count_heroes = int(input())
for hero in range(count_heroes):
    #hero_info = input().split()
    # hero_name = hero_info[0]
    # hero_hp = int(hero_info[1])
    # hero_mp = int(hero_info[2])
    hero_info = input()
    hero_name, hero_hp, hero_mp = [int(item) if item.isdigit() else item for item in hero_info.split()]
    heroes[hero_name] = heroes.get(hero_name, {'hero_hp': hero_hp, 'hero_mp': hero_mp})

command = input()
while command !="End":
    current_command = command.split(" - ")
    action = current_command[0]
    current_hero_name = current_command[1]
    if action == "CastSpell":
        mp_needed,spell_name = int(current_command[2]),current_command[3]
        cast_spell()
    elif action == "TakeDamage":
        damage,attacker = int(current_command[2]),current_command[3]
        take_dmg()
    elif action == "Recharge":
        amount = int(current_command[2])
        recharge()
    elif action == "Heal":
        amount = int(current_command[2])
        heal()


    command = input()
for hero_name in heroes:
    if heroes[hero_name]['hero_hp'] > 0:
        print(f"{hero_name}\n  HP: {heroes[hero_name]['hero_hp']} \n  MP: {heroes[hero_name]['hero_mp']}")