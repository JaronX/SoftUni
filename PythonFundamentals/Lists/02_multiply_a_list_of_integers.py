list_of_integers = list(map(int, input().split()))
multiplier = int(input())

index_in_list = 0

for num in list_of_integers:
    multiply = num * multiplier

    list_of_integers[index_in_list] = multiply

    index_in_list += 1

string_with_integers = ''

for num in list_of_integers:
    string_with_integers += str(num) + ' '

print(string_with_integers)