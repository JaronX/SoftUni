holiday = int(input())
norm = 30000

day_off = holiday * 127
working_days = (365 - holiday) * 63
play_time = day_off + working_days
difference = abs(norm - play_time)
hours = difference // 60
minutes = difference % 60


if play_time > norm:
    print(f"""Tom will run away
{hours} hours and {minutes} minutes more for play""")

else:
    print(f"""Tom sleeps well
{hours} hours and {minutes} minutes less for play""")