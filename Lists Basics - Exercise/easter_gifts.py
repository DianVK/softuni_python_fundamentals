<<<<<<< Updated upstream
gifts_list = input().split()
command = input()
new_list = []
while command != "No Money":
    command_list = command.split()
    current_gift = command_list[1]
    if command_list[0] == "OutOfStock":
        for word in range(len(gifts_list)):
            if gifts_list[word] == current_gift:
                gifts_list[word] = "None"
    elif command_list[0] == "Required":
        index = int(command_list[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = command_list[1]

    elif command_list[0] == "JustInCase":
        gifts_list[-1] = current_gift

    command = input()

for word in range(len(gifts_list)):
    current_word = gifts_list[word]
    if current_word != "None":
        new_list.append(current_word)

=======
gifts_list = input().split()
command = input()
new_list = []
while command != "No Money":
    command_list = command.split()
    current_gift = command_list[1]
    if command_list[0] == "OutOfStock":
        for word in range(len(gifts_list)):
            if gifts_list[word] == current_gift:
                gifts_list[word] = "None"
    elif command_list[0] == "Required":
        index = int(command_list[2])
        if 0 <= index < len(gifts_list):
            gifts_list[index] = command_list[1]

    elif command_list[0] == "JustInCase":
        gifts_list[-1] = current_gift

    command = input()

for word in range(len(gifts_list)):
    current_word = gifts_list[word]
    if current_word != "None":
        new_list.append(current_word)

>>>>>>> Stashed changes
print(*new_list)