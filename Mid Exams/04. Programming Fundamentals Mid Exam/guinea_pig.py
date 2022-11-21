month = 30
food_per_month = float(input()) * 1000
hay_per_month = float(input()) * 1000
cover_per_month = float(input()) * 1000
weight = float(input()) * 1000
day_counter = 0
for day in range(1, month + 1):
    day_counter += 1
    food_per_month -= 300
    if food_per_month <= 0:
        break
    if day % 2 == 0:
        hay_per_month -= food_per_month * 0.05
    if day % 3 == 0 :
        cover_per_month -= weight / 3

if day_counter == 30 and food_per_month >= 0 and hay_per_month >= 0 and cover_per_month >= 0:
    print(f"Everything is fine! Puppy is happy! Food: {food_per_month/1000:.2f}, Hay: {hay_per_month/1000:.2f}, Cover: {cover_per_month/1000:.2f}.")

if food_per_month < 0 or hay_per_month < 0 or cover_per_month < 0:
    print("Merry must go to the pet store!")