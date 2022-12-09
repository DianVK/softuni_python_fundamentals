import re
text = input()
text_pattern = re.compile(r'(^|(?<= ))(?P<separator>[\:]{2}|[\*]{2})(?P<word>[A-Za-z]+)(?P=separator)')
valid_text = text_pattern.finditer(text)
all_valid_text = text_pattern.finditer(text)
all_valid_texts = []
cool_words = []
for valid in all_valid_text:
    current_text = valid['separator'] + valid['word'] + valid['separator']
    all_valid_texts.append(current_text)

for valid in valid_text:
    current_text = valid['word']
    current_sum = 0
    min_amount = 1
    count_emojis = 0
    for digit in range(len(text)):
        current_digit = text[digit]
        if current_digit.isdigit():
            min_amount *= int(current_digit)
    for char in range(len(current_text)):
        current_char = current_text[char]
        if current_char.isdigit():
            current_sum += int(current_char)
    if current_sum >= min_amount:
        print(f"Cool threshold: {min_amount}")
        print(f"{count_emojis} emojis found in the text. The cool ones are:")
        print(*all_valid_text,sep="\n")