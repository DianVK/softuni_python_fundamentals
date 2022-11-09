names = input().split(", ")
result = sorted(names, key=lambda name: (-len(name), name))
print(result)