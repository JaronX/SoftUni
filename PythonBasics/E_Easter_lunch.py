easter_bread = int(input())
eggshells = int(input())
cookies = int(input())

price_easter_bread = easter_bread * 3.20
price_eggshells = eggshells * 4.35
price_cookies = cookies * 5.40
price_paint = eggshells * 12 * 0.15
price_total = price_easter_bread + price_eggshells + price_cookies + price_paint

print(f"{price_total:.2f}")