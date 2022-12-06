import re
text = input()
mail_pattern = re.compile(r"(^|\s)(?P<valid_name>([a-z]+[\.\-]?)+[@][a-z]+([\-\.]?[a-z]+)?([\.][a-z]+)+)")
valid_mail = mail_pattern.finditer(text)
for valid in valid_mail:
    print(f"{valid['valid_name']}")