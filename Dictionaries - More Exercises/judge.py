contest = input()

database = {
    'individuals': {},
    'contests': {}
}

while contest != "no more time":
    username, course, points = [int(name) if name.isdigit() else name for name in contest.split(" -> ")]
    database['contests'][course] = database['contests'].get(course, {})
    database['contests'][course][username] = database['contests'][course].get(username, 0)
    if database['contests'][course][username] < points:
        database['contests'][course][username] = points
    contest = input()
for exams in database['contests']:
    for names in database['contests'][exams]:
        database['individuals'][names] = database['individuals'].get(names, 0) + database['contests'][exams][names]

for submission in database['contests']:
    print(f"{submission}: {len(database['contests'][submission])} participants")
    for position, (name, points) in enumerate(
            sorted(database['contests'][submission].items(), key=lambda item: (-item[1], item[0])), 1):
        print(f"{position}. {name} <::> {points}")
print("Individual standings:")
for position, (name, points) in enumerate(
        sorted(database['individuals'].items(), key=lambda item: (-item[1], item[0])), 1):
    print(f"{position}. {name} -> {points}")