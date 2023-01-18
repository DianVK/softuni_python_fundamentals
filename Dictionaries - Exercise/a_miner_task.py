command = input()

items = {}
while command != "stop":
    amount = int(input())
    if command not in items:
        items[command] = amount
    else:
        items[command] += amount
    command = input()

for resource, quantity in items.items():
    print(f"{resource} -> {quantity}")
