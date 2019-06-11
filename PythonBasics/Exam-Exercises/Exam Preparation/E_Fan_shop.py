budget = int(input())
n = int(input())

total = 0
product_counter = 0


for i in range(n):
    product = input()

    product_counter += 1

    if product == "hoodie":
        total += 30
    elif product == "keychain":
        total += 4
    elif product == "T-shirt":
        total += 20
    elif product == "flag":
        total += 15
    elif product == "sticker":
        total += 1

diff = abs(budget - total)

if budget >= total:
    print(f"You bought {product_counter} items and left with {diff} lv.")
else:
    print(f"Not enough money, you need {diff} more lv.")