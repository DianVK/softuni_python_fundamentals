def price_calculation(item,count):
    if item == "coffee":
        return 1.50 * count
    if item == "coke":
        return 1.40 * count
    if item == "water":
        return count
    if item == "snacks":
        return 2.00 * count


product = input()
quantity = int(input())
result = price_calculation(product, quantity)
print(f"{result:.2f}")