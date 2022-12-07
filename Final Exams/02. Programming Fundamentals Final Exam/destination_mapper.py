import re
text = input()
text_pattern = re.compile(r'(?P<separator>[\=|\/])(?P<destination>[A-Z][A-Za-z]+)(?P=separator)')
valid_text = text_pattern.finditer(text)
destinations = []
travel_points = 0
for item in valid_text:
    if len(item['destination']) >= 3:
        destinations.append(item['destination'])
        travel_points += len(item['destination'])

print(f"Destinations:", end=" ")
print(*destinations, sep=", ")
print(f"Travel Points: {travel_points}")