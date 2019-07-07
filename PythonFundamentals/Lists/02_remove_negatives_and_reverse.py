integers_list = list(map(int, input().split()))

positive_list = []

for num in integers_list:
    if num >= 0:
        positive_list.append(num)

positive_list.reverse()

string_with_integers = ''

for num in positive_list:
    string_with_integers += str(num) + ' '

if string_with_integers:
    print(string_with_integers)
else:
    print('empty')