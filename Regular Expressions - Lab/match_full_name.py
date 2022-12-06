import re
names = input()
name_pattern = r"\b[A-Z][a-z]+ [A-Z][a-z]+\b"
valid_names = re.findall(name_pattern,names)
print(*valid_names)