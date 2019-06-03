import sys

movies = int(input())

max_rating = -sys.maxsize - 1
min_rating = sys.maxsize
total_rating = 0

movie_highest_rating = None
movie_lowest_rating = None

for i in range(movies):
    name = input()
    rating = float(input())

    if rating > max_rating:
        max_rating = rating
        movie_highest_rating = name
    if rating < min_rating:
        min_rating = rating
        movie_lowest_rating = name

    total_rating += rating

average_rating = total_rating / movies

print(f"""{movie_highest_rating} is with highest rating: {max_rating:.1f}
{movie_lowest_rating} is with lowest rating: {min_rating:.1f}
Average rating: {average_rating:.1f}""")

