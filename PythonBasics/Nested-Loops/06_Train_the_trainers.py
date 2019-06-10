n = int(input())
name_of_the_presentation = input()

grade_presentation = 0
final_grade = 0
counter = 0

while name_of_the_presentation != "Finish":

    for i in range(n):
        grade = float(input())
        grade_presentation += grade
        final_grade += grade
        counter += 1
    average_grade_presentation = grade_presentation / n

    print(f"{name_of_the_presentation} - {average_grade_presentation:.2f}.")

    grade_presentation = 0
    average_grade_presentation = 0

    name_of_the_presentation = input()

average_final_grade = final_grade / counter
print(f"Student's final assessment is {average_final_grade:.2f}.")

