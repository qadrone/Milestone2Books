books = [
    {
        'name': 'b1',
        'author': 'a1',
        'read': False
    },
    {
        'name': 'b2',
        'author': 'a2',
        'read': True
    }
]


def add_book(name, author):
    books.append({'name': name, 'author': author, 'read': False})
    print(f"{name} has been added to your library.")


def list_books():
    for book in books:
        read = 'Yes' if book['read'] else 'No'
        print(f"{book['name']}\t{book['author']}\tRead: {read}")
    print(f"You have {len(books)} books in your library!")


def read_book(have_read):
    for book in books:
        if book['name'] == have_read:
            book['read'] = True
            print(f"'Have Read' status for {have_read} updated to: {book['read']}")


def delete_book(del_name):
    global books
    books = [book for book in books if book['name'] != del_name]
    print(f"{del_name} has been deleted from your library.")



