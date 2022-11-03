string_of_money = input().split(", ")
beggars_count = int(input())
money_list = []
beggar_index_counter = 0

for beggar in range(beggars_count):
    current_sum = 0
    for index in range(beggar_index_counter, len(string_of_money), beggars_count):
        current_sum += int(string_of_money[index])

    money_list.append(current_sum)
    beggar_index_counter += 1

print(money_list)