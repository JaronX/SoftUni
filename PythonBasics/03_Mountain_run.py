from math import floor

worldRecord = float(input())
distance = float(input())
timePerMeter = float(input())

timeInSeconds = distance * timePerMeter
additionalSeconds = floor(distance / 50) * 30
totalTime = timeInSeconds + additionalSeconds

if worldRecord > totalTime:
    print(f"Yes! The new record is {totalTime:.2f} seconds.")
else:
    print(f"No! He was {abs(worldRecord - totalTime):.2f} seconds slower.")
