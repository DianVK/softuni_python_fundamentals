words = input().split()
special_word = input()
palindrome_words = [word for word in words if word == word[::-1]]
print(palindrome_words)
print(f"Found palindrome {palindrome_words.count(special_word)} times")