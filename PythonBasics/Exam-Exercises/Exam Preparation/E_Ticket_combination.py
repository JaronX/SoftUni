n = int(input())

counter = 0
prize = 0

for x1 in range(66, 77, 2):
    for x2 in range(102, 96, -1):
        for x3 in range(65, 68):
            for x4 in range(1, 10 + 1):
                for x5 in range(10, 1 - 1, -1):

                    counter += 1

                    if counter == n:
                        print(f"Ticket combination: {chr(x1)}{chr(x2)}{chr(x3)}{x4}{x5}")

                        prize = x1 + x2 + x3 + x4 + x5
                        print(f"Prize: {prize} lv.")

                        exit(0)