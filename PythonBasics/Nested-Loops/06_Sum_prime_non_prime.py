number = input()
prime_numbers = 0
non_prime_numbers = 0

while number != "stop":
    number = int(number)
    counter = 0

    if number < 0:
        print("Number is negative.")
    else:
        for i in range(2, number + 1):
            if number % i == 0:
                counter += 1

        if counter == 1:
            prime_numbers += number
        else:
            non_prime_numbers += number

    number = input()

print(f"""Sum of all prime numbers is: {prime_numbers}
Sum of all non prime numbers is: {non_prime_numbers}
""")

