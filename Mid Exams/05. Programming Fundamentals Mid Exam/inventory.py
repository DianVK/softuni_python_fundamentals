def collect(current_item,all_items):
    if not current_item in all_items:
        all_items.append(current_item)
    return all_items


def drop (current_item,all_items):
    if current_item in all_items:
        all_items.remove(current_item)
    return all_items


def combine(old,new,all_items):
    if old in all_items:
        index = all_items.index(old)
        all_items.insert(index + 1,new)
    return all_items


def renew(current_item,all_items):
    if current_item in all_items:
        all_items.remove(current_item)
        all_items.append(current_item)
    return all_items


inventory = input().split(", ")
command = input()
while command != "Craft!":
    current_command = command.split(" - ")
    action = current_command[0]
    item = current_command[1]
    if action == "Collect":
        collect(item, inventory)
    elif action == "Drop":
        drop(item, inventory)
    elif action == "Combine Items":
        old_item, new_item = item.split(":")
        combine(old_item, new_item, inventory)
    elif action == "Renew":
        renew(item, inventory)
    command = input()

print(", ".join(inventory))