text = input()

lower_case = []
upper_case = []
mixed = []

replacements = (',', ';', ':', '. ', '!', '(', ')', '"', "'", '\\', '/', '[', ']', "''", '  ', " .", '.')

for r in replacements:
    text = text.replace(r, ' ')

text_list = text.split()

for word in text_list:
    if word.islower() and word.isalpha():
        lower_case.append(word)
    elif word.isupper() and word.isalpha():
        upper_case.append(word)
    else:
        mixed.append(word)

print("Lower-case: " + ', '.join(lower_case))
print("Mixed-case: " + ', '.join(mixed))
print("Upper-case: " + ', '.join(upper_case))
