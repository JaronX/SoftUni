number = float(input())
unit_input = input()
unit_output = input()

if unit_input == "mm" and unit_output == "m":
    result = number / 1000

elif unit_input == "mm" and unit_output == "cm":
    result = number / 10

elif unit_input == "m" and unit_output == "cm":
    result = number * 100

elif unit_input == "m" and unit_output == "mm":
    result = number * 1000

elif unit_input == "cm" and unit_output == "mm":
    result = number * 10

elif unit_input == "cm" and unit_output == "m":
    result = number / 100


print(f"{result:.3f}")