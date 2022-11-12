words = input().split()
check_is_digit = "0123456789"
current_first_letter = ""
rest_of_the_word = ""

for each_word in words:
    current_first_letter = ""
    rest_of_the_word = ""
    current_word = each_word
    for letter in each_word:
        if letter in check_is_digit:
            current_first_letter += letter
        elif letter not in check_is_digit:
            rest_of_the_word += letter
    if len(rest_of_the_word) > 1:
        second_letter, last_letter = rest_of_the_word[-1], rest_of_the_word[0]
        print(f"{chr(int(current_first_letter))}{second_letter}{rest_of_the_word[1:-1]}{last_letter}", end=" ")
    elif len(rest_of_the_word) == 1:
        print(f"{chr(int(current_first_letter))}{rest_of_the_word}", end=" ")