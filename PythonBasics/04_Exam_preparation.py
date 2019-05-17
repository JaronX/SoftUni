unsatisfactory_assessments = int(input())

problems_count = 0
rating_total = 0
unsatisfactory_assessments_count = 0
last_problem_name = None

while True:
    problem_name = input()

    if problem_name == "Enough":
        average_score = rating_total / problems_count
        print(f"""Average score: {average_score:.2f}
        Number of problems: {problems_count}
        Last problem: {last_problem_name}
    """)
        break

    rating = int(input())

    problems_count += 1
    rating_total += rating

    last_problem_name = problem_name

    if rating <= 4:
        unsatisfactory_assessments_count += 1

    if unsatisfactory_assessments_count == unsatisfactory_assessments:
        print(f"You need a break, {unsatisfactory_assessments_count} poor grades.")
        break