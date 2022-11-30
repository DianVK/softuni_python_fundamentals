first_text = input()
second_text = input()

while True:
    if first_text in second_text:
        second_text = second_text.replace(first_text,"")
    else:
        break

print(second_text)