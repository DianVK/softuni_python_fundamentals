text = input()
previous_letter = ''

for current_letter in text:
    if current_letter != previous_letter:
        print(current_letter, end="")
        previous_letter = current_letter