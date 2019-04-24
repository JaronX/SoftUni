from math import floor

length = float(input())
width = float(input())
side_wardrobe = float(input())

hall = (length * 100) * (width * 100)
wardrobe = (side_wardrobe * 100) * (side_wardrobe * 100)
bench = hall / 10
free_space = hall - wardrobe - bench

dancers = free_space / (40 + 7000)

print(floor(dancers))