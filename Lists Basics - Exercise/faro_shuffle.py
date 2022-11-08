cards = input().split()
number_of_shuffles = int(input())
left_half = []
right_half = []

for index in range(number_of_shuffles):
    new_cards = []
    half_cards = int(len(cards) / 2)
    left_half = cards[0:half_cards]
    right_half = cards[half_cards::]
    for card in range(len(left_half)):
        new_cards.append(left_half[card])
        new_cards.append(right_half[card])
    cards = new_cards

print(cards)