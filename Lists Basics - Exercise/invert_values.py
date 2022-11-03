list_of_numbers = input().split()
opposite_numbers = []

for index in range(len(list_of_numbers)):
    opposite_number = -int(list_of_numbers[index])
    opposite_numbers.append(opposite_number)

print(opposite_numbers)