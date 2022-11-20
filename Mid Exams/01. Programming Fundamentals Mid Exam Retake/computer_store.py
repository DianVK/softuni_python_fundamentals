command = input()
total_price_with_taxes = 0
total_price_without_taxes = 0
total_amount_of_taxes = 0
total_price_with_discount = 0
end_price = 0
while command != "special" and command != "regular":
    current_price = float(command)
    if current_price < 0:
        print("Invalid price!")
        command = input()
        continue
    else:
        total_price_without_taxes += current_price
    percentage = current_price * 0.20
    total_amount_of_taxes += percentage
    total_price = current_price + percentage
    command = input()

if command == "special":
    total_price_with_discount = total_price_without_taxes * 0.90

    percentage = total_price_with_discount * 0.20


    end_price = total_price_with_discount + percentage
else:
    percentage = total_price_without_taxes * 0.20

    end_price = total_price_without_taxes + percentage


if end_price == 0:
    print("Invalid order!")
else:
    print(f"Congratulations you've just bought a new computer!\nPrice without taxes: {total_price_without_taxes:.2f}$\n"
          f"Taxes: {total_amount_of_taxes:.2f}$\n-----------\nTotal price: {end_price:.2f}$")