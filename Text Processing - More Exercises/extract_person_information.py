number_of_lines = int(input())
for _ in range(number_of_lines):
    text = input()
    name_start = text.index("@")
    name_end = text.index("|")
    age_start = text.index("#")
    age_end = text.index("*")
    name = text[name_start +1:name_end]
    age = text[age_start+1:age_end]
    print(f"{name} is {age} years old.")