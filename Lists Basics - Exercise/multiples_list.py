factor = int(input())
count = int(input())
list_numbers = []
for num in range(1, count + 1):
    list_numbers.append(num * factor)

print(list_numbers)