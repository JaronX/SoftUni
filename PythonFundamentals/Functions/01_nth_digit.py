def find_nth_digit(number, index):
    counter = 0
    while counter != index:
        last_digit = number % 10
        number = number // 10
        counter += 1
    print(last_digit)


num = int(input())
digit = int(input())

find_nth_digit(num, digit)
