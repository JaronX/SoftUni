def integer_to_base(number, to_base):
    result = ''
    while number != 0:
        reminder = number % to_base
        result = str(reminder) + result
        number //= to_base

    print(result)


num = int(input())
base = int(input())

integer_to_base(num, base)



