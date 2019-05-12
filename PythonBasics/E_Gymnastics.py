country = input()
instrument = input()

rating = 0

if country == "Russia":
    if instrument == "ribbon":
        rating = 9.100 + 9.400
    elif instrument == "hoop":
        rating = 9.300 + 9.800
    elif instrument == "rope":
        rating = 9.600 + 9.000
elif country == "Bulgaria":
    if instrument == "ribbon":
        rating = 9.600 + 9.400
    elif instrument == "hoop":
        rating = 9.550 + 9.750
    elif instrument == "rope":
        rating = 9.500 + 9.400
elif country == "Italy":
    if instrument == "ribbon":
        rating = 9.200 + 9.500
    elif instrument == "hoop":
        rating = 9.450 + 9.350
    elif instrument == "rope":
        rating = 9.700 + 9.150

points_left = 20 - rating
percents_left = (points_left / 20) * 100

print(f"""The team of {country} get {rating:.3f} on {instrument}.
{percents_left:.2f}%""")