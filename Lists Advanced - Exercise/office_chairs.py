number_of_rooms = int(input())
free_chairs = 0
room_counter = 0

for num in range(1, number_of_rooms + 1):
    room_counter += 1
    number_of_seats = input().split()
    chairs = number_of_seats[0]
    visitors = int(number_of_seats[1])
    if len(chairs) != visitors:
        free_chairs += len(chairs) - visitors
    if len(chairs) < visitors:
        print(f"{visitors - len(chairs)} more chairs needed in room {room_counter}")

if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")