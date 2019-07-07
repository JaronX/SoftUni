integers_list = list(map(int, input().split()))

for i in range(len(integers_list)):
    if i % 2 != 0 and integers_list[i] % 2 != 0:
        print('Index ' + str(i) + ' -> ' + str(integers_list[i]))
