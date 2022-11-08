def even_numbers(num):
    return num % 2 == 0


numbers = [int(number) for number in input().split()]

result = filter(even_numbers, numbers)
print(list(result))