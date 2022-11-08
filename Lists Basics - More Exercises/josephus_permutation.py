numbers = [int(number) for number in input().split()]
kill_number = int(input())
counter = 0
new_list = []
index = 0
while len(numbers) > 0:
    counter += 1
    if counter % kill_number == 0:
        new_list.append(numbers[index])
        numbers.pop(index)
    elif counter % kill_number != 0:
        index += 1

    if index >= len(numbers):
        index = 0

print(str(new_list).replace(' ', ''))
