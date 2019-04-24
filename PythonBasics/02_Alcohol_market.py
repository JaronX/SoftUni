price_whiskey = float(input())
liters_beer = float(input())
liters_wine = float(input())
liters_brandies = float(input())
liters_whiskey = float(input())

price_per_liter_brandies = price_whiskey / 2
price_per_liter_wine = price_per_liter_brandies - (0.4 * price_per_liter_brandies)
price_per_liter_beer = price_per_liter_brandies - (0.8 * price_per_liter_brandies)

total_brandies = liters_brandies * price_per_liter_brandies
total_wine = liters_wine * price_per_liter_wine
total_beer = price_per_liter_beer * liters_beer
total_whiskey = liters_whiskey * price_whiskey

total = total_brandies + total_wine + total_beer + total_whiskey

print(f'{total:.2f}')