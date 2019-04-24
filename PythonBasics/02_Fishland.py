price_mackerel = float(input()) #skumriq
price_sprats = float(input()) #caca
bonito = float(input()) #palamud
horse_mackerel = float(input()) #safrid
mussels = int(input()) #midi

price_bonito = price_mackerel + price_mackerel * 0.60 #price per kilo
sum_bonito = bonito * price_bonito

price_horse_mackerel = price_sprats + price_sprats * 0.80 # price per kio
sum_horse_mackerel = horse_mackerel * price_horse_mackerel

sum_mussels = mussels * 7.50

total = sum_bonito + sum_horse_mackerel + sum_mussels

print(f"{total:.2f}")