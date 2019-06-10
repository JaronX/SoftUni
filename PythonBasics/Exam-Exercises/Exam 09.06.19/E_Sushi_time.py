import math

type_sushi = input()
restaurant = input()
portion = int(input())
order = input()

price_per_portion = 0
order_for_home = 0.20

if type_sushi == "sashimi":
    if restaurant == "Sushi Zone":
        price_per_portion = 4.99
    elif restaurant == "Sushi Time":
        price_per_portion = 5.49
    elif restaurant == "Sushi Bar":
        price_per_portion = 5.25
    elif restaurant == "Asian Pub":
        price_per_portion = 4.50


elif type_sushi == "maki":
    if restaurant == "Sushi Zone":
        price_per_portion = 5.29
    elif restaurant == "Sushi Time":
        price_per_portion = 4.69
    elif restaurant == "Sushi Bar":
        price_per_portion = 5.55
    elif restaurant == "Asian Pub":
        price_per_portion = 4.80


elif type_sushi == "uramaki":
    if restaurant == "Sushi Zone":
        price_per_portion = 5.99
    elif restaurant == "Sushi Time":
        price_per_portion = 4.49
    elif restaurant == "Sushi Bar":
        price_per_portion = 6.25
    elif restaurant == "Asian Pub":
        price_per_portion = 5.50


elif type_sushi == "temaki":
    if restaurant == "Sushi Zone":
        price_per_portion = 4.29
    elif restaurant == "Sushi Time":
        price_per_portion = 5.19
    elif restaurant == "Sushi Bar":
        price_per_portion = 4.75
    elif restaurant == "Asian Pub":
        price_per_portion = 5.50


price = portion * price_per_portion

if order == "Y":
    price += order_for_home * price
else:
    pass

if restaurant == "Sushi Zone" or restaurant == "Sushi Time" or restaurant == "Sushi Bar" or restaurant == "Asian Pub":
    print(f"Total price: {math.ceil(price)} lv.")
else:
    print(f"{restaurant} is invalid restaurant!")