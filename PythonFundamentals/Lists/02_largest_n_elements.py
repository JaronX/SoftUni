integers_list = list(map(int, input().split()))
number_of_integers = int(input())

integers_list.sort(reverse=True)

number_counter = 0

for num in integers_list:

    if number_counter < number_of_integers:
        print(num, end=' ')

    number_counter += 1
