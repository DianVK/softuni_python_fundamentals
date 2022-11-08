def number_comparison(n1, n2, n3):
    smallest_num = 0
    if n1 > n2 and n3 > n2:
        smallest_num = n2
    elif n2 > n1 and n3 > n1:
        smallest_num = n1
    elif n1 > n3 and n2 > n3:
        smallest_num = n3
    return smallest_num


first_number = int(input())
second_number = int(input())
third_number = int(input())
result = number_comparison(first_number,second_number,third_number)
print(result)