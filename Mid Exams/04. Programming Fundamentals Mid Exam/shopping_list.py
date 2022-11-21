def urgent(item):
    if item not in groceries:
        groceries.insert(0, item)


def unnecessary(item):
    if item in groceries:
        groceries.remove(item)


def correct(oldItem,newItem):
    if oldItem in groceries:
        index = groceries.index(oldItem)
        groceries[index] = newItem


def rearrange(item):
    if item in groceries:
        groceries.remove(item)
        groceries.append(item)


groceries = input().split("!")
command = input()

while command != "Go Shopping!":
    current_command = command.split()
    action = current_command[0]
    item = current_command[1]
    if action == "Urgent":
        urgent(item)
    elif action == "Unnecessary":
        unnecessary(item)
    elif action == "Correct":
        old_item = item
        new_item = current_command[2]
        correct(old_item,new_item)
    elif action == "Rearrange":
        rearrange(item)
    command = input()

print(", ".join(groceries))