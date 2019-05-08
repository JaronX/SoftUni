exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_in_minutes = (exam_hour * 60) + exam_minutes
arrival_in_minutes = (arrival_hour * 60) + arrival_minutes

late_time = arrival_in_minutes - exam_in_minutes
early_time = exam_in_minutes - arrival_in_minutes

if late_time > 0:
    print("Late")
    if late_time <= 59:
        print(f"{late_time} minutes after the start")
    else:
        hours = late_time // 60
        minutes = late_time % 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif 0 <= early_time <= 30:
    print("On time")
    if early_time != 0:
        print(f"{early_time} minutes before the start")
elif early_time > 30:
    print(f"Early")
    if early_time <= 59:
        print(f"{early_time} minutes before the start")
    else:
        hours = early_time // 60
        minutes = early_time % 60
        print(f"{hours}:{minutes:02d} hours before the start")