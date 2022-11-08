from math import floor
group_size = int(input())
days_adventure = int(input())
total_coints = 0
for day in range(1, days_adventure + 1):
    if day % 10 == 0:
        group_size -= 2
    if day % 15 == 0:
        group_size += 5
    total_coints += 50
    total_coints -= 2 * group_size
    if day % 3 == 0:
        total_coints -= 3 * group_size
    if day % 5 == 0:
        total_coints += 20 * group_size
        if day % 3 == 0:
            total_coints -= 2 * group_size
coins_per_person = floor(total_coints / group_size)
print(f"{group_size} companions received {coins_per_person} coins each.")


