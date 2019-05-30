stadium_capacity = int(input())
fans = int(input())

fans_in_sector_a = 0
fans_in_sector_b = 0
fans_in_sector_v = 0
fans_in_sector_g = 0


for fan in range(fans):
    sector = input()

    if sector == "A":
        fans_in_sector_a += 1
    elif sector == "B":
        fans_in_sector_b += 1
    elif sector == "V":
        fans_in_sector_v += 1
    else:
        fans_in_sector_g += 1

p0 = (fans_in_sector_a / fans) * 100
p1 = (fans_in_sector_b / fans) * 100
p2 = (fans_in_sector_v / fans) * 100
p3 = (fans_in_sector_g / fans) * 100

p_of_all_fans = ((fans_in_sector_a + fans_in_sector_b + fans_in_sector_v + fans_in_sector_g) / stadium_capacity) * 100

print(f"""{p0:.2f}%
{p1:.2f}%
{p2:.2f}%
{p3:.2f}%
{p_of_all_fans:.2f}%""")