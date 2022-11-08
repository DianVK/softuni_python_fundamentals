numbers_input = input().split()
new_list = []
for num in range(len(numbers_input)):
    new_list.append(-int(numbers_input[num]))

print(new_list)