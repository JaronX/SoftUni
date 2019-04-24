w = float(input())
h = float(input())

shirochina = h * 100
realna_shirochina = shirochina - 100 #koridor

biura = int(realna_shirochina / 70)


duljina = w * 100
redove = int(duljina / 120)

broi_mesta = redove * biura - 3

print(broi_mesta)