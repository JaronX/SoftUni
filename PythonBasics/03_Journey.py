budget = float(input())
season = input()

if budget <= 100:
    place = "Bulgaria"
    if season == "summer":
        money_spend = budget * 0.30
        sleep = "Camp"
    elif season == "winter":
        money_spend = budget * 0.70
        sleep = "Hotel"
elif budget <= 1000:
    place = "Balkans"
    if season == "summer":
        money_spend = budget * 0.40
        sleep = "Camp"
    elif season == "winter":
        money_spend = budget * 0.80
        sleep = "Hotel"
elif budget > 1000:
    place = "Europe"
    money_spend = budget * 0.90
    sleep = "Hotel"

print(f"""Somewhere in {place}
{sleep} - {money_spend:.2f}""")

