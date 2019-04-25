import datetime

birthday_one = input()


datetime_object = datetime.datetime.strptime(birthday_one, '%d-%m-%Y').date()
modified_date = datetime_object + datetime.timedelta(days=1000)

date = modified_date.strftime("%d-%m-%Y")


print(date)
