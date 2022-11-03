items_list = input().split("|")
cash = int(input())
bought_item_prices = []
increased_price = []
profit = 0
for item in items_list:
    items_split = item.split("->")
    item_type = items_split[0]
    item_price = float(items_split[1])
    if cash >= item_price:
        if item_type == "Clothes" and item_price <= 50.00 or \
                item_type == "Shoes" and item_price <= 35.00 or \
                item_type == "Accessories" and item_price <= 20.50:
            bought_item_prices.append(item_price)
            cash -= item_price

for price in bought_item_prices:
    profit += price * 0.40
    increased_price.append(price + (price * 0.4))
for price in increased_price:
    print(f"{price:.2f}", end=" ")
print(f"\nProfit: {profit:.2f}")
if sum(increased_price) + cash >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
