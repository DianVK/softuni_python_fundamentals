text = input()
all_text = ''
current_text = ''

for character in range(len(text)):
    if character + 1 < len(text) and text[character].isdigit() and text[character + 1].isdigit():
        current_text = current_text * int(text[character:character + 2])
        all_text += current_text
        current_text = ''
    elif text[character].isdigit():
        current_text = current_text * int(text[character])
        all_text += current_text
        current_text = ''
    else:
        current_text += text[character]

all_text = all_text.upper()
letter_checker = ''
for letter in all_text:
    if letter not in letter_checker:
        letter_checker += letter


print(f"Unique symbols used: {len(letter_checker)}")
print(all_text)