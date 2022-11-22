def loot(items):
    del items[0]
    for item in items:
        if item not in chest:
            chest.insert(0, item)


def drop(item_index, items):
    if item_index < len(items):
        current_item = items[item_index]
        items.pop(item_index)
        items.append(current_item)
        return items


def steal(items,count):
    removed_items = []
    if count > len(items):
        count = len(items)
    for item in range(1, count + 1):
        item = items[-1]
        removed_items.append(item)
        items.pop(-1)
    removed_items.reverse()
    print(", ".join(removed_items))
    return items


chest = input().split("|")
command = input()

while command != "Yohoho!":
    current_command = command.split()
    action = current_command[0]
    if action == "Loot":
        loot(command.split())
    elif action == "Drop":
        index = int(current_command[1])
        drop(index, chest)

    elif action == "Steal":
        count_items = int(current_command[1])
        steal(chest,count_items)

    command = input()

if len(chest) > 0:
    all_treasure_len = 0
    for item in range(len(chest)):
        all_treasure_len += len(chest[item])
    average_gain = all_treasure_len / len(chest)
    print(f"Average treasure gain: {average_gain:.2f} pirate credits.")
else:
    print("Failed treasure hunt.")