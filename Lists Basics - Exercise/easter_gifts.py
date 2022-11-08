list_of_gifts = input().split()
command = input()
counter = 0
while command != "No Money":
    current_command = command.split()
    current_gift = current_command[1]
    if current_command[0] == "OutOfStock":
        for index in range(len(list_of_gifts)):
            if list_of_gifts[index] == current_gift:
                list_of_gifts[index] = "None"
                counter += 1

    elif current_command[0] == "Required":
        index_command = int(current_command[2])
        if 0 <= index_command < len(list_of_gifts):
            list_of_gifts[index_command] = current_gift
    elif current_command[0] == "JustInCase":
        list_of_gifts[-1] = current_gift
    command = input()

for none in range(counter):
    if "None" in list_of_gifts:
        list_of_gifts.remove("None")
print(*list_of_gifts)