sweet = input()
sweet_count = int(input())
day_of_month = int(input())

price = 0
balance = 0

if day_of_month <= 15 and sweet == "Cake":
    price = 24

elif day_of_month <= 15 and sweet == "Souffle":
    price = 6.66

elif day_of_month <= 15 and sweet == "Baklava":
    price = 12.60


elif day_of_month > 15 and sweet == "Cake":
    price = 28.70

elif day_of_month > 15 and sweet == "Souffle":
    price = 9.80

elif day_of_month > 15 and sweet == "Baklava":
    price = 16.98


balance = price * sweet_count

if 100 <= balance <= 200 and day_of_month <= 22:
    balance -= balance * 0.15
elif balance > 200 and day_of_month <= 22:
    balance -= balance * 0.25

if day_of_month <= 15:
    balance -= balance * 0.10

print(f"{balance:.2f}")
