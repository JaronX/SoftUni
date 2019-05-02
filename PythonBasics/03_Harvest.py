import math

vineyard = int(input())
grapes_meter = float(input())
needed_liters = int(input())
workers = int(input())

total_grapes = vineyard * grapes_meter
wine_produced = (0.40 * total_grapes) / 2.5

if wine_produced < needed_liters:
    lack_wine = needed_liters - wine_produced
    print(f"It will be a tough winter! More {math.floor(lack_wine)} liters wine needed.")
else:
    wine_left = wine_produced - needed_liters
    wine_workers = wine_left / workers
    print(f"""Good harvest this year! Total wine: {math.floor(wine_produced)} liters.
{math.ceil(wine_left)} liters left -> {math.ceil(wine_workers)} liters per person.""")