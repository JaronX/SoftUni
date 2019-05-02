guests = int(input())
price_couvert = float(input())
budget = float(input())

if guests < 10:
    couvert_discount = price_couvert
elif 10 <= guests <= 15:
    couvert_discount = price_couvert * 0.85
elif 16 <= guests <= 20:
    couvert_discount = price_couvert * 0.80
else:
    couvert_discount = price_couvert * 0.75

cake_price = 0.10 * budget
total_summ = guests * couvert_discount + cake_price

if budget > total_summ:
    money_left = budget - total_summ
    print(f"It is party time! {money_left:.2f} leva left.")
else:
    money_needed = total_summ - budget
    print(f"No party! {money_needed:.2f} leva needed.")