size_eggs = input()
color_eggs = input()
batches = int(input())

price_eggs = 0

if size_eggs == "Large":
    if color_eggs == "Red":
        price_eggs = 16
    elif color_eggs == "Green":
        price_eggs = 12
    elif color_eggs == "Yellow":
        price_eggs = 9
elif size_eggs == "Medium":
    if color_eggs == "Red":
        price_eggs = 13
    elif color_eggs == "Green":
        price_eggs = 9
    elif color_eggs == "Yellow":
        price_eggs = 7
elif size_eggs == "Small":
    if color_eggs == "Red":
        price_eggs = 9
    elif color_eggs == "Green":
        price_eggs = 8
    elif color_eggs == "Yellow":
        price_eggs = 5

price = batches * price_eggs
costs = price * 0.35
total = price - costs

print(f"{total:.2f} leva.")