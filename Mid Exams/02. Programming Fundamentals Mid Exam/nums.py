nums = [int(num) for num in input().split()]
sorted_nums = list(sorted(nums, reverse=True))

average_num = sum(sorted_nums) / len(sorted_nums)
greater_nums = []
for num in range(len(sorted_nums)):
    current_num = int(sorted_nums[num])
    if current_num > average_num:
        greater_nums.append(current_num)

for num in range(len(greater_nums)):
    if len(greater_nums) > 5:
        greater_nums.pop(-1)

if not greater_nums:
    print("No")
else:
    print(*greater_nums)