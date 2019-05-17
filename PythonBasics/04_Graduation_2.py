name = input()

grade = 1
result = 0
failure_counter = 0

while grade <= 12:
    score = float(input())

    if score >= 4:
        result += score
        grade += 1
    else:
        failure_counter += 1
        if failure_counter > 1:
            print(f"{name} has been excluded at {grade} grade")
            break




if not failure_counter > 1:
    av_score = result / 12
    print(f"{name} graduated. Average grade: {av_score:.2f}")