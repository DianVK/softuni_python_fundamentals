import re
count_messages = int(input())
planets = []
special_chars = "sStTaArR"

for _ in range(count_messages):
    current_message = input()
    counter = 0
    for char in special_chars:
        counter += current_message.count(char)
    planets.append("".join(chr(ord(x) - counter) for x in current_message))

pattern = re.compile(r'@(?P<planet>[A-Za-z]+)[0-9]*[^@|\-|!|:|>]*'
                            r':(?P<population>\d+)[^@|\-|!|:|>]*'
                            r'!(?P<attack_type>A|D)![^@|\-|!|:|>]*'
                            r'->(?P<soldiers>\d+)')

attacked_planets = []
destroyed_planets = []

for planet in planets:
    result = list(pattern.finditer(planet))
    for check in result:
        if check['attack_type'] == "A":
            attacked_planets.append(check['planet'])
        if check['attack_type'] == "D":
            destroyed_planets.append(check['planet'])

print(f"Attacked planets: {len(attacked_planets)}")
[print(f"-> {x}") for x in sorted(attacked_planets)]
print(f"Destroyed planets: {len(destroyed_planets)}")
[print(f"-> {x}") for x in sorted(destroyed_planets)]