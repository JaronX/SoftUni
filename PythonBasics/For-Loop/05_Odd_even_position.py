import sys

n = int(input())

odd_sum = 0
even_sum = 0

odd_max_num = -sys.maxsize - 1
odd_min_num = sys.maxsize

even_max_num = -sys.maxsize - 1
even_min_num = sys.maxsize


for position in range(1, n + 1):
    number = float(input())

    if position % 2 != 0:
        odd_sum += number

        if number > odd_max_num:
            odd_max_num = number
        if number < odd_min_num:
            odd_min_num = number

    else:
        even_sum += number

        if number > even_max_num:
            even_max_num = number
        if number < even_min_num:
            even_min_num = number


print(f"OddSum={odd_sum:.2f},")

if odd_max_num == -sys.maxsize - 1:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min_num:.2f},")

if odd_min_num == sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={odd_max_num:.2f},")


print(f"EvenSum={even_sum:.2f},")


if even_max_num == -sys.maxsize - 1:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_min_num:.2f},")

if even_min_num == sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={even_max_num:.2f}")