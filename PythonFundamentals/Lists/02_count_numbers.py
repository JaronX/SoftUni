from collections import Counter

x = '8 2 2 8 2 2 3 7'

integer_list = list(map(int, x.split()))

a = Counter(integer_list)

for letter in a:
    print(letter, a[letter])