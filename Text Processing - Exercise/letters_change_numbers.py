from string import ascii_lowercase
text = input().split()
total_sum = 0
alphabet = " " + ascii_lowercase

for letter in text:
    first_letter = letter[0]
    last_letter = letter[-1]
    number = int(letter[1:-1])

    if letter[0].isupper():
        total_sum += number / alphabet.index(first_letter.lower())
    elif letter[0].islower():
        total_sum += number * alphabet.index(first_letter)

    if letter[-1].isupper():
        total_sum -= alphabet.index(last_letter.lower())
    elif letter[-1].islower():
        total_sum += alphabet.index(last_letter)

print(f"{total_sum:.2f}")