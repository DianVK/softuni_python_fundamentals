tour = input()
command = input()
while command != "Travel":
    command = command.split(":")
    action = command[0]
    if action == "Add Stop":
        index,string = int(command[1]),command[2]
        if index < len(tour):
            tour = tour[0:index] + string + tour[index:]

    elif action == "Remove Stop":
        start_index,end_index = int(command[1]),int(command[2])
        if end_index < len(tour) and start_index < len(tour):
            tour = tour[0:start_index] + tour[end_index + 1:]
    elif action == "Switch":
        old_string,new_string = command[1],command[2]
        if old_string in tour:
            tour = tour.replace(old_string,new_string)
    print(tour)
    command = input()
print(f"Ready for world tour! Planned stops: {tour}")