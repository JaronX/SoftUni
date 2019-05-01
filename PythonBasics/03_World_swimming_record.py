import math

record = float(input())
meters = float(input())
time = float(input())

swimming = meters * time
extra_time = math.floor((meters / 15)) * 12.5
total_time = swimming + extra_time
real_time = abs(total_time - record)


if total_time < record:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")

else:
    print(f"No, he failed! He was {real_time:.2f} seconds slower.")