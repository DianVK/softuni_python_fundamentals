number_wagons = int(input())
wagon = [0] * number_wagons
command = input()

while command != "End":
    data = command.split()
    if data[0] == "add":
        people = int(data[1])
        wagon[-1] += people
    elif data[0] == "insert":
        index = int(data[1])
        people = int(data[2])
        wagon[index] += people
    elif data[0] == "leave":
        index = int(data[1])
        people = int(data[2])
        wagon[index] -= people
    command = input()

print(wagon)