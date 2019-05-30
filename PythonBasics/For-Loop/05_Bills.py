months = int(input())

total_electricity = 0
total_other = 0


for month in range(months):
    electricity_bill = float(input())

    total_electricity += electricity_bill
    total_other += (electricity_bill + 20 + 15) * 1.20

total_water = months * 20
total_internet = months * 15
average = (total_electricity + total_other + total_water + total_internet) / months

print(f"""Electricity: {total_electricity:.2f} lv
Water: {total_water:.2f} lv
Internet: {total_internet:.2f} lv
Other: {total_other:.2f} lv
Average: {average:.2f} lv
""")