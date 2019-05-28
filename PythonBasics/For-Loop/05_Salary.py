n = int(input())
salary = int(input())



for tab in range(n):
    website = input()

    if website == "Facebook":
        salary -= 150
        if salary <= 0:
            break
    if website == "Instagram":
        salary -= 100
        if salary <= 0:
            break
    if website == "Reddit":
        salary -= 50
        if salary <= 0:
            break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary}")