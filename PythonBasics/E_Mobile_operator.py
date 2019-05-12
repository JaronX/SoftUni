term_of_contract = input()
type_of_contract = input()
added_mobile_internet = input()
months_to_pay = int(input())

price_contract = 0

if term_of_contract == "one":
    if type_of_contract == "Small" and added_mobile_internet == "yes":
        price_contract = 9.98 + 5.50
    elif type_of_contract == "Small" and added_mobile_internet == "no":
        price_contract = 9.98
    elif type_of_contract == "Middle" and added_mobile_internet == "yes":
        price_contract = 18.99 + 4.35
    elif type_of_contract == "Middle" and added_mobile_internet == "no":
        price_contract = 18.99
    elif type_of_contract == "Large" and added_mobile_internet == "yes":
        price_contract = 25.98 + 4.35
    elif type_of_contract == "Large" and added_mobile_internet == "no":
        price_contract = 25.98
    elif type_of_contract == "ExtraLarge" and added_mobile_internet == "yes":
        price_contract = 35.99 + 3.85
    elif type_of_contract == "ExtraLarge" and added_mobile_internet == "no":
        price_contract = 35.99
elif term_of_contract == "two":
    if type_of_contract == "Small" and added_mobile_internet == "yes":
        price_contract = 8.58 + 5.50
    elif type_of_contract == "Small" and added_mobile_internet == "no":
        price_contract = 8.58
    elif type_of_contract == "Middle" and added_mobile_internet == "yes":
        price_contract = 17.09 + 4.35
    elif type_of_contract == "Middle" and added_mobile_internet == "no":
        price_contract = 17.09
    elif type_of_contract == "Large" and added_mobile_internet == "yes":
        price_contract = 23.59 + 4.35
    elif type_of_contract == "Large" and added_mobile_internet == "no":
        price_contract = 23.59
    elif type_of_contract == "ExtraLarge" and added_mobile_internet == "yes":
        price_contract = 31.79 + 3.85
    elif type_of_contract == "ExtraLarge" and added_mobile_internet == "no":
        price_contract = 31.79
    price_contract -= price_contract * 0.0375

total = price_contract * months_to_pay

print(f"{total:.2f} lv.")