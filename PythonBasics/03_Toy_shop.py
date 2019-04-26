excursion_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

summ = (puzzles * 2.60) + (dolls * 3) + (bears * 4.10) + (minions * 8.20) + (trucks * 2)
toys = puzzles + dolls + bears + minions + trucks

discount = 0

if toys >= 50:
    discount = (25 / 100) * summ


final_price = summ - discount
rent = (10 / 100) * final_price
profit = final_price - rent

if profit >= excursion_price:
    money = profit - excursion_price
    print(f"Yes! {money:.2f} lv left.")
elif profit < excursion_price:
    money = excursion_price - profit
    print(f"Not enough money! {money:.2f} lv needed.")
