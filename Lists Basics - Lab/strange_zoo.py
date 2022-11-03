tail = input()
body = input()
head = input()

strange_zoo = [tail, body, head]

strange_zoo[0], strange_zoo[2] = strange_zoo[2], strange_zoo[0]

print(strange_zoo)