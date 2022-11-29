def check_for_items():
    global legendary_item_found
    if legendary_items["shards"] >= 250:
        legendary_items["shards"] -= 250
        print("Shadowmourne obtained!")

    elif legendary_items["fragments"] >= 250:
        legendary_items["fragments"] -= 250
        print("Valanyr obtained!")

    elif legendary_items["motes"] >= 250:
        legendary_items["motes"] -= 250
        print("Dragonwrath obtained!")
    legendary_item_found = True


legendary_items = {"shards": 0,
                   "fragments": 0,
                   "motes": 0
                   }

legendary_item_found = False

while not legendary_item_found:
    loot_table = input().split()

    for loot in range(0, len(loot_table), 2):
        quantity = int(loot_table[loot])
        current_shard = loot_table[loot + 1].lower()

        if current_shard in legendary_items:
            legendary_items[current_shard] += quantity

        elif current_shard not in legendary_items:
            legendary_items[current_shard] = quantity

        check_for_items()
        if legendary_item_found:
            break


for current_shard in legendary_items:
    print(f"{current_shard}: {legendary_items[current_shard]}")