n = int(input())

remainder_2 = 0
remainder_3 = 0
remainder_4 = 0

for num in range(n):
    number = int(input())

    if number % 2 == 0:
        remainder_2 += 1
    if number % 3 == 0:
        remainder_3 += 1
    if number % 4 == 0:
        remainder_4 += 1

p1 = (remainder_2 / n) * 100
p2 = (remainder_3 / n) * 100
p3 = (remainder_4 / n) * 100

print(f"""{p1:.2f}%
{p2:.2f}%
{p3:.2f}%""")