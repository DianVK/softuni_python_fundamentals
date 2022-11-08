<<<<<<< Updated upstream
n = int(input())
sum = 0
for i in range(1, n + 1):
    liters = int(input())
    sum += liters
    if sum > 255:
        sum -= liters
        print("Insufficient capacity!")
=======
n = int(input())
sum = 0
for i in range(1, n + 1):
    liters = int(input())
    sum += liters
    if sum > 255:
        sum -= liters
        print("Insufficient capacity!")
>>>>>>> Stashed changes
print(sum)