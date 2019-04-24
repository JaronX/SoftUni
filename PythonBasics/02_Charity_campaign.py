campaign = int(input())
confectioners = int(input())
cakes = int(input())
waffles = int(input())
pancakes = int(input())

cakes = cakes * 45
waffles = waffles * 5.80
pancakes = pancakes * 3.20

total_day = (cakes + waffles + pancakes) * confectioners
total_campaign = total_day * campaign
net = total_campaign - 1 / 8 * total_campaign

print(f'{net:.2f}')