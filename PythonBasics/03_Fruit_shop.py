fruit = input()
day = input()
quantity = float(input())

result = 0

if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        result = 2.50 * quantity
        print(f"{result:.2f}")
    elif fruit == "apple":
        result = 1.20 * quantity
        print(f"{result:.2f}")
    elif fruit == "orange":
        result = 0.85 * quantity
        print(f"{result:.2f}")
    elif fruit == "grapefruit":
        result = 1.45 * quantity
        print(f"{result:.2f}")
    elif fruit == "kiwi":
        result = 2.70 * quantity
        print(f"{result:.2f}")
    elif fruit == "pineapple":
        result = 5.50 * quantity
        print(f"{result:.2f}")
    elif fruit == "grapes":
        result = 3.85 * quantity
        print(f"{result:.2f}")
    else:
        print("error")
elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        result = 2.70 * quantity
        print(f"{result:.2f}")
    elif fruit == "apple":
        result = 1.25 * quantity
        print(f"{result:.2f}")
    elif fruit == "orange":
        result = 0.90 * quantity
        print(f"{result:.2f}")
    elif fruit == "grapefruit":
        result = 1.60 * quantity
        print(f"{result:.2f}")
    elif fruit == "kiwi":
        result = 3.00 * quantity
        print(f"{result:.2f}")
    elif fruit == "pineapple":
        result = 5.60 * quantity
        print(f"{result:.2f}")
    elif fruit == "grapes":
        result = 4.20 * quantity
        print(f"{result:.2f}")
    else:
        print("error")
else:
    print("error")

#print(f"{result:.2f}")
