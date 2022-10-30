divisor = int(input())
boundary = int(input())
for i in range(boundary, 0, -1):
    if i % divisor == 0:
        print(i)
        exit()