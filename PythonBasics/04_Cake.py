width_cake = int(input())
height_cake = int(input())

cake_size = width_cake * height_cake
current_cake_size = 0

while cake_size >= current_cake_size:
    command = input()

    if command == "STOP":
        break

    current_cake_size += int(command)

if current_cake_size > cake_size:
    needed_cake = current_cake_size - cake_size
    print(f"No more cake left! You need {needed_cake} pieces more.")
else:
    left_cake = cake_size - current_cake_size
    print(f"{left_cake} pieces are left.")