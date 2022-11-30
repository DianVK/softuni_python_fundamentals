banned_word = input().split(", ")
text = input()

for ban_word in banned_word:
    if ban_word in text:
        new_symbol = "*" * len(ban_word)
        text = text.replace(ban_word, new_symbol)

print(text)