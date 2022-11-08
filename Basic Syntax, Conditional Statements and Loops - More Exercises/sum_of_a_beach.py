word = input().lower()
words_to_check = "water", "fish", "sun" , "sand"
counter = 0
counter += word.count("sand")
counter += word.count("water")
counter += word.count("fish")
counter += word.count("sun")
print(counter)