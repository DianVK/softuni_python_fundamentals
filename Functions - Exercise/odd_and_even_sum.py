def odd_and_even_sum(n):
    odd_sum = 0
    even_sum = 0
    for num in range(len(number)):
        current_num = int(number[num])

        if current_num % 2 == 0:
            even_sum += current_num
        else:
            odd_sum += current_num
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = input()
result = odd_and_even_sum(number)
print(result)
