word = input()
reverse_word = ""
for letter in range(len(word) -1, -1, -1):
    reverse_word += word[letter]
print(reverse_word)