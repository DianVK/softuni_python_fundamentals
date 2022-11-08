budget = float(input())
price_per_kg_floar = float(input())
price_per_pack_eggs = price_per_kg_floar * 0.75
price_per_liter_milk = price_per_kg_floar * 1.25

total_price = price_per_pack_eggs + price_per_kg_floar + (price_per_liter_milk / 4)
colored_eggs = 0
breads = 0
while total_price < budget:
    budget -= total_price
    breads += 1
    colored_eggs += 3
    if breads % 3 == 0:
        colored_eggs -= breads - 2

print(f"You made {breads} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")