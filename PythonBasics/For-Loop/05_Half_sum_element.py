import sys
n = int(input())

total = 0
max_num = -sys.maxsize - 1

for num in range(n):
    number = int(input())

    if number > max_num:
        max_num = number

    total += number

total -= max_num

if total == max_num:
    print(f'''Yes
Sum = {total}''')
else:
    diff = abs(max_num - total)
    print(f'''No
Diff = {diff}''')