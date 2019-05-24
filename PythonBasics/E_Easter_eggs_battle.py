eggs_player_1 = int(input())
eggs_player_2 = int(input())

winner = None

while winner != "End of battle":
    winner = input()

    if winner == "one":
        eggs_player_2 -= 1
    elif winner == "two":
        eggs_player_1 -= 1

    if eggs_player_1 == 0:
        print(f"Player one is out of eggs. Player two has {eggs_player_2} eggs left.")
        break
    elif eggs_player_2 == 0:
        print(f"Player two is out of eggs. Player one has {eggs_player_1} eggs left.")
        break


if winner == "End of battle":
    print(f"""Player one has {eggs_player_1} eggs left.
Player two has {eggs_player_2} eggs left.""")