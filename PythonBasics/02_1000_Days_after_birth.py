import datetime

birthday_one = input()
birthday_two = input()

datetime_object = datetime.datetime.strptime(birthday_one, '%d-%m-%Y').date()
modified_date = datetime_object + datetime.timedelta(days=999)

x = modified_date.strftime("%d-%m-%Y")


datetime_object2 = datetime.datetime.strptime(birthday_two, '%d-%m-%Y').date()
modified_date2 = datetime_object2 + datetime.timedelta(days=999)

x2 = modified_date2.strftime("%d-%m-%Y")

print(x)
print(x2)
