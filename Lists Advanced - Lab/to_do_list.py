command = input()
to_do_list = [0] * 10
while command != "End":
    importance, task = command.split("-")
    importance = int(importance) - 1
    to_do_list[importance] = task
    command = input()

#print([item for item in to_do_list if item != 0])
print(list(filter(lambda x: x != 0, to_do_list)))