numbers = int(input())
key_word = input()

words = []
key_words = []

for _ in range(numbers):
    word = input()
    words.append(word)
    if key_word in word:
        key_words.append(word)

print(words)
print(key_words)