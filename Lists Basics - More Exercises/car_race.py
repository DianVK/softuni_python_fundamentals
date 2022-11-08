sequence_of_numbers = input().split()
left_car = []
right_car = []
right_car_time = 0
middle = 0
left_car_time = 0
for index in range(len(sequence_of_numbers)):
    half_nums = int(len(sequence_of_numbers) / 2)
    left_car = sequence_of_numbers[0:half_nums]
    right_car = sequence_of_numbers[half_nums::]
    right_car.reverse()
    middle = int(right_car[-1])
    right_car.pop(-1)
    break

for index in range(len(left_car)):
    current_index = int(left_car[index])
    if current_index > 0:
        left_car_time += int(left_car[index])
    elif current_index == 0:
        left_car_time = left_car_time * 0.80

for index in range(len(right_car)):
    current_index = int(right_car[index])
    if current_index > 0:
        right_car_time += int(right_car[index])
    elif current_index == 0:
        right_car_time = right_car_time * 0.80

left_car_sum = abs(left_car_time - middle)
right_car_sum = abs(right_car_time - middle)

if left_car_sum < right_car_sum:
    print(f"The winner is left with total time: {left_car_time:.1f}")
elif right_car_sum < left_car_sum:
    print(f"The winner is right with total time: {right_car_time:.1f}")