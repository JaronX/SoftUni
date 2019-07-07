integers_list = list(map(int, input().split()))

integers_list.sort()


string_with_integers = ''

index = 1

length = len(integers_list)

for num in integers_list:
    index += 1

    string_with_integers += f"{num}"

    if index <= length:
        string_with_integers += ' <= '


print(string_with_integers)