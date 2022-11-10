employees_happiness = list(map(lambda x: int(x), input().split()))
happiness_multiplier = int(input())
multiplied_happiness = list(map(lambda el: el * happiness_multiplier, employees_happiness))
avg_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
over_avg = list(filter(lambda el: el > avg_happiness, multiplied_happiness))
below_avg = list(filter(lambda el: el < avg_happiness, multiplied_happiness))
if len(over_avg) > len(below_avg):
    print(f"Score: {len(over_avg)}/{len(multiplied_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(over_avg)}/{len(multiplied_happiness)}. Employees are not happy!")

# employees_happiness = [int(num) for num in input().split()]
# multiplier = int(input())
# multiplied_happiness = [el * multiplier for el in employees_happiness]
# avg_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
# over_avg = [el for el in multiplied_happiness if el > avg_happiness]
# below_avg = [el for el in multiplied_happiness if el < avg_happiness]
# if len(over_avg) >= len(below_avg):
#     print(f"Score: {len(over_avg)}/{len(multiplied_happiness)}. Employees are happy!")
# else:
#     print(f"Score: {len(over_avg)}/{len(multiplied_happiness)}. Employees are not happy!")