number_of_electrons = int(input())
shell = False
filled_shells = []
shell_num = 1

while not shell:
    max_num_of_electrons = 2*shell_num**2
    if number_of_electrons < max_num_of_electrons:
        filled_shells.append(number_of_electrons)
        break
    number_of_electrons -= max_num_of_electrons
    filled_shells.append(max_num_of_electrons)
    if number_of_electrons <= 0:
        shell = True
        break
    shell_num += 1

print(filled_shells)