def attack(all,atcks):
    destroyed_ships = 0
    for atck in range(len(atcks)):
        current_attack = atcks[atck]
        current_row,current_column = [int(num) for num in current_attack.split("-")]
        for r in range(len(all)):
            if r == current_row:
                now_row = all[current_row]
                if now_row[current_column] > 0:
                    now_row[current_column] -= 1
                    if now_row[current_column] == 0:
                        destroyed_ships += 1

    print(destroyed_ships)


rows = int(input())
all_ships = []
for x in range(rows):
    row = [int(num) for num in input().split()]
    all_ships.append(row)

attackings = input().split()
attack(all_ships, attackings)