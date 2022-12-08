import re
text = input()
pattern = re.compile(r'([@|#])(?P<first_valid>[A-Za-z]{3,})\1{2}(?P<second_valid>[A-Za-z]{3,})\1')
valid_words = pattern.finditer(text)
mirror_pairs = {
    "mirror words": [],
    "invalid pairs": []
}

for valid in valid_words:
    first_word = valid['first_valid']
    second_word = valid['second_valid']
    if second_word[::-1] == first_word and first_word[::-1] == second_word:
        mirror_pairs['mirror words'].append(f"{first_word} <=> {second_word}")
    else:
        mirror_pairs['invalid pairs'].append(f"{first_word} <=> {second_word}")

if not mirror_pairs['mirror words'] and not mirror_pairs['invalid pairs']:
    print(f"No word pairs found!")

if mirror_pairs['mirror words'] or mirror_pairs['invalid pairs']:
    valid_pairs = len(mirror_pairs['mirror words'] + mirror_pairs['invalid pairs'])
    print(f"{valid_pairs} word pairs found!")

if not mirror_pairs['mirror words']:
    print("No mirror words!")

if mirror_pairs['mirror words']:
    print("The mirror words are:")
    print(', '.join(mirror_pairs['mirror words']))