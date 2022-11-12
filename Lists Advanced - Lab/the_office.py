employees_happiness = [int(num) for num in input().split()]
happiness_multiplier = int(input())
multiplied_happiness = list(map(lambda num: num * happiness_multiplier, employees_happiness))
avg_happiness = sum(multiplied_happiness) / len(multiplied_happiness)
happy_count = list(filter(lambda num: num > avg_happiness, multiplied_happiness))
unhappy_count = list(filter(lambda num: num < avg_happiness, multiplied_happiness))
print(f"Score: {len(happy_count)}/{len(multiplied_happiness)}. Employees are happy!"
      if len(happy_count) >= len(unhappy_count) else f"Score: {len(happy_count)}/{len(multiplied_happiness)}. Employees are not happy!")

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