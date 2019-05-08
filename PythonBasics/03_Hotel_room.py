month = input()
nights = int(input())

price_studio = 0
price_apartment = 0

if (month == "May") or (month == "October"):
    price_studio = 50
    if 7 < nights <= 14:
        price_studio -= price_studio * 0.05
    elif nights > 14:
        price_studio -= price_studio * 0.30
elif (month == "June") or (month == "September"):
    price_studio = 75.20
    if nights > 14:
        price_studio -= price_studio * 0.20
elif (month == "July") or (month == "August"):
    price_studio = 76

if (month == "May") or (month == "October"):
    price_apartment = 65
    if nights > 14:
        price_apartment -= price_apartment * 0.10
elif (month == "June") or (month == "September"):
    price_apartment = 68.70
    if nights > 14:
        price_apartment -= price_apartment * 0.10
elif (month == "July") or (month == "August"):
    price_apartment = 77
    if nights > 14:
        price_apartment -= price_apartment * 0.10

total_studio = price_studio * nights
total_apartment = price_apartment * nights

print(f"""Apartment: {total_apartment:.2f} lv.
Studio: {total_studio:.2f} lv.""")