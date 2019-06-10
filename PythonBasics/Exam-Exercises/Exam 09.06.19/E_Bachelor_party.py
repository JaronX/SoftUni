money_for_singer = int(input())

group = None
money_from_couverts = 0
guests = 0


while True:
    group = input()
    if group == "The restaurant is full":
        break

    if int(group) < 5:
        money_from_couverts += int(group) * 100
        guests += int(group)
    elif int(group) >= 5:
        money_from_couverts += int(group) * 70
        guests += int(group)

if money_from_couverts >= money_for_singer:
    money_left = money_from_couverts - money_for_singer
    print(f"You have {guests} guests and {money_left} leva left.")
else:
    print(f"You have {guests} guests and {money_from_couverts} leva income, but no singer.")
