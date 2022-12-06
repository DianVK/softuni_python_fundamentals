import re
items = input()
items_pattern = r">>(?P<furniture_name>[A-Za-z]+)<<(?P<price>[0-9]+[\\.0-9]*)!(?P<quantity>[0-9]+)"
furniture_names = []
total_sum = 0
while items != "Purchase":
    valid_furniture = re.match(items_pattern, items)
    if valid_furniture:
        data = valid_furniture.groupdict()
        total_sum += int(valid_furniture['quantity']) * float(valid_furniture['price'])
        furniture_names.append(valid_furniture['furniture_name'])
    items = input()
print(f"Bought furniture:")
if furniture_names:
    print(*furniture_names,sep="\n")
print(f"Total money spend: {total_sum:.2f}")