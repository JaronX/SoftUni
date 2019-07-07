import sys

list_of_integers = list(map(int, input().split()))

max_number = sys.maxsize

for num in list_of_integers:
    if num < max_number:
        max_number = num

print(max_number)