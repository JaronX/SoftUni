budget = float(input())
city = input()
nights = int(input())

price_per_night = 0
tickets = 0
balance = 0

if city == "Cairo":
    price_per_night = 250
    tickets = 600
elif city == "Paris":
    price_per_night = 150
    tickets = 350
elif city == "Lima":
    price_per_night = 400
    tickets = 850
elif city == "New York":
    price_per_night = 300
    tickets = 650
elif city == "Tokyo":
    price_per_night = 350
    tickets = 700

balance = (nights * (price_per_night * 2)) + tickets

if 1 <= nights <= 4:
    if city == "Cairo" or city == "New York":
        balance -= balance * 0.03

elif 5 <= nights <= 9:
    if city == "Cairo" or city == "New York":
        balance -= balance * 0.05
    elif city == "Paris":
        balance -= balance * 0.07

elif 10 <= nights <= 24:
    if city == "Cairo":
        balance -= balance * 0.10
    elif city == "New York" or city == "Paris" or city == "Tokyo":
        balance -= balance * 0.12

elif 25 <= nights <= 49:
    if city == "Cairo" or city == "Tokyo":
        balance -= balance * 0.17
    elif city == "New York" or city == "Lima":
        balance -= balance * 0.19
    elif city == "Paris":
        balance -= balance * 0.22

else:
    balance -= balance * 0.30

if budget > balance:
    money_left = budget - balance
    print(f"Yes! You have {money_left:.2f} leva left.")
else:
    money_needed = balance - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")