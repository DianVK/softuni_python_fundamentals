import re
phone_numbers = input()
number_pattern = r"\+359(?P<separator>[ |-])[2](?P=separator)\d{3}(?P=separator)\d{4}\b"
valid_numbers = [obj.group() for obj in re.finditer(number_pattern,phone_numbers)]
print(*valid_numbers,sep=", ")