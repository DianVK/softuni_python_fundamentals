number = int(input())
even = []
odd = []
negative = []
positive = []

for num in range(number):
    number = int(input())
    if number % 2 == 0:
        even.append(number)
    if number % 2 != 0:
        odd.append(number)
    if number >= 0:
        positive.append(number)
    if number < 0:
        negative.append(number)

command = input()
if command == "even":
    print(even)
elif command == "odd":
    print(odd)
elif command == "negative":
    print(negative)
elif command == "positive":
    print(positive)