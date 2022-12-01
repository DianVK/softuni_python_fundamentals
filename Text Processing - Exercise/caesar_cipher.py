text = input()
for word in range(len(text)):
    current_word = text[word]
    for char in range(len(current_word)):
        current_ascii_num = ord(current_word[char])
        print(chr(current_ascii_num + 3),end="")