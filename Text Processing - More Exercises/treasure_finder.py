secret_key = input().split()
index_of_keys = 0
encrypted_text = input()
decrypted_text = ""
all_results = []
while encrypted_text != "find":
    result = ''
    for character in encrypted_text:
        if index_of_keys >= len(secret_key):
            index_of_keys = 0
        result += chr(ord(character) - int(secret_key[index_of_keys]))
        index_of_keys += 1

    all_results.append(result)
    result, index_of_keys = '', 0
    encrypted_text = input()

for location in all_results:
    start_index_material = location.index("&") + 1
    end_index_material = location.index("&", start_index_material + 1)
    start_coordinates, end_coordinates = location.index("<") + 1, location.index(">")
    print(f"Found {location[start_index_material:end_index_material]} at {location[start_coordinates:end_coordinates]}")