count_words = int(input())
count_lines = 2 * count_words
all_words = {}

for line in range(count_words):
    head_word = input()
    synonym = input()
    if head_word in all_words:
        all_words[head_word] += f", {synonym}"
    else:
        all_words[head_word] = synonym

for (word, synonyms) in all_words.items():
    print(f"{word} - {synonyms}")