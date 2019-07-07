import sys

list_of_integers = list(map(int, input().split()))

smallest_number = sys.maxsize #the biggest number

for num in list_of_integers: #checking each item for smallest number in list
    if num < smallest_number:
        smallest_number = num

print(smallest_number)