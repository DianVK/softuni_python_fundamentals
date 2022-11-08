numbers = input().split(", ")
counter = 0
int_numbers = []
int_numbers_delete = []

for num in range(len(numbers)):
    int_num = int(numbers[num])
    int_numbers.append(int_num)

for num in range(len(int_numbers)):
    int_numbers_delete.append(int_numbers[num])

for num in range(len(int_numbers)):
    if int_numbers[num] == 0:
        int_numbers_delete.remove(0)
        counter += 1

for zero in range(1, counter + 1):
    int_numbers_delete.append(0)

print(int_numbers_delete)