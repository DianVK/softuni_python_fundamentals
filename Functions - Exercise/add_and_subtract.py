def sum_numbers(n1,n2):
    return n1 + n2


def subtract(sum_n,n3):
    return sum_n - n3


first_number = int(input())
second_number = int(input())
third_number = int(input())
result1 = sum_numbers(first_number,second_number)
result2 = subtract(sum_numbers(first_number,second_number),third_number)

print(result2)