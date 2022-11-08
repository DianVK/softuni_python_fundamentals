<<<<<<< Updated upstream
n = int(input())
positive = []
negative = []
for i in range(1, n + 1):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)


print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")
=======
n = int(input())
positive = []
negative = []
for i in range(1, n + 1):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)


print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")
>>>>>>> Stashed changes
