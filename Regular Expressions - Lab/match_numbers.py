import re
text = input()

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
matches = [match.group() for match in re.finditer(pattern, text)]
print(*matches, sep=" ")