import re
text = input()
correct_text = r"(^_|(?<=\s_))[a-zA-Z0-9]+\b"
valid_text = []

matched_text = [obj.group() for obj in re.finditer(correct_text,text)]
print(*matched_text,sep=",")