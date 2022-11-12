words = input().split()
special_word = input()
palindrome_words = list(filter(lambda word: word == word[::-1], words))
#palindrome_words = [word for word in words if word == word[::-1]]
print(f"{palindrome_words}\nFound palindrome {palindrome_words.count(special_word)} times")