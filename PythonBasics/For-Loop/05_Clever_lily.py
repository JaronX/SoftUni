age = int(input())
price_washing_machine = float(input())
price_toy = int(input())

toy_counter = 0
amount = 10
money = 0

for year in range(1, age + 1):
    if year % 2 != 0:
        toy_counter += 1
    else:
        money += amount - 1
        amount += 10

money += toy_counter * price_toy
diff = abs(money - price_washing_machine)


if money >= price_washing_machine:
    print(f"Yes! {diff:.2f}")
else:
    print(f"No! {diff:.2f}")