type_projection = input()
rows = int(input())
columns = int(input())

income = None
seats = rows * columns

if type_projection == "Premiere":
    income = seats * 12
elif type_projection == "Normal":
    income = seats * 7.50
else:
    income = seats * 5.00

print(f"{income:.2f} leva")