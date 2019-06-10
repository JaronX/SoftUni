passenger_counter = int(input())
stops = int(input())




for num in range(1, (stops + 1)):
    passengers_out = int(input())
    passengers_in = int(input())

    if num % 2 != 0:
        passengers_in += 2
    else:
        passengers_out += 2

    passenger_counter = (passenger_counter - passengers_out) + passengers_in

print(f"The final number of passengers is : {passenger_counter}")