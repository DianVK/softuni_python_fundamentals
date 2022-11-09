employees_happiness = [int(number) for number in input().split()]
happiness_improvement_factor = int(input())

improved_happiness = list(map(lambda el: el * happiness_improvement_factor,employees_happiness))
average_happiness = sum(improved_happiness) // len(improved_happiness)
happy_emp_over_avg = list(filter(lambda h: h > average_happiness, improved_happiness))
happy_emp_below_avg = list(filter(lambda h: h < average_happiness, improved_happiness))

if len(happy_emp_over_avg) > len(happy_emp_below_avg):
    print(f"Score: {len(happy_emp_over_avg)}/{len(happy_emp_over_avg) + len(happy_emp_below_avg)}. Employees are happy!")
else:
    print(f"Score: {len(happy_emp_over_avg)}/{len(happy_emp_over_avg) + len(happy_emp_below_avg)}. Employees are not happy!")