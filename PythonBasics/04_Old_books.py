search_book = input()
all_books = int(input())

counter = 0
checked_books = 0

while counter < all_books:

    book = input()

    if book != search_book:
        checked_books += 1

    if checked_books == all_books:
            print(f"""The book you search is not here!
            You checked {checked_books} books.""")

    elif book == search_book:
        print(f"You checked {checked_books} books and found it.")
        break

    counter += 1