country = input()
type_of_souvenirs = input()
purchased_souvenirs = int(input())

price_for_souvenirs = 0
invalid_counter = False


if country == "Argentina":
    if type_of_souvenirs == "flags":
        price_for_souvenirs = 3.25
    elif type_of_souvenirs == "caps":
        price_for_souvenirs = 7.20
    elif type_of_souvenirs == "posters":
        price_for_souvenirs = 5.10
    elif type_of_souvenirs == "stickers":
        price_for_souvenirs = 1.25
    else:
        print("Invalid stock!")
        invalid_counter = True

elif country == "Brazil":
    if type_of_souvenirs == "flags":
        price_for_souvenirs = 4.20
    elif type_of_souvenirs == "caps":
        price_for_souvenirs = 8.50
    elif type_of_souvenirs == "posters":
        price_for_souvenirs = 5.35
    elif type_of_souvenirs == "stickers":
        price_for_souvenirs = 1.20
    else:
        print("Invalid stock!")
        invalid_counter = True

elif country == "Croatia":
    if type_of_souvenirs == "flags":
        price_for_souvenirs = 2.75
    elif type_of_souvenirs == "caps":
        price_for_souvenirs = 6.90
    elif type_of_souvenirs == "posters":
        price_for_souvenirs = 4.95
    elif type_of_souvenirs == "stickers":
        price_for_souvenirs = 1.10
    else:
        print("Invalid stock!")
        invalid_counter = True

elif country == "Denmark":
    if type_of_souvenirs == "flags":
        price_for_souvenirs = 3.10
    elif type_of_souvenirs == "caps":
        price_for_souvenirs = 6.50
    elif type_of_souvenirs == "posters":
        price_for_souvenirs = 4.80
    elif type_of_souvenirs == "stickers":
        price_for_souvenirs = 0.90
    else:
        print("Invalid stock!")
        invalid_counter = True
else:
    print("Invalid country!")
    invalid_counter = True



total = purchased_souvenirs * price_for_souvenirs

if not invalid_counter:
    print(f"Pepi bought {purchased_souvenirs} {type_of_souvenirs} of {country} for {total:.2f} lv.")