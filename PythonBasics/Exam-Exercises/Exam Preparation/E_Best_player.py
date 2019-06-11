top_goals = 0
top_scorer = None

while True:
    name = input()

    if name == "END":
        break

    goals = int(input())

    if goals > top_goals:
        top_goals = goals
        top_scorer = name

    if goals >= 10:
        break


print(f"{top_scorer} is the best player!")

if top_goals >= 3:
    print(f"He has scored {top_goals} goals and made a hat-trick !!!")
else:
    print(f"He has scored {top_goals} goals.")


