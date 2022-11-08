<<<<<<< Updated upstream
current_name = input()
while current_name != "Welcome!":
    if current_name == "Voldemort":
        print("You must not speak of that name!")
        exit()
    if len(current_name) < 5:
        print(f"{current_name} goes to Gryffindor.")
    elif len(current_name) == 5:
        print(f"{current_name} goes to Slytherin.")
    elif len(current_name) == 6:
        print(f"{current_name} goes to Ravenclaw.")
    elif len(current_name) > 6:
        print(f"{current_name} goes to Hufflepuff.")
    current_name = input()

=======
current_name = input()
while current_name != "Welcome!":
    if current_name == "Voldemort":
        print("You must not speak of that name!")
        exit()
    if len(current_name) < 5:
        print(f"{current_name} goes to Gryffindor.")
    elif len(current_name) == 5:
        print(f"{current_name} goes to Slytherin.")
    elif len(current_name) == 6:
        print(f"{current_name} goes to Ravenclaw.")
    elif len(current_name) > 6:
        print(f"{current_name} goes to Hufflepuff.")
    current_name = input()

>>>>>>> Stashed changes
print("Welcome to Hogwarts.")