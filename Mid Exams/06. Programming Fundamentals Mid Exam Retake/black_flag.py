count_days = int(input())
plunder_for_day = int(input())
expected_plunder = float(input())
total_plunder = 0

for day in range(1, count_days + 1):
    total_plunder += plunder_for_day
    if day % 3 == 0:
        total_plunder += plunder_for_day * 0.50
    if day % 5 == 0:
        total_plunder = total_plunder * 0.70

if total_plunder >= expected_plunder:
    print(f"Ahoy! {total_plunder:.2f} plunder gained.")
else:
    percentage = (total_plunder / expected_plunder) * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")