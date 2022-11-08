def calculations_of_numbers(op,num1,num2):
    if op == "multiply":
        return num1 * num2
    elif op == "divide":
        return num1 // num2
    elif op == "add":
        return num1 + num2
    elif op == "subtract":
        return num1 - num2


operator = input()
first_number = int(input())
second_number = int(input())
print(calculations_of_numbers(operator,first_number,second_number))
