days = int(input()) - 1
accommodation = input()
rating = input()

discount = 0


if accommodation == "room for one person":
    discount = days * 18
elif accommodation == "apartment":
    if days < 10:
        discount = days * 25 * 0.70
    elif 10 <= days <= 15:
        discount = days * 25 * 0.65
    else:
        discount = days * 25 * 0.50
else:
    if days < 10:
        discount = days * 35 * 0.90
    elif 10 <= days <= 15:
        discount = days * 35 * 0.85
    else:
        discount = days * 35 * 0.80



if rating == "positive":
    discount *= 1.25
else:
    discount *= 0.9


print(f"{discount:.2f}")