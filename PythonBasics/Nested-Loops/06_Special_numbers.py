n = int(input())

for j in range(1, 10):
    for k in range(1, 10):
        for l in range(1, 10):
            for m in range(1, 10):
                if n % j == 0:
                    if n % k == 0:
                        if n % l == 0:
                            if n % m == 0:
                                print(f"{j}{k}{l}{m}", end = ' ')



