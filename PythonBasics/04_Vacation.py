money_for_vacation = float(input())
current_money = float(input())

spending_counter = 0
days = 0

while money_for_vacation > current_money and spending_counter != 5:
    days += 1
    action = input()
    money = float(input())

    if action == "spend":
        current_money -= money
        spending_counter += 1
        if current_money < 0:
            current_money = 0
    elif action == "save":
        current_money += money
        spending_counter = 0



if spending_counter == 5:
    print(f"""You can't save the money.
{days}""")
elif current_money >= money_for_vacation:
    print(f"You saved the money for {days} days.")
