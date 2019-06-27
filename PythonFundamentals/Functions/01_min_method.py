def get_min(a, b):
    if a > b:
        result = b
    else:
        result = a
    return result


def get_minimum(n1, n2, n3):
    minimum = get_min(n1, n2)
    if n3 < minimum:
        print(n3)
    else:
        print(minimum)


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

get_minimum(num_1, num_2, num_3)
