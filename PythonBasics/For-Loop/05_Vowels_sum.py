word = input()

result = 0

for letter in word:
    if letter == "a":
        result += 1
    elif letter == "e":
        result += 2
    elif letter == "i":
        result += 3
    elif letter == "o":
        result += 4
    elif letter == "u":
        result += 5

print(result)


for index in range(0, len(word)):
    if word[index] == 'a':
        result += 1
    elif word[index] == 'e':
        result += 1