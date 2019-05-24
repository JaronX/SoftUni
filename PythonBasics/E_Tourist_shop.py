budget = float(input())

balance = 0
product_counter = 0

while balance <= budget:
    name_product = input()

    if name_product == "Stop":
        break

    price_product = float(input())

    product_counter += 1

    if product_counter % 3 == 0:
        price_product *= 0.50

    balance += price_product

if name_product == "Stop":
    print(f"You bought {product_counter} products for {balance:.2f} leva.")
else:
    needed_money = balance - budget
    print(f"""You don't have enough money!
You need {needed_money:.2f} leva!""")
