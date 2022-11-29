words = [word.lower() for word in input().split()]

odd_items = dict()

for word in words:
    if word not in odd_items:
        odd_items[word] = 1

    elif word in odd_items:
        odd_items[word] += 1

for word in odd_items:
    if odd_items[word] % 2 != 0:
        print(f"{word}", end=" ")