def tribonacci_seq(num):
    tribonacci_list = [1, 1]
    for number in range(1, num + 1):
        if number == 1 or number == 2:
            print(tribonacci_list[number - 1], end=" ")
            continue
        else:
            add_last_number = 0
            if len(tribonacci_list) > 2:
                add_last_number = tribonacci_list.pop(0)
        print(sum(tribonacci_list) + add_last_number, end=" ")
        tribonacci_list.append(sum(tribonacci_list) + add_last_number)


number_inp = int(input())
tribonacci_seq(number_inp)
