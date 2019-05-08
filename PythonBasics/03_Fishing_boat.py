budget = int(input())
season = input()
fishers_count = int(input())

price_boat = 0

if season == "Spring":
    price_boat = 3000
    if fishers_count <= 6:
        price_boat -= price_boat * 0.10
    elif 7 <= fishers_count <= 11:
        price_boat -= price_boat * 0.15
    elif fishers_count > 12:
        price_boat -= price_boat * 0.25
elif season == "Summer" or season == "Autumn":
    price_boat = 4200
    if fishers_count <= 6:
        price_boat -= price_boat * 0.10
    elif 7 <= fishers_count <= 11:
        price_boat -= price_boat * 0.15
    elif fishers_count > 12:
        price_boat -= price_boat * 0.25
elif season == "Winter":
    price_boat = 2600
    if fishers_count <= 6:
        price_boat -= price_boat * 0.10
    elif 7 <= fishers_count <= 11:
        price_boat -= price_boat * 0.15
    elif fishers_count > 12:
        price_boat -= price_boat * 0.25

if fishers_count % 2 == 0 and season != "Autumn":
    price_boat -= price_boat * 0.05

money_left = budget - price_boat

if money_left >= 0:
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    print(f"Not enough money! You need {abs(money_left):.2f} leva.")