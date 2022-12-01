tickets = input().replace(" ", "")
tickets = tickets.split(",")
special_symbols = ["@", "#", "$", "^"]

for ticket in tickets:
    jackpot_win = False
    normal_win = False
    symbols = 0
    if len(ticket) == 20:
        first_half = ticket[:len(ticket) // 2]
        second_half = ticket[len(ticket) // 2:]
        for symbol in special_symbols:
            if 20 * symbol in ticket:
                jackpot_win = True
                break

            elif 6 * symbol in first_half and 6 * symbol in second_half:
                symbols = 6
                for index in range(7, 11):
                    if index * symbol in first_half and index * symbol in second_half:
                        symbols += 1
                normal_win = True
                break

        if normal_win:
            print(f'ticket "{ticket}" - {symbols}{symbol}')
        elif jackpot_win:
            print(f'ticket "{ticket}" - 10{symbol} Jackpot!')
        elif not normal_win and not jackpot_win:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")


# tickets = input().split(", ")
# special_symbols = "@#$^"
# for ticket in range(len(tickets)):
#     if len(tickets[ticket]) == 20:
#         left_half_special_elements = []
#         right_half_special_elements = []
#         current_ticket = tickets[ticket]
#         half_ticket = int(len(current_ticket) / 2)
#         left_half = current_ticket[0 : half_ticket]
#         right_half = current_ticket[half_ticket : -1]
#         for el_in_left in range(len(left_half)):
#             current_el = left_half[el_in_left]
#             if current_el in special_symbols:
#                 left_half_special_elements.append(current_el)
#         for el_in_left in range(len(right_half)):
#             current_el = right_half[el_in_left]
#             if current_el in special_symbols:
#                 right_half_special_elements.append(current_el)
#         if (len(left_half_special_elements) == 6 and len(right_half_special_elements) == 6) or (len(left_half_special_elements) == 10 and len(right_half_special_elements) == 10):
#             current_special_el = ""
#             all_special_elements_true = True
#             for el in left_half_special_elements:
#                 if current_special_el == "":
#                     current_special_el = el
#                 if el != current_special_el:
#                     all_special_elements_true = False
#             current_special_el = ""
#             for el in right_half_special_elements:
#                 if current_special_el == "":
#                     current_special_el = el
#                 if el != current_special_el:
#                     all_special_elements_true = False
#             if all_special_elements_true:
#                 print(f'ticket "{current_ticket}" - {len(left_half_special_elements)}{current_special_el}')
