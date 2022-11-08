def find_factorial(first_num, second_num):
    result_first_number, result_second_number = 1, 1
    for first_digit in range(1, first_num + 1):
        result_first_number *= first_digit
    for second_digit in range(1, second_num + 1):
        result_second_number *= second_digit
    return result_first_number / result_second_number


first_number = int(input())
second_number = int(input())
print(f"{find_factorial(first_number, second_number):.2f}")