n = int(input())
for _ in range(1, n + 1):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        exit()

print("All numbers are even.")