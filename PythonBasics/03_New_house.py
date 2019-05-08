kind_of_flowers = input()
flowers_count = int(input())
budget = int(input())

price_flowers = 0
rise = 0


if kind_of_flowers == "Roses":
    price_flowers = flowers_count * 5
    if flowers_count > 80:
        price_flowers -= price_flowers * 0.10
elif kind_of_flowers == "Dahlias":
    price_flowers = flowers_count * 3.80
    if flowers_count > 90:
        price_flowers -= price_flowers * 0.15
elif kind_of_flowers == "Tulips":
    price_flowers = flowers_count * 2.80
    if flowers_count > 80:
        price_flowers -= price_flowers * 0.15
elif kind_of_flowers == "Narcissus":
    price_flowers = flowers_count * 3.00
    if flowers_count < 120:
        price_flowers += price_flowers * 0.15
elif kind_of_flowers == "Gladiolus":
    price_flowers = flowers_count * 2.50
    if flowers_count < 80:
        price_flowers += price_flowers * 0.20



if budget - price_flowers >= 0:
    print(f"Hey, you have a great garden with {flowers_count} {kind_of_flowers} and {budget - price_flowers:.2f} leva left.")
elif budget - price_flowers <= 0:
    print(f"Not enough money, you need {abs(budget - price_flowers):.2f} leva more.")