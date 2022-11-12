text = input()
print(*[text[letter] for letter in range(len(text)) if text[letter] not in str("aoueiAOUEI")], sep="")

# text = input()
# letters_to_remove = "aoueiAOUEI"
# new_text = []
# for letter in range(len(text)):
#     if text[letter] not in letters_to_remove:
#         new_text.append(text[letter])
# print(*new_text, sep="")