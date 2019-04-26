import math

figure = input().lower()

if figure == "square":
    square_side = float(input())
    area = square_side * square_side
elif figure == "rectangle":
    rectangle_side_a = float(input())
    rectangle_side_b = float(input())
    area = rectangle_side_a * rectangle_side_b
elif figure == "circle":
    circle_radius = float(input())
    area = math.pi * circle_radius ** 2
elif figure == "triangle":
    triangle_side_a = float(input())
    triangle_side_a_h = float(input())
    area = (triangle_side_a * triangle_side_a_h) / 2

print(f'{area:.3f}')