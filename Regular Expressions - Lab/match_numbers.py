import re
digits = input()
digit_pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
valid_digits = [obj.group() for obj in re.finditer(digit_pattern,digits)]
print(*valid_digits)