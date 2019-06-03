import math
import sys

easter_bread = int(input())

total_sugar = 0
total_flour = 0

max_sugar = -sys.maxsize - 1
max_flour = -sys.maxsize - 1

for bread in range(easter_bread):
    sugar = int(input())
    flour = int(input())

    total_sugar += sugar
    total_flour += flour

    if sugar > max_sugar:
        max_sugar = sugar
    if flour > max_flour:
        max_flour = flour

sugar_packets = math.ceil(total_sugar / 950)
flour_packets = math.ceil(total_flour / 750)

print(f"""Sugar: {sugar_packets}
Flour: {flour_packets}
Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.""")

