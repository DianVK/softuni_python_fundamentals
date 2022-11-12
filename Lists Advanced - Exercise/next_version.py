# numbers_as_list = input().split(".")
# numbers_as_int = int("".join(numbers_as_list)) + 1
# numbers_as_str = str(numbers_as_int)
# print(".".join(numbers_as_str))
print(".".join(str(int("".join(input().split("."))) + 1)))