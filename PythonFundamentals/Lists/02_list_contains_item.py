integer_list = list(map(int, input().split()))
number_in_list = int(input())

if number_in_list in integer_list:
    print('yes')
else:
    print('no')