numbers = input().split()
message = input()
new_word = []
for sequence in numbers:
    current_sum = 0
    for index in sequence:
        current_sum += int(index)

    current_sum = current_sum % len(message) #остатък, индекса на съответното място, дори и дължината на message да е по голяма
    new_word.append(message[current_sum])
    message = message.replace(message[current_sum], "", 1) #replace (стар индекс, ново попълнение, брой)

print(*new_word, sep="")