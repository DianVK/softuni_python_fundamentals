sequence = input()
for char in range(len(sequence)):
    if sequence[char] == ":":
        print(f"{sequence[char]}{sequence[char + 1]}")