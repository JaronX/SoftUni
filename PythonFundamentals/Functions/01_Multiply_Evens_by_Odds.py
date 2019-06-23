def multiply_evens_by_odds(number):
    even_sum = 0
    odd_sum = 0

    for digit in str(number):
        last_number = abs(number) % 10

        if last_number % 2 == 0:
            even_sum += last_number
        else:
            odd_sum += last_number

        number = abs(number) // 10

    return even_sum * odd_sum


number = int(input())

print(multiply_evens_by_odds(number))
