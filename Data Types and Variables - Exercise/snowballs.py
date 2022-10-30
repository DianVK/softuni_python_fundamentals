snowballs = int(input())
highest_valued = 0
highest_weigh = 0
highest_time = 0
highest_quality = 0
for i in range(1, snowballs + 1):
    weight = int(input())
    time = int(input())
    quality = int(input())
    sum = (weight / time) ** quality
    if sum > highest_valued:
        highest_valued = sum
        highest_weigh = weight
        highest_time = time
        highest_quality = quality

print(f"{highest_weigh} : {highest_time} = {int(highest_valued)} ({highest_quality})")