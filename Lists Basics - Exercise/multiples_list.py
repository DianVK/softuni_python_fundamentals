factor = int(input())
count = int(input())
numbers = []
for nums in range(1, count + 1):
    numbers.append(nums * factor)
print(numbers)