command = input()

while command != "end":
    current_word = command
    word_reversed = ""
    for text in reversed(current_word):
        word_reversed += text
    print(f"{current_word} = {word_reversed}")
    command = input()