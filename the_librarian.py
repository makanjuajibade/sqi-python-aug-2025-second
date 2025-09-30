# Project Overview:
# Create a simple library management system where users can add, view, update, and delete 
# books in a file named `the_librarian.py`.

# Requirements:
# Data Storage: Use a list of dictionaries to store book information. Each book should have the following attributes:
# Title (string)
# Author (string)
# Year of publication (int)
# ISBN (string)
# Available (boolean)
# Functions/Actions:
# add_book(): Add a new book to the library.
# view_books(): Display all the books in the library.
# update_book(isbn): Update the information of a book given its ISBN.
# delete_book(isbn): Remove a book from the library using its ISBN.
# search_book(title): Search for a book by its exact title.
# borrow_book(isbn): Mark a book as borrowed (not available).
# return_book(isbn): Mark a book as returned (available).
# User Interface: Use a loop to display a menu and prompt the user for an action above until they choose to exit. Assume the user always inputs the correct data types.
# Define books at the top

books_in_the_library = [
    {"title": "Think Big", "author": "Ben Carson", "year_of_publication": 1992, "isbn": "987-3627-737-23", "available": True},
    {"title": "Rich Dad Poor Dad", "author": "Robert Kiyosaki", "year_of_publication": 1997, "isbn": "987-3879-875-23", "available": True},
    {"title": "The Whistler", "author": "John Grisham", "year_of_publication": 2016, "isbn": "987-3793-658-23", "available": True},
    {"title": "Martyr!", "author": "Kaveh Akbar", "year_of_publication": 2024, "isbn": "987-3893-563-23", "available": True},
]

def add_book(books_in_the_library: list):
    title = input("Enter the title of the book: ")
    author = input("Enter the name of the author: ")
    year_of_publication = input("Enter the year of publication: ")
    isbn = input("Enter the ISBN: ")

    new_book = {
        "title": title,
        "author": author,
        "year_of_publication": year_of_publication,
        "isbn": isbn,
        "available": True
    }
    books_in_the_library.append(new_book)
    print(f"Book {title} added successfully")

def view_books(books_in_the_library):
    if not books_in_the_library:   
        print("No books in the library.")
    else:
        for book in books_in_the_library:
            print(f"Title: {book['title']}, Author: {book['author']}, "
                  f"Year: {book['year_of_publication']}, ISBN: {book['isbn']}, "
                  f"Available: {book['available']}")

def update_book(books_in_the_library: list):
    inquired = input("Enter the ISBN of the book you want to update: ")

    for book in books_in_the_library:
        if inquired == book["isbn"]:
            book["title"] = input("Enter the new title of the book: ")
            book["author"] = input("Enter the new author of the book: ")
            book["year_of_publication"] = input("Enter the new year of publication: ")
            print(f"Book with ISBN {inquired} updated successfully.")
            return

    print("Book not found.")


def delete_book(books_in_the_library: list):
    inquired = input("Enter the ISBN of the book you want to update: ")
    for book in books_in_the_library:
        if inquired == book["isbn"]: 
            books_in_the_library.remove(book)
        print(f"You have successfully deleted book {book['title']}")
        return
    
    print("Book not found.")

def search_book(books_in_the_library: list):
    inquired = input("Enter title or author to search: ").lower()
    found = False
    
    for book in books_in_the_library:
        if inquired in book["title"].lower() or inquired in book["author"].lower():
            print(f"Title: {book['title']}, Author: {book['author']}, "
                  f"Year: {book['year_of_publication']}, ISBN: {book['isbn']}, "
                  f"Available: {book['available']}")
            found = True
    
    if not found:
        print("No matching book found.")


def borrow_book(books_in_the_library: list):
    inquired = input("Enter the ISBN of the book you want to borrow: ")

    for book in books_in_the_library:
        if inquired == book["isbn"]:
            if book["available"]:
                book["available"] = False
                print(f"You have successfully borrowed {book['title']}.")
            else:
                print("Sorry, this book is already borrowed.")
            return  

    print("Book not found.") 


def return_book(books_in_the_library: list):
    returned_book = input("Enter the ISBN of the book to be returned: ")

    for book in books_in_the_library:
        if returned_book == book["isbn"]:
            if not book["available"]:
                book["available"] = True
                print(f"You have successfully returned {book['title']}.")
            else:
                print(f"'{book['title']}' was not borrowed.")
            return
        
    print("Book not found")


menu = """Select Operation
1. Add a new book
2. View books in the library
3. Update the information of a book in the library 
4. Remove a book from the library
5. Search for a book
6. Borrow a book from the library
7. Return a book to the library
8. Exit
"""

print("Welcome to Ifeoluwa's Library")

while True:
    print(menu)
    choice = input("Enter your choice from 1 to 8: ")

    if choice not in "12345678":
        print("Invalid choice")
        continue

    if choice == "1":
        add_book(books_in_the_library)
    elif choice == "2":
        view_books(books_in_the_library)
    elif choice == "3":
        update_book(books_in_the_library) 
    elif choice == "4":
        delete_book(books_in_the_library)
    elif choice == "5":
        search_book(books_in_the_library)
    elif choice == "6":
        borrow_book(books_in_the_library)
    elif choice == "7":
        return_book(books_in_the_library)
    elif choice == "8":
        print("Exiting.....")
        break
