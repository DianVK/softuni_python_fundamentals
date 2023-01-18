number_pieces = int(input())
pieces = []
composers = []
keys = []
for el in range(number_pieces):
    current_piece = input()
    piece, composer, key = current_piece.split("|")
    pieces.append(piece)
    composers.append(composer)
    keys.append(key)

command = input()
while command != "Stop":
    current_command = command.split("|")
    action = current_command[0]
    if action == "Add":
        piece, composer, key = current_command[1], current_command[2], current_command[3]
        if piece in pieces:
            print(f"{piece} is already in the collection!")
        else:
            print(f"{piece} by {composer} in {key} added to the collection!")
            pieces.append(piece)
            composers.append(composer)
            keys.append(key)
    elif action == "Remove":
        piece = current_command[1]
        if piece in pieces:
            piece_index = pieces.index(piece)
            pieces.pop(piece_index)
            composers.pop(piece_index)
            keys.pop(piece_index)
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")

    elif action == "ChangeKey":
        piece, new_key = current_command[1], current_command[2]
        if piece in pieces:
            piece_index = pieces.index(piece)
            keys[piece_index] = new_key
            print(f"Changed the key of {piece} to {new_key}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    command = input()

for index in range(len(pieces)):
    current_piece = pieces[index]
    current_composer = composers[index]
    current_key = keys[index]

    print(f"{current_piece} -> Composer: {current_composer}, Key: {current_key}")
