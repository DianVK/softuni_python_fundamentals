population=[int(x) for x in input().split(", ")]
min_limit=int(input())
for i in range(len(population)) :
    wealthiest=max(population)
    if wealthiest <= min_limit:
        break
    poorest=min(population)
    take_inx_rich=population.index(wealthiest)
    take_inx_poor=population.index(poorest)
    difer = min_limit - poorest
    if difer == 0:
        continue
    population[take_inx_poor]+= difer  # Add the difference to the poorest index

    population[take_inx_rich]-= difer  # Subtract the difference from the richest index

if not min(population)>= min_limit:  # If current poverty is greater than or equal to min limit enter
    print("No equal distribution possible")
else :
    print(population)