def drive(car_to_drive, distance, fuel_needed):
    upper_border_for_kilometers = 100000
    if garage[car_to_drive]['fuel'] >= fuel_needed:
        garage[car_to_drive]['mileage'] += distance
        garage[car_to_drive]['fuel'] -= fuel_needed
        print(f"{car_to_drive} driven for {distance} kilometers. {fuel_needed} liters of fuel consumed.")
        if garage[car_to_drive]['mileage'] >= upper_border_for_kilometers:
            del garage[car_to_drive]
            print(f"Time to sell the {car_to_drive}!")
    else:
        print("Not enough fuel to make that ride")


def refuel(refuel_car, refuel_amount):
    max_fuel_capacity = 75
    liters_refueled = 0
    if garage[refuel_car]['fuel'] + refuel_amount > max_fuel_capacity:
        liters_refueled = max_fuel_capacity - garage[refuel_car]['fuel']
        garage[refuel_car]['fuel'] = max_fuel_capacity
    elif garage[refuel_car]['fuel'] + refuel_amount <= max_fuel_capacity:
        garage[refuel_car]['fuel'] += refuel_amount
        liters_refueled = refuel_amount
    print(f"{refuel_car} refueled with {liters_refueled} liters")


def revert(car_to_revert, reverted_kilometers):
    border_for_mileage = 10000
    if garage[car_to_revert]['mileage'] - reverted_kilometers >= border_for_mileage:
        garage[car_to_revert]['mileage'] -= reverted_kilometers
        print(f"{car_to_revert} mileage decreased by {reverted_kilometers} kilometers")
    elif garage[car_to_revert]['mileage'] - reverted_kilometers < border_for_mileage:
        garage[car_to_revert]['mileage'] = border_for_mileage


garage = {}
number_of_cars = int(input())
for car in range(number_of_cars):
    car_info = input()
    current_car, mileage, fuel = [int(item) if item.isdigit() else item for item in car_info.split("|")]
    garage[current_car] = garage.get(current_car, {'mileage': mileage, 'fuel': fuel})
command = input()

while command != "Stop":
    operation, car_type, *info = [int(item) if item.isdigit() else item for item in command.split(" : ")]
    if operation == "Drive":
        drive(car_type, *info)
    elif operation == "Refuel":
        refuel(car_type, *info)
    elif operation == "Revert":
        revert(car_type, *info)
    command = input()
for key, value in garage.items():
    print(f"{key} -> Mileage: {value['mileage']} kms, Fuel in the tank: {value['fuel']} lt.")