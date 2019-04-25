days = int(input())
money = float(input())
dolars = float(input())

monthly = days * money
yearly = monthly * 12 + monthly * 2.5
taxes = (25 / 100) * yearly
year_net_income = (yearly - taxes) * dolars
day_income = year_net_income / 365

print(f"{day_income:.2f}")