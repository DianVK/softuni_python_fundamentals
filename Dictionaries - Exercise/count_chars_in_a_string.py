words = input().split()
all_sequences = {}
if len(words) == 1:
    for char in range(len(words)):
        current_char = words[char]
        if current_char not in all_sequences:
            all_sequences[current_char] = 1
        else:
            all_sequences[current_char] += 1
else:

    for chr in words:
        for letter in range(len(chr)):
            current_chr = chr[letter]
            if current_chr not in all_sequences:
                all_sequences[current_chr] = 1
            else:
                all_sequences[current_chr] += 1

for item in all_sequences.items():
    print(f"{item[0]} -> {item[1]}")