installment_count = int(input())

balance = 0
counter = 0

while counter < installment_count:
    installment = float(input())

    if installment < 0:
        print("Invalid operation!")
        print(f"Total: {balance:.2f}")
        break
    print(f"Increase: {installment:.2f}")

    balance += installment

    if counter == installment_count:
        print(f"Total: {balance:.2f}")

    counter += 1