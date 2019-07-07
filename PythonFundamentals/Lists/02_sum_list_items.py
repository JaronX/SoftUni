number_of_integers = int(input())

list_of_integers = []

for num in range(number_of_integers):
    number = int(input())
    list_of_integers.append(number)


total_of_list = 0

for num in list_of_integers:
    total_of_list += num


print(total_of_list)
