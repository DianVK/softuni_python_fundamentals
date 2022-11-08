numbers = [int(number) for number in input().split()]
kill_num = int(input())
counter = 0
killed = []
index = 0
while len(numbers) > 0:
    counter += 1
    if counter % kill_num == 0:
        killed.append(numbers[index])
        numbers.pop(index)
    elif counter % kill_num != 0:
        index += 1

    if index >= len(numbers):
        index = 0

print(str(killed).replace(" ", ""))







