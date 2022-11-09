numbers_as_string = list(map(int, input().split(", ")))
find_index_or_no = map(
    lambda x: x if numbers_as_string[x] % 2 == 0 else 'no',
    range(len(numbers_as_string))
)
even_indices = list(filter(lambda a: a != 'no', find_index_or_no))
print(even_indices)