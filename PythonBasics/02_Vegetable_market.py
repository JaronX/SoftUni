vegetable = float(input())
fruit = float(input())
kg_vegetable = int(input())
kg_fruit = int(input())

total_vegetable = vegetable * kg_vegetable
total_fruits = fruit * kg_fruit
total = ((total_vegetable + total_fruits) / 1.94)

print(f"{total:.2f}")