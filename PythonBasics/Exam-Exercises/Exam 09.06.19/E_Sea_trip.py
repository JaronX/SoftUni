money_for_food = float(input())
money_for_souvenirs = float(input())
money_for_hotel = float(input())

money_for_oil = 54.39
money_for_food_and_souvenirs = (3 * money_for_food) + (3 * money_for_souvenirs)
first_day_in_hotel = money_for_hotel * 0.9
second_day_in_hotel = money_for_hotel * 0.85
third_day_in_hotel = money_for_hotel * 0.8

total_money = money_for_oil + money_for_food_and_souvenirs + first_day_in_hotel + second_day_in_hotel + third_day_in_hotel

print(f"Money needed: {total_money:.2f}")