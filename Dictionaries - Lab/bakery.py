elements = input().split()
bakery = {}

for el in range(0, len(elements), 2):
    key = elements[el]
    value = elements[el + 1]
    bakery[key] = int(value)

print(bakery)