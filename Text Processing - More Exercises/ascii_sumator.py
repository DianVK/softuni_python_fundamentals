first_input = input()
second_input = input()
third_input = input()

sum_of_chars = 0

left_range = int(ord(first_input))
right_range = int(ord(second_input))
for char in third_input:
    current_char = int(ord(char))
    if left_range < current_char < right_range:
        sum_of_chars += current_char

print(sum_of_chars)