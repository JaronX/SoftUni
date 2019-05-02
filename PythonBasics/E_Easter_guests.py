from math import ceil

guests = int(input())
budget = int(input())

easter_bread = ceil(guests / 3)
eggs = guests * 2
price_easter_bread = easter_bread * 4
price_eggs = eggs * 0.45
total_price = price_easter_bread + price_eggs

if budget >= total_price:
    money_left = budget - total_price
    print(f"""Lyubo bought {easter_bread} Easter bread and {eggs} eggs.
He has {money_left:.2f} lv. left.""")
else:
    money_needed = total_price - budget
    print(f"""Lyubo doesn't have enough money.
He needs {money_needed:.2f} lv. more.""")
