import re
command = input()
pattern = re.compile(r'(%)(?P<customer>[A-Z][a-z]+)(%)([^\|\$\%\.]*)(<)'
                     r'(?P<product>\w+)(>)([^\|\$\%\.]*)(\|)'
                     r'(?P<count>\d+)(\|)([^\|\$\%\.]*)'
                     r'(?P<price>[1-9]+[.0-9]*)\$')
valid_income = []
total_income = 0

while command != "end of shift":
    matches = pattern.finditer(command)
    for match in matches:
        name, product = match['customer'], match['product']
        money_spent = int(match['count']) * float(match['price'])
        total_income += money_spent
        valid_income.append(f"{name}: {product} - {money_spent:.2f}")
    command = input()

for customers in valid_income:
    print(customers)

print(f"Total income: {total_income:.2f}")