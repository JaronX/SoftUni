x = float(input())
y = float(input())
h = float(input())

#walls

side_wall = x * y
window = 1.5 ** 2
total_side_wall = 2 * side_wall - 2 * window
rear_wall = x ** 2
entrance = 1.2 * 2
total_front_rear = 2 * rear_wall - entrance
total_area_walls = total_side_wall + total_front_rear
gree_paint = total_area_walls / 3.4

#roof

rectangles = 2 * (x * y)
triangles = 2 * (x * h / 2)
total_area_roof = rectangles + triangles
red_paint = total_area_roof / 4.3

print(f"{gree_paint:.2f}")
print(f"{red_paint:.2f}")