import re

numbers = input()
number_pattern = r'(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))'
check_numbers = re.finditer(number_pattern,numbers)
valid_numbers = []
for valid in check_numbers:
    valid_numbers.append(valid[0])

print(*valid_numbers, sep=" ")

# import re
# text = input()
#
# pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
# matches = [match.group() for match in re.finditer(pattern, text)]
# print(*matches, sep=" ")