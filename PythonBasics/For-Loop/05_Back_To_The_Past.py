money = float(input())
years_live = int(input())

current_years = 18


for year in range(1800, years_live + 1):
    if year % 2 == 0:
        money -= 12000
        current_years += 1
    elif year % 2 != 0:
        money -= 12000 + (50 * current_years)
        current_years += 1

if money >= 0:
    print(f"Yes! He will live a carefree life and will have {money:.2f} dollars left.")
else:
    print(f"He will need {abs(money):.2f} dollars to survive.")