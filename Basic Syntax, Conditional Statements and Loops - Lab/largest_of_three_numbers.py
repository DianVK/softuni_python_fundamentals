import sys

first_number = int(input())
second_number = int(input())
third_number = int(input())
biggest_number = -sys.maxsize

if first_number > biggest_number:
    biggest_number = first_number
if second_number > biggest_number:
    biggest_number = second_number
if third_number > biggest_number:
    biggest_number = third_number

print(biggest_number)