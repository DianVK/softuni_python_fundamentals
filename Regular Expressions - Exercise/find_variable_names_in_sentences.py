import re
text = input()
searched_word = input()
word_pattern = rf"\b{searched_word}\b"
count_words = re.findall(word_pattern,text, re.IGNORECASE)
print(len(count_words))