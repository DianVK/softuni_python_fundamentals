import re
names = input()

pattern = r"\b[A-Z][a-z]+[ ][A-Z][a-z]+\b"
matching_names = re.findall(pattern, names)
print(' '.join(matching_names))