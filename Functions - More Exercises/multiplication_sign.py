def check_numbers(first, second, third):
    if (first > 0 and second > 0 and third > 0) or\
            (first > 0 and second < 0 and third < 0) or \
            (second > 0 and first < 0 and third < 0) or \
            (third > 0 and first < 0 and second < 0):
        return "positive"
    elif first < 0 or second < 0 or third < 0:
        return "negative"
    elif first == 0 or second == 0 or third == 0:
        return "zero"


first_num = int(input())
second_num = int(input())
third_num = int(input())
print(check_numbers(first_num, second_num, third_num))