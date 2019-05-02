from math import floor

needed_hours = int(input())
days = int(input())
workers = int(input())

working_days = 0.10 * days
extra_hours = (workers * 2) * days
total_hours = floor(working_days * 8) * workers + extra_hours

if total_hours > needed_hours:
    hours_left = total_hours - needed_hours
    print(f"Yes!{hours_left} hours left.")
else:
    lack_hours = needed_hours - total_hours
    print(f"Not enough time!{lack_hours} hours needed.")