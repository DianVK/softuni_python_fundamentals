import re
sequence = input()
text_pattern = re.compile(r"(^|(?<= ))_(?P<text>([A-Za-z]+))($|(?= ))")
valid_pattern = text_pattern.finditer(sequence)
texts = []
for text in valid_pattern:
    texts.append(text['text'])

print(*texts,sep=",")