def swap(indx1, indx2, lst):
    lst[indx1], lst[indx2] = lst[indx2], lst[indx1]


def multiply(indx1, indx2, lst):
    product = lst[indx1] * lst[indx2]
    lst[indx1] = product


def decrease(lst):
    for el in range(len(lst)):
        numbers[el] -= 1


numbers = [int(num) for num in input().split()]
command = input()
while command != "end":
    current_command = command.split()
    action = current_command[0]
    if action == "swap":
        index1 = int(current_command[1])
        index2 = int(current_command[2])
        swap(index1,index2,numbers)
    elif action == "multiply":
        index1 = int(current_command[1])
        index2 = int(current_command[2])
        multiply(index1,index2,numbers)
    elif action == "decrease":
        decrease(numbers)
    command = input()

numbers_to_str = list(map(lambda x: str(x),numbers))
print(", ".join(numbers_to_str))