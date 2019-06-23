def sing_of_integer_number(number):
    if number < 0:
        print(f"The number {number} is negative.")
    elif number == 0:
        print(f'The number {number} is zero.')
    else:
        print(f'The number {number} is positive.')

n = int(input())

sing_of_integer_number(n)