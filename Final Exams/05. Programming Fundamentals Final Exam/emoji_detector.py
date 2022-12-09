import re
text = input()
text_pattern = re.compile(r'(:{2}|\*{2})(?P<word>[A-Z][a-z]{2,})\1')
valid_texts = list(text_pattern.finditer(text))
threshold = 1
for character in text:
    if character.isdigit():
        threshold *= int(character)
print(f"Cool threshold: {threshold}")
print(f"{len(valid_texts)} emojis found in the text. The cool ones are:")
for valid in valid_texts:
    sum_of_ascii_letters = sum([ord(letter) for letter in valid['word']])
    if sum_of_ascii_letters >= threshold:
        print(valid[0])