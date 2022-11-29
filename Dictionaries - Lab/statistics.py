command = input()
products = {}
while command != "statistics":
    key,value = command.split(": ")
    if key in products:
        products[key] += int(value)
    else:
        products[key] = int(value)

    command = input()

print("Products in stock:")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")

print(f"Total Products: {len(products.keys())}\nTotal Quantity: {sum(products.values())}")