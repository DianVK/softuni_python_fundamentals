messages = input().split()

for message in messages:
    whats_the_word = ""
    secret_message = ""
    letters = []
    letters_str = ""
    whole_message = ""
    for msg in range(len(message)):
        current_letter = message[msg]
        if current_letter.isdigit():
            whats_the_word += current_letter
        else:
            letters.append(current_letter)
    word = chr(int(whats_the_word))
    secret_message += word
    letters[0], letters[-1] = letters[-1], letters[0]
    for letter in letters:
        letters_str += letter
    whole_message = secret_message + letters_str
    print(whole_message, end=" ")

# words = input().split()
# current_first_letter = ""
# rest_of_the_word = ""
#
# for each_word in words:
#     current_first_letter = ""
#     rest_of_the_word = ""
#     current_word = each_word
#     for letter in each_word:
#         if letter.isdigit():
#             current_first_letter += letter
#         elif not letter.isdigit():
#             rest_of_the_word += letter
#     if len(rest_of_the_word) > 1:
#         second_letter, last_letter = rest_of_the_word[-1], rest_of_the_word[0]
#         print(f"{chr(int(current_first_letter))}{second_letter}{rest_of_the_word[1:-1]}{last_letter}", end=" ")
#     elif len(rest_of_the_word) == 1:
#         print(f"{chr(int(current_first_letter))}{rest_of_the_word}", end=" ")