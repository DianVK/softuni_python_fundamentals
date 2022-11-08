def numbers_to_abs_value(nums):
    abs_numbers = []
    for num in numbers:
        num = abs(num)
        abs_numbers.append(num)
    return abs_numbers


numbers = [float(num) for num in input().split()]
print(numbers_to_abs_value(numbers))