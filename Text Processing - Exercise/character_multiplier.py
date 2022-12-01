first_el, second_el = input().split()

total_sum = 0
shorter_word = min(len(first_el), len(second_el))
longer_word = max(len(first_el), len(second_el))

longest_word = ''
if len(first_el) >= len(second_el):
    longest_word = first_el
elif len(second_el) >= len(first_el):
    longest_word = second_el

for pair in range(shorter_word):
    total_sum += ord(first_el[pair]) * ord(second_el[pair])

if first_el != second_el:
    for longer_word_letter in range(shorter_word, longer_word):
        total_sum += ord(longest_word[longer_word_letter])

print(total_sum)