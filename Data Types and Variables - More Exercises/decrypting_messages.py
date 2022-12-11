secret_key = int(input())
number_lines = int(input())
secret_word = ""
for _ in range(number_lines):
    letter = input()
    current_letter = chr(ord(letter) + secret_key)
    secret_word += current_letter
print(secret_word)