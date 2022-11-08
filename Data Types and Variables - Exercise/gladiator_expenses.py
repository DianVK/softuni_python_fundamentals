lost_fights_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())
shield_breaking_count = 0
total_price = 0
for day in range(1, lost_fights_count + 1):
    if day % 2 == 0:
        total_price += helmet_price
    if day % 3 == 0:
        total_price += sword_price
    if day % 2 == 0 and day % 3 == 0:
        total_price += shield_price
        shield_breaking_count += 1
        if shield_breaking_count % 2 == 0:
            total_price += armor_price

print(f"Gladiator expenses: {total_price:.2f} aureus")

