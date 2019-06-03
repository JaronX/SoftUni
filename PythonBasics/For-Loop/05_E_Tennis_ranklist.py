import math

tournaments = int(input())
starting_points = int(input())

points_from_tournaments = 0
win_tournaments = 0

for game in range(tournaments):
    reached_stage_of_tournament = input()

    if reached_stage_of_tournament == "W":
        points_from_tournaments += 2000
        win_tournaments += 1
    elif reached_stage_of_tournament == "F":
        points_from_tournaments += 1200
    elif reached_stage_of_tournament == "SF":
        points_from_tournaments += 720

final_points = starting_points + points_from_tournaments
average_points_per_tournament = points_from_tournaments / tournaments
percent_won_tournaments = (win_tournaments / tournaments) * 100


print(f"""Final points: {final_points}
Average points: {math.floor(average_points_per_tournament)}
{percent_won_tournaments:.2f}%""")