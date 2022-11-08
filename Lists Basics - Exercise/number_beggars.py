money = input().split(", ")
number_beggars = int(input())
list_money = []
counter_beggar = 0
for beggar in range(number_beggars):
    current_sum = 0
    for index in range(counter_beggar, len(money), number_beggars):
        current_sum += int(money[index])
    list_money.append(current_sum)
    counter_beggar += 1

print(list_money)