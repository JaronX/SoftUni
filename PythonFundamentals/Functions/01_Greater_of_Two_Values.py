def greater_of_two_values(values_type, value1, value2):
    if values_type == "int":
        if int(value1) > int(value2):
            print(f'{value1}')
        else:
            print(f'{value2}')
    elif values_type == "char":
        if value1 > value2:
            print(f'{value1}')
        else:
            print(f'{value2}')
    else:
        if value1 > value2:
            print(f'{value1}')
        else:
            print(f'{value2}')

values_type = input()
value1 = input()
value2 = input()


greater_of_two_values(values_type, value1, value2)



