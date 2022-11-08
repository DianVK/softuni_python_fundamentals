from math import ceil

people = int(input())
capacity = int(input())

amount = ceil(people / capacity)

print(amount)
