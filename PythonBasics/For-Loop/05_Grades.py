students = int(input())

grade_0 = 0
grade_1 = 0
grade_2 = 0
grade_3 = 0

total_grade = 0

for student in range(students):
    grade = float(input())

    if grade <= 2.99:
        grade_0 += 1
    elif grade <= 3.99:
        grade_1 += 1
    elif grade <= 4.99:
        grade_2 += 1
    else:
        grade_3 += 1

    total_grade += grade

average_all_students = total_grade / students

p0 = (grade_0 / students) * 100
p1 = (grade_1 / students) * 100
p2 = (grade_2 / students) * 100
p3 = (grade_3 / students) * 100

print(f"""Top students: {p3:.2f}%
Between 4.00 and 4.99: {p2:.2f}%
Between 3.00 and 3.99: {p1:.2f}%
Fail: {p0:.2f}%
Average: {average_all_students:.2f}""")
