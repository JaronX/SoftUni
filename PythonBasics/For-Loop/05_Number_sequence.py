import sys

n = int(input())

max_number = -sys.maxsize - 1
min_number = sys.maxsize

for num in range(n):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    if current_number < min_number:
        min_number = current_number

print(f"""Max number: {max_number}
Min number: {min_number}""")