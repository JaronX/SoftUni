fruit = input()
size = input()
sets_count = int(input())

price_per_set = 0
balance = 0

if size == "small":
    if fruit == "Watermelon":
        price_per_set = 56 * 2
    elif fruit == "Mango":
        price_per_set = 36.66 * 2
    elif fruit == "Pineapple":
        price_per_set = 42.10 * 2
    elif fruit == "Raspberry":
        price_per_set = 20 * 2
elif size == "big":
    if fruit == "Watermelon":
        price_per_set = 28.70 * 5
    elif fruit == "Mango":
        price_per_set = 19.60 * 5
    elif fruit == "Pineapple":
        price_per_set = 24.80 * 5
    elif fruit == "Raspbberry":
        price_per_set = 15.20 * 5


balance = price_per_set * sets_count

if 400 <= balance <= 1000:
    balance -= balance* 0.15
elif balance > 1000:
    balance -= balance * 0.50

print(f"{balance:.2f} lv.")