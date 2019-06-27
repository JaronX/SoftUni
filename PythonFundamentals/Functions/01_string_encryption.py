def encrypt_password(symbols_of_password):
    result = ''
    counter = 0

    while symbols_of_password != counter:
        user_password = input()

        for letter in user_password:
            ascii_code = ord(letter)

            first_digit = str(ascii_code)[:1]
            last_digit = ascii_code % 10

            middle_of_result = first_digit + str(last_digit)
            beginning_of_result = chr(ascii_code + last_digit)
            end_of_result = chr(ascii_code - int(first_digit))

            result += beginning_of_result + middle_of_result + end_of_result

        counter += 1

    print(result)


number_of_symbols = int(input())

encrypt_password(number_of_symbols)
