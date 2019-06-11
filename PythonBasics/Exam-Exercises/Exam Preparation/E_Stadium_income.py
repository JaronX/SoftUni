sectors = int(input())
capacity = int(input())
ticket = float(input())

total_income = capacity * ticket
sector_income = total_income / sectors
money_for_charity = (total_income - (sector_income * 0.75)) / 8

print(f"""Total income - {total_income:.2f} BGN
Money for charity - {money_for_charity:.2f} BGN
""")