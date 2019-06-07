import sys

current_result = 0
max_result = -sys.maxsize - 1
winner = None


while True:


    name = input()
    if name == "STOP":
        print(f"Winner is {winner} - {max_result}!")
        break


    for letter in name:
        current_result += ord(letter)

    if current_result > max_result:
        max_result = current_result
        winner = name

    current_result = 0
