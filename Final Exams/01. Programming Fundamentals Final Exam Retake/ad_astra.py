import re
items = input()
item_pattern = r"(\#|\|)(?P<item_name>[A-Za-z]+(\s[A-Za-z]+)?)\1(?P<expiration_date>\d{2}\/\d{2}\/\d{2})\1(?P<calories>\d+)\1"
valid_items = [obj.group() for obj in re.finditer(item_pattern,items)]
total_calories = 0
for el in range(len(valid_items)):
    current_el = valid_items[el]
    spliter = current_el[0]
    current_el_list = current_el.split(spliter)
    total_calories += int(current_el_list[3])
print(f"You have food to last you for: {total_calories // 2000} days!")
for el in range(len(valid_items)):
    current_el = valid_items[el]
    spliter = current_el[0]
    current_el_list = current_el.split(spliter)
    print(f"Item: {current_el_list[1]}, Best before: {current_el_list[2]}, Nutrition: {int(current_el_list[3])}")

