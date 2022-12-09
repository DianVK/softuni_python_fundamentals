def contains():
    if substring in raw_activation_key:
        print(f"{raw_activation_key} contains {substring}")
    else:
        print(f"Substring not found!")


def flip_to_upper():
    global raw_activation_key
    range_to_upper = raw_activation_key[start_index:end_index]
    range_to_upper = range_to_upper.upper()
    raw_activation_key = raw_activation_key[:start_index] + range_to_upper + raw_activation_key[end_index:]
    print(raw_activation_key)


def flip_to_lower():
    global raw_activation_key
    range_to_lower = raw_activation_key[start_index:end_index]
    range_to_lower = range_to_lower.lower()
    raw_activation_key = raw_activation_key[:start_index] + range_to_lower + raw_activation_key[end_index:]
    print(raw_activation_key)


def slice():
    global raw_activation_key
    item_to_slice = raw_activation_key[start_index:end_index]
    empty_string = ""
    raw_activation_key = raw_activation_key.replace(item_to_slice,empty_string)
    print(raw_activation_key)


raw_activation_key = input()
command = input()

while command != "Generate":
    current_command = command.split(">>>")
    action = current_command[0]
    if action == "Contains":
        substring = current_command[1]
        contains()
    elif action == "Flip":
        type_action = current_command[1]
        start_index = int(current_command[2])
        end_index = int(current_command[3])
        if type_action == "Upper":
            flip_to_upper()
        elif type_action == "Lower":
            flip_to_lower()

    elif action == "Slice":
        start_index = int(current_command[1])
        end_index = int(current_command[2])
        slice()
    command = input()

if command == "Generate":
    print(f"Your activation key is: {raw_activation_key}")
