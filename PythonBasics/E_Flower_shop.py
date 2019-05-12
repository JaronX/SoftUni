chrysanthemums = int(input())
roses = int(input())
tulips = int(input())
season = input()
holiday = input()

price_chrysanthemums = 0
price_roses = 0
price_tulips = 0

if season == "Spring" or season == "Summer":
    price_chrysanthemums = 2.00
    price_roses = 4.10
    price_tulips = 2.50
elif season == "Autumn" or season == "Winter":
    price_chrysanthemums = 3.75
    price_roses = 4.50
    price_tulips = 4.15

balance = (chrysanthemums * price_chrysanthemums) + (roses * price_roses) + (tulips * price_tulips)

if holiday == "Y":
    balance += balance * 0.15



if tulips > 7 and season == "Spring":
    balance -= balance * 0.05
elif roses >= 10 and season == "Winter":
    balance -= balance * 0.10

if chrysanthemums + roses + tulips > 20:
    balance -= balance * 0.20

total = balance + 2

print(f"{total:.2f}")