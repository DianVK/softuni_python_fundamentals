def sides(side_, user_):
    for key in force_book:
        if user_ in force_book[key]:
            return
    force_book[side_] = force_book.get(side_, {})
    force_book[side_][user_] = force_book.get(side_)


def change_side(user_, side_):
    for key in force_book:
        if user_ in force_book[key]:
            del force_book[key][user_]
            break
    force_book[side_] = force_book.get(side_, {})
    force_book[side_][user_] = force_book.get(side_)
    print(f"{user_} joins the {side_} side!")


force_command = input()
force_book = {}

while force_command != "Lumpawaroo":

    if " | " in force_command:
        force_command = force_command.split(" | ")
        sides(str(force_command[0]), str(force_command[-1]))
    elif " -> " in force_command:
        force_command = force_command.split(" -> ")
        change_side(str(force_command[0]), str(force_command[-1]))
    force_command = input()

for side in force_book:
    if force_book[side]:
        print(f"Side: {side}, Members: {len(force_book[side])}")
        for name in force_book[side]:
            print(f"! {name}")

# book = {}
# command = input()
# while command != "Lumpawaroo":
#     first_option = " | "
#     second_option = " -> "
#     is_name_in = False
#     if first_option in command:
#         force_side,force_user = command.split(" | ")
#         if force_side not in book:
#             book[force_side] = []
#         for side,name in book.items():
#
#             if force_user in name:
#                 is_name_in = True
#
#         if not is_name_in:
#             book[force_side].append(force_user)
#     elif second_option in command:
#         snd_force_user,snd_force_side = command.split(" -> ")
#         is_name_in = False
#         what_side_is_in = ""
#         for second_option_side,second_option_name in book.items():
#
#             if snd_force_user in second_option_name:
#                 is_name_in = True
#                 what_side_is_in = second_option_side
#                 for item,items in book.items():
#
#                     if is_name_in and item == what_side_is_in:
#                         for i in range(len(items)):
#                             if items[i] == snd_force_user:
#                                 items.pop(i)
#
#         for second_second_sides,second_second_names in book.items():
#             if book[second_second_sides] != what_side_is_in:
#                 if snd_force_user not in book[snd_force_side]:
#                     book[snd_force_side].append(snd_force_user)
#                     print(f"{snd_force_user} joins the {snd_force_side} side!")
#
#     command = input()
#
# for current_side,current_name in book.items():
#     if current_name:
#         print(f"Side: {current_side}, Members: {len(current_name)}")
#         for name in current_name:
#             print(f"! {name}")
