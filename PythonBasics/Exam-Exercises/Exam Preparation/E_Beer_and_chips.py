from math import ceil

name = input()
budget = float(input())
bottles_of_beer = int(input())
packets_of_chips = int(input())

total_for_beer = 1.20 * bottles_of_beer
price_per_chips = 0.45 * total_for_beer
total_for_chips = ceil(price_per_chips * (packets_of_chips))

total = total_for_beer + total_for_chips

if budget >= total:
    money_left = budget - total
    print(f"{name} bought a snack and has {money_left:.2f} leva left.")
else:
    money_needed = total - budget
    print(f"{name} needs {money_needed:.2f} more leva!")