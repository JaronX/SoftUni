n = int(input())
w = float(input())
l = float(input())
m = int(input())
o = int(input())

total_area = n * n
bench = m * o
coverage_area = total_area - bench
tile_area = w * l
tiles = coverage_area / tile_area
time = tiles * 0.2

print(f'{tiles:.2f}')
print(f'{time:.2f}')