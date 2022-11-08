from math import floor


def check_center(sum1,sum2,sum3,sum4):
    first_calculation = sum1 + sum2
    second_calculation = sum3 + sum4
    if first_calculation > second_calculation:
        if abs(x1) + abs(x2) > abs(y1) + abs(y2):
            return f"({y1}, {y2})({x1}, {x2})"
        else:
            return f"({x1}, {x2})({y1}, {y2})"
    elif first_calculation < second_calculation:
        if abs(x3) + abs(x4) > abs(y3) + abs(y4):
            return f"({y3}, {y4})({x3}, {x4})"
        else:
            return f"({x3}, {x4})({y3}, {y4})"
    else:
        if abs(x3) + abs(x4) > abs(y3) + abs(y4):
            return f"({y3}, {y4})({x3}, {x4})"
        else:
            return f"({x3}, {x4})({y3}, {y4})"


x1, x2, y1, y2 = floor(float(input())), floor(float(input())), floor(float(input())), floor(float(input()))
x3, x4, y3, y4 = floor(float(input())), floor(float(input())), floor(float(input())), floor(float(input()))

sum_x = floor(abs(x1) + abs(x2))
sum_y = floor(abs(y1) + abs(y2))
sum_x2 = floor(abs(x3) + abs(x4))
sum_y2 = floor(abs(y3) + abs(y4))

print(check_center(sum_x, sum_y, sum_x2, sum_y2))