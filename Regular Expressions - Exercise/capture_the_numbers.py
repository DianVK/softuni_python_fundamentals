import re

pattern = r"\d+"
text_line = input()
all_numbers = []
while text_line != "":
    numbers = re.findall(pattern,text_line)
    all_numbers.extend(numbers)
    text_line = input()

print(*all_numbers)