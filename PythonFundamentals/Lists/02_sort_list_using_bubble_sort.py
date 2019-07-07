integers_list = list(map(int, input().split()))

restart = True

while restart:
    index_counter = 1

    if sorted(integers_list) == integers_list:
        break

    for number in integers_list:

        if index_counter >= len(integers_list):
            break

        if number > integers_list[index_counter]:
            integers_list.insert(index_counter + 1, number)
            integers_list.pop(index_counter - 1)

        index_counter += 1

for num in integers_list:
    print(num, end=' ')