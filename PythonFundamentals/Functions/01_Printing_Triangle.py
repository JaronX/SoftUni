def triangle_from_number(n):
    for i in range(0, n):
        num = 1

        for j in range(0, i):
            print(num, end=" ")
            num = num + 1

        print()

    for i in range(n, -1, -1):
        num = 1

        for j in range(0, i):
            print(num, end=' ')
            num = num + 1

        print()


n = int(input())

triangle_from_number(n)
