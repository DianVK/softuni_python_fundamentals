import re
number_texts = int(input())
for number in range(number_texts):
    text = input()
    valid_text_pattern = re.compile(r'(?P<left_side>[\@][\#]+)(?P<text>[A-Z][A-Za-z0-9]+[A-Z])(?P<right_side>[\@][\#]+)')
    valid_text = valid_text_pattern.finditer(text)
    all_valid_texts = []
    all_whole_texts = []

    for valid in valid_text:
        if len(valid['text']) >= 6:
            all_valid_texts.append(valid['text'])
            whole_text = valid['left_side'] + valid['text'] + valid['right_side']
            all_whole_texts.append(whole_text)
    for item in range(len(all_whole_texts)):
        current_item = all_whole_texts[item]
        current_group = ""
        for char in current_item:
            if char.isdigit():
                current_group += char
        if current_group != "":
            print(f"Product group: {current_group}")
        if current_group == "":
            print(f"Product group: 00")
    if text not in all_whole_texts:
        print("Invalid barcode")
