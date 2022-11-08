word = input()
upper_letter = []

for i in range(len(word)):
    if word[i].isupper():
        upper_letter.append(i)

print(upper_letter)