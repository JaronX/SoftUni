eggs = int(input())

command = None
eggs_sold = 0

while command != "Close":
    command = input()

    if command == "Buy":
        eggs_quantity = int(input())

        if eggs_quantity > eggs:
            print(f"""Not enough eggs in store!
You can buy only {eggs}.""")
            break

        eggs -= eggs_quantity
        eggs_sold += eggs_quantity


    elif command == "Fill":
        eggs_quantity = int(input())
        eggs += eggs_quantity


if command == "Close":
    print(f"""Store is closed!
{eggs_sold} eggs sold.""")
