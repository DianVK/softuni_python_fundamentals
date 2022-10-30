upper_words = {
    "upper letters":["CODING" , "DOG" , "CAT" , "MOVIE"]
}
lower_words = {
    "lower letters":["coding" , "dog" , "cat" , "movie"]
}

command = input()
total_coffees_needed = 0
while command != "END":
    if command in upper_words["upper letters"]:
        total_coffees_needed += 2
    if command in lower_words["lower letters"]:
        total_coffees_needed += 1
    command = input()

if total_coffees_needed > 5:
    print("You need extra sleep")
else:
    print(total_coffees_needed)