first_word = input()
second_word = input()
last_word = first_word

for char in range(len(first_word)):
    first_name = second_word[:char + 1] #[0:char + 1:1]
    second_name = first_word[char + 1:] #[0:len(first_word):1]
    new_word = first_name + second_name
    if new_word == last_word:
        continue
    last_word = new_word
    print(new_word)
