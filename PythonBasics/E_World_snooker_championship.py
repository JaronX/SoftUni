stage_of_the_championship = input()
type_of_ticket = input()
tickets_count = int(input())
photo = input()

price_per_ticket = 0


if stage_of_the_championship == "Quarter final":
    if type_of_ticket == "Standard":
        price_per_ticket =  55.50
    elif type_of_ticket == "Premium":
        price_per_ticket =  105.20
    elif type_of_ticket == "VIP":
        price_per_ticket =  118.90
elif stage_of_the_championship == "Semi final":
    if type_of_ticket == "Standard":
        price_per_ticket =  75.88
    elif type_of_ticket == "Premium":
        price_per_ticket =  125.22
    elif type_of_ticket == "VIP":
        price_per_ticket =  300.40
elif stage_of_the_championship == "Final":
    if type_of_ticket == "Standard":
        price_per_ticket =  110.10
    elif type_of_ticket == "Premium":
        price_per_ticket =  160.66
    elif type_of_ticket == "VIP":
        price_per_ticket =  400

total_tickets = tickets_count * price_per_ticket

if 2500 < total_tickets <= 4000:
    total_tickets -= total_tickets * 0.10
    if photo == "Y":
        total_tickets += tickets_count * 40
elif total_tickets > 4000:
    total_tickets -= total_tickets * 0.25



print(f"{total_tickets:.2f}")