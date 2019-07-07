list_of_strings = input().split()

new_list = []
second_list = []

new_list.append(list_of_strings[-1])
second_list.extend(list_of_strings[:-1])


list_of_strings = new_list + second_list


convert_list_to_str = ''
for item in list_of_strings:
    convert_list_to_str += item + ' '


print(convert_list_to_str)