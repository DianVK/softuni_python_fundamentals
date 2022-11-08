def chars_between(chr1,chr2):
    chars_between_list = []
    for char in range(ord(chr1) +1, ord(chr2)):
        chars_between_list.append(chr(char))
    return chars_between_list


first_char = input()
second_char = input()
result = chars_between(first_char, second_char)
print(" ".join(result))