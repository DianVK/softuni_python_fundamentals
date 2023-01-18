encrypted_message = input()


def main():
    command = input()
    while command != "Decode":
        command = command.split("|")
        action = command[0]
        if action == "Move":
            move(int(command[1]))
        elif action == "Insert":
            insert(int(command[1]), command[2])
        elif action == "ChangeAll":
            change_all(command[1], command[2])
        command = input()
    print(f"The decrypted message is: {encrypted_message}")


def move(number_of_letters):
    global encrypted_message
    first_letters = encrypted_message[0:number_of_letters]
    encrypted_message = encrypted_message[number_of_letters:] + first_letters


def insert(index, value):
    global encrypted_message
    encrypted_message = encrypted_message[0:index] + value + encrypted_message[index:]


def change_all(substring, replacement):
    global encrypted_message
    if substring in encrypted_message:
        encrypted_message = encrypted_message.replace(substring, replacement)


main()
