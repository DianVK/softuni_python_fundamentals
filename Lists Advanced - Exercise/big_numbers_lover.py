numbers_as_string = input().split()

reversed_numbers = numbers_as_string[::-1]
receive_as_string = ""

for number in reversed_numbers:
    receive_as_string += number
print(receive_as_string)