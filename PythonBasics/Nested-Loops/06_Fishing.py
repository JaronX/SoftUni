max_fish = int(input())
name_fish = input()

fish_counter = 0
price_for_fish = 0
budget = 0

while not name_fish == "Stop":

    kilograms_fish = float(input())
    fish_counter += 1

    for letter in name_fish:
        price_for_fish += (ord(letter)) / kilograms_fish

    if fish_counter % 3 == 0:
        budget += price_for_fish
    else:
        budget -= price_for_fish


    if fish_counter == max_fish:
        print(f"Lyubo fulfilled the quota!")
        break

    price_for_fish = 0
    name_fish = input()

if budget >= 0:
    print(f"Lyubo's profit from {fish_counter} fishes is {budget:.2f} leva.")
else:
    print(f"Lyubo lost {abs(budget):.2f} leva today.")