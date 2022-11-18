class Party:
    def __init__(self):
        self.people = []


party_time = Party()

names = input()
while names != "End":
    party_time.people.append(names)
    names = input()

print(f"Going: {', '.join(party_time.people)}\nTotal: {len(party_time.people)}")