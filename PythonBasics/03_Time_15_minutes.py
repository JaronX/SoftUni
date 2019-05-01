hours = int(input())
minutes = int(input())

minutes += 15

total_time = (hours * 60) + minutes

hour = total_time // 60
minutes = total_time % 60

if hour > 23:
    hour = hour - 24

print(f'{hour}:{minutes:02d}')