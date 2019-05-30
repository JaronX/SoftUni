moves = int(input())

total_points = 0

points_from_0_to_9 = 0
points_from_10_to_19 = 0
points_from_20_to_29 = 0
points_from_30_to_39 = 0
points_from_40_to_50 = 0

invalid_numbers = 0

for num in range(moves):
    number = int(input())

    if 0 <= number <= 9:
        total_points += 0.20 * number
        points_from_0_to_9 += 1
    elif 10 <= number <= 19:
        total_points += 0.30 * number
        points_from_10_to_19 += 1
    elif 20 <= number <= 29:
        total_points += 0.40 * number
        points_from_20_to_29 += 1
    elif 30 <= number <= 39:
        total_points += 50
        points_from_30_to_39 += 1
    elif 40 <= number <= 50:
        total_points += 100
        points_from_40_to_50 += 1
    else:
        total_points /= 2
        invalid_numbers += 1

p0 = (points_from_0_to_9 / moves) * 100
p1 = (points_from_10_to_19 / moves) * 100
p2 = (points_from_20_to_29 / moves) * 100
p3 = (points_from_30_to_39 / moves) * 100
p4 = (points_from_40_to_50 / moves) * 100
p5 = (invalid_numbers / moves) * 100


print(f"""{total_points:.2f}
From 0 to 9: {p0:.2f}%
From 10 to 19: {p1:.2f}%
From 20 to 29: {p2:.2f}%
From 30 to 39: {p3:.2f}%
From 40 to 50: {p4:.2f}%
Invalid numbers: {p5:.2f}%""")