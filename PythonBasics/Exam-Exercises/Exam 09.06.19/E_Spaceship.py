import math

width = float(input())
length = float(input())
height = float(input())
astronauts_height = float(input())

volume_rocket = width * length * height
volume_room = (astronauts_height + 0.40) * 2 * 2
enough_space_for = math.floor(volume_rocket / volume_room)

if enough_space_for < 3:
    print("The spacecraft is too small.")
elif enough_space_for <= 10:
    print(f"The spacecraft holds {enough_space_for} astronauts.")
elif enough_space_for > 10:
    print("The spacecraft is too big.")