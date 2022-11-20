def check_comparison(el1, el2,items):
    if items[el1] == items[el2]:
        print(f"Congrats! You have found matching elements - {items[el1]}!")
        item_to_remove = items[el1]
        items.remove(item_to_remove)
        items.remove(item_to_remove)



def middle_of_elements(items):
    middle = len(items) // 2
    item_to_append = f"-{count_moves}a"
    items.insert(middle, item_to_append)
    items.insert(middle, item_to_append)
    print("Invalid input! Adding additional elements to the board")


elements = input().split()
command = input()
count_moves = 0
he_won = False
while command != "end":
    current_command = command.split()
    first_index = int(current_command[0])
    second_index = int(current_command[1])

    if 0 <= first_index < len(elements) and 0 <= second_index <= len(elements):
        if elements[first_index] == elements[second_index]:
            count_moves += 1
            check_comparison(first_index,second_index,elements)
        elif elements[first_index] != elements[second_index]:
            print("Try again!")
    elif 0 > first_index or first_index > len(elements) or 0 > second_index or second_index > len(elements):
        count_moves += 1
        middle_of_elements(elements)

    if len(elements) == 0:
        print(f"You have won in {count_moves} turns!")
        he_won = True
        exit()

    command = input()

if command == "end" and not he_won:
    print("Sorry you lose :(")

print(*elements)