def top_rows(n):
    for row in range(n * 2):
        print('-', end='')
    print()

def middle_rows(n):

    for i in range(0, (n - 2)):
        print('-', end='')
        for k in range(n - 1):
            print('\\/', end='')
        print('-')


n = int(input())


top_rows(n)
middle_rows(n)
top_rows(n)
