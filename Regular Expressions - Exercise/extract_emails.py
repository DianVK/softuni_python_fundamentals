import re
check_email = input()

pattern = r"(^|(?<=\s))[a-zA-Z0-9]+[\._-]?[a-zA-Z0-9]+@[a-z]+-?[a-z]+(\.[a-z]+)+"
correct_email = [obj.group() for obj in re.finditer(pattern, check_email)]
print(*correct_email,sep="\n")