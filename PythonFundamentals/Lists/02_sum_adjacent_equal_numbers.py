decimal_list = list(map(float, input().split()))

restart = True

while restart:
    index_counter = 1
    for num in decimal_list:

        if index_counter >= len(decimal_list):
            restart = False
            break

        if num == decimal_list[index_counter]:
            decimal_list[index_counter] = float(num) + float(decimal_list[index_counter])
            del decimal_list[index_counter - 1]
            restart = True
            break
        else:
            index_counter += 1

for num in decimal_list:

    multiply = num * 10

    if multiply % 10 == 0:
        remove_zeros = multiply / 10
        print(num, end=' ')
    else:
        remove_zeros = multiply / 10
        print(num, end=' ')

print(string_with_decimal)
