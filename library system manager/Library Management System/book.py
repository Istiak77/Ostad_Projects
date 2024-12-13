import add_books
import view_all_books
import restore_books
from datetime import datetime
import update_books, delete_books


all_books = []


while True:
    print("Welcome to Library Management System")
    print("Q. to quit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Remove Book")

    all_books = restore_books.restore_all_books(all_books)
    
    menu = input("Select any number: ")
    
    if menu.upper() == "Q":
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        update_books.update_books(all_books)
    elif menu == "4":
        delete_books.delete_books(all_books)
    else:
        print("Choose a valid number")