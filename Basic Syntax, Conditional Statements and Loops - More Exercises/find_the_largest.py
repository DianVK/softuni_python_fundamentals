<<<<<<< Updated upstream
number = input()
largest_digit = []
for digit in number:
    digit = int(digit)
    largest_digit.append(digit)
largest_digit.sort()
=======
number = input()
largest_digit = []
for digit in number:
    digit = int(digit)
    largest_digit.append(digit)
largest_digit.sort()
>>>>>>> Stashed changes
print(*largest_digit[::-1], sep="")