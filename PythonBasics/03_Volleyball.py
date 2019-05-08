from math import floor

year = input()
holiday = int(input())
weekend = int(input())

games_in_sofia = (48 - weekend) * (3 / 4)
games_in_home = weekend
games_in_holiday_sofia = holiday * (2 / 3)
total_games = games_in_sofia + games_in_home + games_in_holiday_sofia

if year == "leap":
    additional_games = 0.15 * total_games
    total_games = additional_games + total_games
    print(f"{floor(total_games)}")
else:
    print(f"{floor(total_games)}")

