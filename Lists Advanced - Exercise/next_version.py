print(".".join(str(int("".join(input().split("."))) + 1)))

# numbers_as_list = input().split(".")
# numbers_as_int = int("".join(numbers_as_list)) + 1
# numbers_as_str = str(numbers_as_int)
# print(".".join(numbers_as_str))


# numbers = [int(num) for num in input().split(".")]
# version_as_string = ""
# final_version = ""
# for num in numbers:
#     version_as_string += str(num)
#
# version_as_int = int(version_as_string) + 1
# len_of_version = 3
# for num in range(len(str(version_as_int))):
#     current_num = str(version_as_int)
#     len_of_version -= 1
#     final_version += current_num[num]
#     if len_of_version != 0:
#         final_version += "."
#
# print(final_version)