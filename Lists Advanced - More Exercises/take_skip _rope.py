hidden_message = input()

numbers_list = list(filter(lambda x: x.isdigit(), hidden_message))
non_numbers_list = list(filter(lambda x: not x.isdigit(), hidden_message))

take_list = [int(numbers_list[x]) for x in range(len(numbers_list)) if x % 2 == 0]
skip_list = [int(numbers_list[x]) for x in range(len(numbers_list)) if not x % 2 == 0]

deciphered_message = []
while take_list:
    for el in range(len(take_list)):
        how_many_to_take = take_list[0]
        if how_many_to_take > 0:
            for ninja in range(1, how_many_to_take + 1):
                if non_numbers_list:
                    deciphered_message.append(non_numbers_list[0])
                    non_numbers_list.pop(0)
        take_list.pop(0)

        for elm in range(len(skip_list)):
            how_many_to_remove = skip_list[0]
            if how_many_to_remove >= 0:
                for rem in range(1, how_many_to_remove + 1):
                    if non_numbers_list:
                        non_numbers_list.pop(0)
                    else:
                        break
                skip_list.pop(0)
                break
            break


print("".join(deciphered_message))