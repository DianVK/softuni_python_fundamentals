<<<<<<< Updated upstream
cards = input().split()
number_of_shuffles = int(input())
left_deck = []
right_deck = []

for shuffle in range(number_of_shuffles):
    current_deck = []
    half_deck = int(len(cards) / 2)
    left_deck = cards[0:half_deck]
    right_deck = cards[half_deck::]
    for card in range(len(left_deck)):
        current_deck.append(left_deck[card])
        current_deck.append(right_deck[card])
    cards = current_deck

=======
cards = input().split()
number_of_shuffles = int(input())
left_deck = []
right_deck = []

for shuffle in range(number_of_shuffles):
    current_deck = []
    half_deck = int(len(cards) / 2)
    left_deck = cards[0:half_deck]
    right_deck = cards[half_deck::]
    for card in range(len(left_deck)):
        current_deck.append(left_deck[card])
        current_deck.append(right_deck[card])
    cards = current_deck

>>>>>>> Stashed changes
print(cards)