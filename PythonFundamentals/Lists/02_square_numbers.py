import math

integers_list = list(map(int, input().split()))

super_square_list = []

for num in integers_list:
    if num <= 0:
        continue
    if num % math.sqrt(num) == 0:
        super_square_list.append(num)


super_square_list.sort(reverse = True)


convert_integer_list_to_str = ''

for item in super_square_list:
    convert_integer_list_to_str += str(item) + ' '


print(convert_integer_list_to_str)