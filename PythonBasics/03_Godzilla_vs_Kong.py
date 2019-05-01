budget = float(input())
statist = int(input())
price = float(input())

dekor = 0.10 * budget
clothing = statist * price



if statist > 150:
    discount = 0.10 * clothing
    total_clothing = clothing - discount
    total_movie = dekor + total_clothing
    money = abs(budget - total_movie)

else:
    total_movie = dekor + clothing
    money = abs(budget - total_movie)

if total_movie > budget:
    print(f"""Not enough money!
Wingard needs {money:.2f} leva more.""")

else:
    print(f"""Action!
Wingard starts filming with {money:.2f} leva left.""")

