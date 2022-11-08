def rounding_numbers(num):
    rounded_numbers = []
    for number in num:
        rounded_number = round(number)
        rounded_numbers.append(rounded_number)
    return rounded_numbers


numbers = [float(nums) for nums in input().split()]
print(rounding_numbers(numbers))