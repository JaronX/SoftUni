def triangle_area(base, height):
    return (base * height) / 2


base = float(input())
height = float(input())

area = triangle_area(base, height)

print(f"{area:.12g}")

