price_flour = float(input())
kg_flour = float(input())
kg_sugar = float(input())
eggs = int(input())
yeast = int(input())

price_sugar = price_flour * 0.75
price_eggs = price_flour * 1.1
price_yeast = price_sugar * 0.2

summ_flour = price_flour * kg_flour
summ_sugar = price_sugar * kg_sugar
summ_eggs = price_eggs * eggs
summ_yeast = price_yeast * yeast

total = summ_flour + summ_sugar + summ_eggs + summ_yeast

print(f"{total:.2f}")