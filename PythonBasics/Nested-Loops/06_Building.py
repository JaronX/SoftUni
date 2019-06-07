floors = int(input())
rooms_per_floor = int(input())

letter = None

for floor in range(floors, 0, -1):
    for room in range(0, rooms_per_floor):
        if floor == floors:
            letter = "L"
        elif floor % 2 == 0:
            letter = "O"
        else:
            letter = "A"

        print(f"{letter}{floor}{room}", end=' ')
    print()






