items = input().split()
stock = {}
for el in range(0, len(items), 2):
    key = items[el]
    value = items[el + 1]
    stock[key] = int(value)

check_for_stock = input().split()
for item in check_for_stock:
    if item in stock:
        print(f"We have {stock[item]} of {item} left")
    else:
        print(f"Sorry, we don't have {item}")