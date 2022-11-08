quantity_decorations = int(input())
days_until_christmas = int(input())
points = 0
total_price = 0
days_counter = 0
for day in range(days_until_christmas, 0, -1):
    days_counter += 1
    if days_counter % 11 == 0:
        quantity_decorations = quantity_decorations + 2
    if days_counter % 2 == 0:
        total_price += quantity_decorations * 2
        points += 5
    if days_counter % 3 == 0:
        total_price += (quantity_decorations * 5) + (quantity_decorations * 3)
        points += 3 + 10
    if days_counter % 5 == 0:
        total_price += quantity_decorations * 15
        points += 17
        if days_counter % 3 == 0:
            points += 30
    if days_counter % 10 == 0:
        points -= 20
        total_price += 5 + 3 + 15
if days_counter % 10 == 0:
    points -= 30
print(f"Total cost: {total_price} \nTotal spirit: {points}")