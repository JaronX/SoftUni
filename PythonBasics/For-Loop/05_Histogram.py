n = int(input())


interval_200 = 0
interval_200_399 = 0
interval_400_599 = 0
interval_600_799 = 0
interval_800 = 0



for num in range(n):
    number = int(input())

    if number < 200:
        interval_200 += 1
    elif number >= 200 and number < 400:
        interval_200_399 += 1
    elif number >= 400 and number < 600:
        interval_400_599 += 1
    elif number >= 600 and number < 800:
        interval_600_799 += 1
    elif number >= 800:
        interval_800 += 1

p1 = (interval_200 / n) * 100
p2 = (interval_200_399 / n) * 100
p3 = (interval_400_599 / n) * 100
p4 = (interval_600_799 / n) * 100
p5 = (interval_800 / n) * 100

print(f"""{p1:.2f}%
{p2:.2f}%
{p3:.2f}%
{p4:.2f}%
{p5:.2f}%""")