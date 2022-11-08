<<<<<<< Updated upstream
all_numbers = input().split()
how_many_to_remove = int(input())
int_numbers = []
for number in all_numbers:
    int_numbers.append(int(number))
for remove in range(how_many_to_remove):
    all_numbers.remove(min(all_numbers))
=======
all_numbers = input().split()
how_many_to_remove = int(input())
int_numbers = []
for number in all_numbers:
    int_numbers.append(int(number))
for remove in range(how_many_to_remove):
    all_numbers.remove(min(all_numbers))
>>>>>>> Stashed changes
print(*all_numbers, sep=", ")