from utils import database_csv  # csv version

MENU_PROMPT = '''
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

что бы вы хотели сделать?: 
'''


def add_book_prompt():
    name = input('Enter book title: ')
    author = input('Enter author name: ')
    database_csv.add_book(name, author)


def list_books_prompt():
    books = database_csv.list_books()
    for book in books:
        read = 'Yes' if book['read'] == '1' else 'No'
        print(f"{book['name']} by {book['author']}, read: {read}")


def read_book_prompt():
    have_read = input("Enter name of book to be marked as /read/: ")
    database_csv.read_book(have_read)


def delete_book_prompt():
    del_name = input('Enter book to delete from library: ')
    database_csv.delete_book(del_name)


user_options = {
    "a": add_book_prompt,
    "l": list_books_prompt,
    "r": read_book_prompt,
    "d": delete_book_prompt
}


def options_menu():
    selection = input(MENU_PROMPT)
    while selection != 'q':
        if selection in user_options:
            selected_function = user_options[selection]
            selected_function()
        else:
            print('Unknown command. Please try again.')

        selection = input(MENU_PROMPT)


options_menu()
