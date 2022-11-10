numbers_as_string = list(map(lambda el: int(el), input().split(", ")))
# even_numbers_indices = [index for index in range(len(numbers_as_string)) if numbers_as_string[index] % 2 == 0]
even_numbers_indices = list(filter(lambda index: numbers_as_string[index] % 2 == 0, range(len(numbers_as_string))))
print(even_numbers_indices)

# numbers_as_string = list(map(int, input().split(", ")))
# find_index_or_no = map(
#     lambda x: x if numbers_as_string[x] % 2 == 0 else 'no',
#     range(len(numbers_as_string))
# )
# even_indices = list(filter(lambda a: a != 'no', find_index_or_no))
# print(even_indices)