<<<<<<< Updated upstream
string_rules = {
    "banned symbols": [",", ".", "_"]
}

number_of_strings = int(input())
for words in range(number_of_strings):
    current_word = input()
    for letter in current_word:
        if letter in string_rules['banned symbols']:
            print(f"{current_word} is not pure!")
            break
    else:
=======
string_rules = {
    "banned symbols": [",", ".", "_"]
}

number_of_strings = int(input())
for words in range(number_of_strings):
    current_word = input()
    for letter in current_word:
        if letter in string_rules['banned symbols']:
            print(f"{current_word} is not pure!")
            break
    else:
>>>>>>> Stashed changes
        print(f"{current_word} is pure.")