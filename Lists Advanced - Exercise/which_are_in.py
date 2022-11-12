first_text = input().split(", ")
second_text = input().split(", ")

second_text_mix = ""
for word in range(len(second_text)):
    second_text_mix += second_text[word]

# which_are_in = [letter for letter in first_text if letter in second_text_mix]
# print(which_are_in)

which_are_in = list(filter(lambda letter: letter in second_text_mix , first_text))
print(which_are_in)