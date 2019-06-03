n = int(input())

red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0



for egg in range(n):
    color = input()

    if color == "red":
        red_eggs += 1

    elif color == "orange":
        orange_eggs += 1

    elif color == "blue":
        blue_eggs += 1

    else:
        green_eggs += 1


highest_eggs = max(red_eggs, orange_eggs, blue_eggs, green_eggs)

if highest_eggs == red_eggs:
    print(f"""Red eggs: {red_eggs}
Orange eggs: {orange_eggs}
Blue eggs: {blue_eggs}
Green eggs: {green_eggs}
Max eggs: {red_eggs} -> red""")

elif highest_eggs == orange_eggs:
    print(f"""Red eggs: {red_eggs}
Orange eggs: {orange_eggs}
Blue eggs: {blue_eggs}
Green eggs: {green_eggs}
Max eggs: {orange_eggs} -> orange""")

elif highest_eggs == blue_eggs:
    print(f"""Red eggs: {red_eggs}
Orange eggs: {orange_eggs}
Blue eggs: {blue_eggs}
Green eggs: {green_eggs}
Max eggs: {blue_eggs} -> blue""")

else:
    print(f"""Red eggs: {red_eggs}
Orange eggs: {orange_eggs}
Blue eggs: {blue_eggs}
Green eggs: {green_eggs}
Max eggs: {green_eggs} -> green""")
