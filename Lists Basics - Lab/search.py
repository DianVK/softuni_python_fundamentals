number = int(input())
key = input()
all_words = []
key_words = []

for num in range(number):
    words = input()
    all_words.append(words)
    if key in words:
        key_words.append(words)

print(all_words)
print(key_words)