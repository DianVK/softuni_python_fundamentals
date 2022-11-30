sequence = input().split()

new_sequence = ""

for word in range(len(sequence)):
    repeat_count = len(sequence)
    for repeat in range(repeat_count):
        new_sequence += sequence[word]

print(new_sequence)