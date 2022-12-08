def take_odd():
    global new_password
    for char in range(len(password)):
        if char % 2 != 0:
            new_password += password[char]

    print(new_password)


def cut():
    global new_password
    cut_from = index
    cut_to = index + length
    empty_string = ""
    new_password = new_password[0:cut_from] + new_password[cut_to:]
    print(new_password)



def substitute():
    global new_password
    if substring in new_password:
        new_password = new_password.replace(substring, current_substitute)
        print(new_password)
    else:
        print(f"Nothing to replace!")


password = input()
command = input()
new_password = ""
while command != "Done":
    current_command = command.split()
    action = current_command[0]
    if action == "TakeOdd":
        take_odd()
    elif action == "Cut":
        index,length = int(current_command[1]),int(current_command[2])
        cut()
    elif action == "Substitute":
        substring,current_substitute = current_command[1],current_command[2]
        substitute()
    command = input()

if command == "Done":
    print(f"Your password is: {new_password}")