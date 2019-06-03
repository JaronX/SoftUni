visitors = int(input())

back = 0
chest = 0
legs = 0
abbs = 0
protein_shake = 0
protein_bar = 0

workout = 0
buyers = 0

for person in range(visitors):
    activity = input()

    if activity == "Back":
        back += 1
        workout += 1
    elif activity == "Chest":
        chest += 1
        workout += 1
    elif activity == "Legs":
        legs += 1
        workout += 1
    elif activity == "Abs":
        abbs += 1
        workout += 1
    elif activity == "Protein shake":
        protein_shake += 1
        buyers += 1
    elif activity == "Protein bar":
        protein_bar += 1
        buyers += 1

percent_work_out = (workout / visitors) * 100
percent_buyers = (buyers / visitors) * 100

print(f"""{back} - back
{chest} - chest
{legs} - legs
{abbs} - abs
{protein_shake} - protein shake
{protein_bar} - protein bar
{percent_work_out:.2f}% - work out
{percent_buyers:.2f}% - protein""")