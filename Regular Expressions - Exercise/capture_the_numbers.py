import re
sequences = input()
numbers_pattern = re.compile(r"(?P<numbers>\d+)")
digits = []
while sequences:
    current_digits = numbers_pattern.finditer(sequences)
    for digit in current_digits:
        digits.append(digit['numbers'])
    sequences = input()

print(*digits)