import re
furniture = input()
total_cost = 0
pattern = r"[>][>][a-zA-Z]+[<][<]\d+[.]?[\!]?([\d]+)?[\!]?([\d]+)?"
all_furniture = []
while furniture != "Purchase":
    check_is_valid = [obj.group() for obj in re.finditer(pattern,furniture)]
    if check_is_valid:
        all_furniture.append(*check_is_valid)
    furniture = input()

items_names = []
items_prices = []
items_quantities = []

for item in all_furniture:
    current_item = item
    find_name = current_item.index("<<")
    item_name = current_item[2:find_name]
    items_names.append(item_name)
    find_price = current_item.index("!")
    item_price = current_item[find_name + 2:find_price]
    items_prices.append(item_price)
    item_quantity = current_item[find_price + 1:]
    items_quantities.append(item_quantity)

for el in range(len(items_prices)):
    current_item_price = float(items_prices[el]) * int(items_quantities[el])
    total_cost += current_item_price

print(f"Bought furniture:")

for item in items_names:
    print(item)

print(f"Total money spend: {total_cost:.2f}")