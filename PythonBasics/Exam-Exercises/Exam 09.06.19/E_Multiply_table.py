number = int(input())


last_number = number % 10

second_number = number // 10
seconds_number = second_number % 10

first_number = second_number // 10
firsts_number = first_number % 10



for i in range(0, last_number + 1):
    for j in range(0, seconds_number + 1):
        for k in range(0, firsts_number + 1):
            if i > 0 and j > 0 and k > 0:
                print(f"{i} * {j} * {k} = {i * j * k};")