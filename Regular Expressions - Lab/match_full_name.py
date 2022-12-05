import re

names = input()
name_pattern = r'\b[A-Z][a-z]+[ ][A-Z][a-z]+\b'
check_name = re.findall(name_pattern, names)
print(" ".join(check_name))