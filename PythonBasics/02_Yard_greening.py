area_yard = float(input())

price_yard = area_yard * 7.61
discount = price_yard * 0.18
final_price = price_yard - discount



print(f'The final price is: {final_price:.2f} lv.')
print(f'The discount is: {discount:.2f} lv.')