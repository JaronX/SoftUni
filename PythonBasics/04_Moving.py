width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())

free_space = width_free_space * length_free_space * height_free_space

occupied_space = 0

while True:

    boxes = input()


    if boxes == "Done":
        left_space = free_space - occupied_space
        print(f"{left_space} Cubic meters left.")
        break
    else:
        occupied_space += int(boxes)

    if free_space < occupied_space:
        needed_space = occupied_space - free_space
        print(f"No more free space! You need {needed_space} Cubic meters more.")
        break