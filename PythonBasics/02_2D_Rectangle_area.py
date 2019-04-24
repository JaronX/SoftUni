x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

length = y1 - y2
width = x1 - x2

area = abs(length) * abs(width)
perimeter = 2 * (abs(length) + abs(width))

print(f'{area:.2f}')
print(f'{perimeter:.2f}')