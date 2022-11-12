numbers = [int(num) for num in input().split(", ")]

positive = list(filter(lambda num: num >= 0, numbers))
negative = list(filter(lambda num: num < 0, numbers))
even = list(filter(lambda num: num % 2 == 0, numbers))
odd = list(filter(lambda num: num % 2 != 0, numbers))

print("Positive:", ', '.join(map(str, positive)))
print("Negative:", ', '.join(map(str, negative)))
print("Even:", ', '.join(map(str, even)))
print("Odd:", ', '.join(map(str, odd)))