number_of_loads = int(input())

minibus = 0
truck = 0
train = 0

for loads in range(number_of_loads):
    tonnage = int(input())

    if tonnage <= 3:
        minibus += tonnage
    elif tonnage <= 11:
        truck += tonnage
    else:
        train += tonnage

all_loads = minibus + truck + train
mean_price_per_ton = ((minibus * 200) + (truck * 175) + (train * 120)) / all_loads

percent_minibus = (minibus / all_loads) * 100
percent_truck = (truck / all_loads) * 100
percent_train = (train / all_loads) * 100

print(f"""{mean_price_per_ton:.2f}
{percent_minibus:.2f}%
{percent_truck:.2f}%
{percent_train:.2f}%""")