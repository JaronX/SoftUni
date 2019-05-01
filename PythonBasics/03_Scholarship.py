from math import floor

income = float(input())
success = float(input())
minimal_salary = float(input())

social_scholarship = 0
excellent_scholarship = 0


if income < minimal_salary and success > 4.50:
    social_scholarship = 0.35 * minimal_salary

if success >= 5.50:
    excellent_scholarship = success * 25

if social_scholarship == 0 and excellent_scholarship == 0:
    print(f"You cannot get a scholarship!")
elif social_scholarship > excellent_scholarship:
    print(f"You get a Social scholarship {floor(social_scholarship)} BGN")
else:
    print(f"You get a scholarship for excellent results {floor(excellent_scholarship)} BGN")