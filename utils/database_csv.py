import csv


books_file = 'books_csv.txt'


def add_book(name, author):
    with open(books_file, 'a') as file:
        file.write(f"{name},{author},0\n")
    print(f"{name} has been added to your library.")


def list_books():
    with open(books_file, 'r') as file:
        lines = [line.strip().split(',') for line in file.readlines()]

    return [
        {'name': line[0], 'author': line[1], 'read': line[2]}
        for line in lines
    ]


def read_book(have_read):
    books = list_books()
    for book in books:
        if book['name'] == have_read:
            book['read'] = '1'
            read = 'Yes' if book['read'] == '1' else 'No'
            print(f"'Have Read' status for {have_read} updated to: {read}")
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(del_name):
    books = list_books()
    books = [book for book in books if book['name'] != del_name]
    _save_all_books(books)
    print(f"{del_name} has been deleted from your library.")



