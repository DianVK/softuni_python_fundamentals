list_of_items = input()
list_to_remove = "aoueiAOUEI"
result = [letter for letter in list_of_items if letter not in list_to_remove]
print("".join(result))

# text = input()
# string_to_remove = "aoueiAOUEI"
# cleared_text = list(filter(lambda x: x not in string_to_remove, text))
# print(*cleared_text, sep="")