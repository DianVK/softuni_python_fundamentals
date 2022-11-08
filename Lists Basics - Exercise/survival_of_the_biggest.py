list_integers = input().split()
numbers_to_remove = int(input())
new_list = []
for num in range(len(list_integers)):
    new_list.append(int(list_integers[num]))

for index in range(numbers_to_remove):
    new_list.remove(min(new_list))

print(*new_list, sep=', ')