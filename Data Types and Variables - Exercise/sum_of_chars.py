number = int(input())
sum = 0
for i in range(1, number + 1):
    word = input()
    sum += ord(word)

print(f"The sum equals: {sum}")