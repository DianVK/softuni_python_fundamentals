def loading_percentage(percentage):
    loading_percent = [".",".",".",".",".",".",".",".",".","."]
    new_loading_list = []
    first_digit = 0
    for first_digit in percentage:
        first_digit = int(first_digit)
        break

    dots_to_percent = loading_percent[:first_digit]
    dots_left = loading_percent[first_digit::]
    for char in range(len(dots_to_percent)):
        if dots_to_percent[char] == ".":
            dots_to_percent[char] = "%"
    new_loading_list = dots_to_percent + dots_left
    updated_list = "".join(new_loading_list)
    return updated_list


percent = input()
if percent != "100":
    print(f"{percent}% [{loading_percentage(percent)}]\nStill loading...")
else:
    print(f"100% Complete!\n[%%%%%%%%%%]")