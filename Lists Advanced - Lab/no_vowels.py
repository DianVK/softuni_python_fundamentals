list_of_items = input()
list_to_remove = "aoueiAOUEI"
result = [letter for letter in list_of_items if letter not in list_to_remove]
print("".join(result))