def min_max_sum_num(nums):
    return min(nums), max(nums), sum(nums)


numbers = [int(number) for number in input().split()]
min_of_numbers, max_of_numbers, sum_of_numbers = min_max_sum_num(numbers)
print(f"The minimum number is {min_of_numbers}")
print(f"The maximum number is {max_of_numbers}")
print(f"The sum number is: {sum_of_numbers}")