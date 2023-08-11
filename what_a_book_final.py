""" 
    title: what_a_book_final.py
    author: D.Coooper
    date: 1 Aug 2023
    description: what_a_book program
    Reference Professor Krasso & Peter Haas
"""








import sys
import mysql.connector
from mysql.connector import errorcode

# database config
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

# function to display the main menu
def show_menu():
    print("\n  -- Main Menu --")
    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        choice = int(input('      Enter your choice: '))
        return choice
    except ValueError:
        print("\n  Invalid input, program terminated...\n")
        sys.exit(0)

# function to display the list of books
def show_books(cursor):
    cursor.execute("SELECT book_id, book_name, author, details FROM book")
    books = cursor.fetchall()

    print("\n  -- DISPLAYING BOOK LISTING --")
    for book in books:
        print("  Book Name: {}\n  Author: {}\n  Details: {}\n".format(book[1], book[2], book[3]))

# function to display store locations
def show_locations(cursor):
    cursor.execute("SELECT store_id, locale FROM store")
    locations = cursor.fetchall()

    print("\n  -- DISPLAYING STORE LOCATIONS --")
    for location in locations:
        print("  Locale: {}\n".format(location[1]))

# function to validate user ID
def validate_user():
    try:
        user_id = int(input('\n      Enter your customer ID: '))
        if user_id < 1 or user_id > 3:
            print("\n  Invalid customer number, program terminated...\n")
            sys.exit(0)
        return user_id
    except ValueError:
        print("\n  Invalid input, program terminated...\n")
        sys.exit(0)

# function to display the account menu
def show_account_menu():
    print("\n      -- Customer Menu --")
    print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")

    try:
        account_option = int(input('        Enter your choice: '))
        return account_option
    except ValueError:
        print("\n  Invalid input, program terminated...\n")
        sys.exit(0)

# function to display user's wishlist
def show_wishlist(cursor, user_id):
    query = ("SELECT book.book_name, book.author "
             "FROM wishlist "
             "INNER JOIN book ON wishlist.book_id = book.book_id "
             "WHERE wishlist.user_id = {}".format(user_id))
    cursor.execute(query)
    wishlist = cursor.fetchall()

    print("\n        -- DISPLAYING WISHLIST ITEMS --")
    for book in wishlist:
        print("        Book Name: {}\n        Author: {}\n".format(book[0], book[1]))

# Function to display books not in user's wishlist
def show_books_to_add(cursor, user_id):
    query = ("SELECT book.book_id, book.book_name, book.author "
             "FROM book "
             "LEFT JOIN wishlist ON book.book_id = wishlist.book_id "
             "AND wishlist.user_id = {} "
             "WHERE wishlist.book_id IS NULL".format(user_id))
    cursor.execute(query)
    books_to_add = cursor.fetchall()

    print("\n        -- DISPLAYING AVAILABLE BOOKS --")
    for book in books_to_add:
        print("        Book ID: {}\n        Book Name: {}\n".format(book[0], book[1]))

# function to add book to user's wishlist
def add_book_to_wishlist(cursor, user_id, book_id):
    insert_query = "INSERT INTO wishlist(user_id, book_id) VALUES({}, {})".format(user_id, book_id)
    cursor.execute(insert_query)

# main program
try:
    db = mysql.connector.connect(**config)  # connect to the database
    cursor = db.cursor()  # create a cursor for MySQL queries

    print("\n  Welcome to the WhatABook Application!")

    while True:
        user_selection = show_menu()  # display the main menu

        if user_selection == 1:
            show_books(cursor)
        elif user_selection == 2:
            show_locations(cursor)
        elif user_selection == 3:
            user_id = validate_user()
            account_option = show_account_menu()

            while account_option != 3:
                if account_option == 1:
                    show_wishlist(cursor, user_id)
                elif account_option == 2:
                    show_books_to_add(cursor, user_id)
                    book_id = int(input("\n        Enter the ID of the book you want to add: "))
                    add_book_to_wishlist(cursor, user_id, book_id)
                    db.commit()
                    print("\n        Book ID: {} was added to your wishlist!".format(book_id))
                else:
                    print("\n      Invalid option, please retry...")

                account_option = show_account_menu()

        elif user_selection == 4:
            print("\n\n  Program terminated...")
            break
        else:
            print("\n      Invalid option, please retry...")

except mysql.connector.Error as err:
    print("Error:", err)
finally:
    if 'db' in locals() and db.is_connected():
        cursor.close()
        db.close()
