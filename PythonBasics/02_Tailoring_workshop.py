tables = int(input())
length = float(input())
width = float(input())

area_tablecloths = tables * (length + 2 * 0.30) * (width + 2 * 0.30)
area_table_mats = tables * (length / 2) * (length / 2)

USD = area_tablecloths * 7 + area_table_mats * 9
BGN = USD * 1.85

print(f'{USD:.2f} USD')
print(f'{BGN:.2f} BGN')