list_of_integers = list(map(int, input().split()))

odd_counter = 0

for num in list_of_integers:
    if not num % 2 == 0:
        odd_counter += 1

print(odd_counter)


