import re
text = input()
searched_word = input()
word_pattern = rf"\b{searched_word}\b"
count_words = re.findall(searched_word,text, re.IGNORECASE)
print(len(count_words))