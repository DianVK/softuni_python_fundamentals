from math import floor


def check_center(sum1,sum2):
    if sum1 <= sum2:
        return f"({x1}, {x2})"
    elif sum2 <= sum1:
        return f"({y1}, {y2})"


x1 = floor(float(input()))
x2 = floor(float(input()))
y1 = floor(float(input()))
y2 = floor(float(input()))

sum_x = floor(abs(x1) + abs(x2))
sum_y = floor(abs(y1) + abs(y2))

print(check_center(sum_x, sum_y))