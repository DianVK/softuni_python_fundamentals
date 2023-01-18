command = input()
phonebook = {}
while len(command) != 1:
    name, number = command.split("-")
    if name not in phonebook:
        phonebook[name] = number
    else:
        phonebook[name] = number
    command = input()

for looking_name in range(int(command)):
    current_name = input()
    if current_name not in phonebook:
        print(f"Contact {current_name} does not exist.")
    else:
        print(f"{current_name} -> {phonebook[current_name]}")
