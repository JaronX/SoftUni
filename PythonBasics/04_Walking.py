goal = 10000

steps_counter = 0

while steps_counter < goal:
    steps = input()

    if steps == "Going home":
        steps = int(input())
        steps_counter += steps
        break

    steps_counter += int(steps)

if steps_counter < goal:
    needed_steps = goal - steps_counter
    print(f"{needed_steps} more steps to reach goal.")
else:
    print("Goal reached! Good job!")