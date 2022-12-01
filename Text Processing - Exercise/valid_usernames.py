import string

usernames = input().split(", ")
for user in usernames:
    check_symbols = "-_"
    if 3 <= len(user) <= 16:
        for letter in user:
            if letter not in check_symbols + string.ascii_letters + string.digits:
                break
        else:
            print(user)