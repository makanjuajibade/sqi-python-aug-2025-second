# OOP - Object Oriented Programming
# paradigm - way of doing things


# Functional
# Modular
# OOP - Classes and Objects


# name = ["Ife"
# "Makanjuola"]

# print(name)

# class BankAccount:
#     # magic dunder method - magic double underscore method
#     # initialize
#     def __init__(self, account_owner, balance, bank_name, is_savings):
#         self.account_owner = account_owner
#         self.account_balance = balance
#         self.bank_name = bank_name
#         self.is_savings = is_savings

#     def account_details(self):
#         details = f"Account Owner: {self.account_owner}\n"\
#                     f"Account Balance: {self.account_balance}\n"\
#                     f"Bank Name: {self.bank_name}\n"\
#                     f"Is Savings: {self.is_savings}\n"
#         return details


# ife_account = BankAccount("Ife", 1_000_000, "Access Bank", True)
# maryam_account = BankAccount("Maryam", 50_150_000, "Opay", False)
# damilola_account = BankAccount(bank_name="GTBank", account_owner="Damilola", balance=7_000_000_000, is_savings=False)

# print(ife_account.account_owner)
# print(maryam_account.bank_name)
# print(damilola_account.account_balance)

# print(ife_account.account_details())



# ife_account = {"account_owner": "Ife", "account_balance": 1_000_000}
# maryam_account = {"account_owner": "Maryam", "accoun_balance": 1_200_000}

# accounts = [ife_account, maryam_account]


# for account in accounts:
#     print(account['account_balance'])

# import datetime

# class Car:
#     def __init__(self, color, brand, model, year_made, plate_number, transmission_type, is_luxurious, price):
#         self.color = color
#         self.brand = brand
#         self.model = model
#         self.year_made = year_made
#         self.plate_number = plate_number
#         self.transmission_type = transmission_type
#         self.is_luxurious = is_luxurious
#         self.price = price

#     def years_since_made(self):
#         return datetime.datetime.now().year - self.year_made

#     def is_cheaper_than(self, amount):
#         return self.price < amount

# micra = Car("Red and cream", "Nissan", "Micra", 2012, "BDJ419-OY", "Manual", False, 2_500_000)
# bugatti = Car("Black", "Bugatti", "Chiron", 2020, "FST666-OY", "Automatic", True, 45_000_000)

# print(micra.plate_number) 
# print(bugatti.price)

# print(micra.years_since_made())
# print(bugatti.years_since_made())

# print(micra.is_cheaper_than(3_000_000))

# 2. Create a class called Car with the following attributes:
#    - brand
#    - model
#    - year
#    - horsepower
#    - fuel_type
#
#    The class should have a method called car_info() that returns:
#    "This is a {year} {brand} {model} with {horsepower} HP running on {fuel_type}."
#
#    After defining the class, create 3 different Car objects with different values.


int("6")

from enum import Enum

class NoteBookPage:
    def __init__(self, content: str, page_number: int, color: str):
        self.content = content
        self.page_no = page_number
        self.color = color

    def __str__(self):
        return f"{self.content[:20]}"
    
    def __repr__(self):
        return f"{self.content[:20]}"

class Medium(Enum):
    HARD = 'hard'
    SOFT = 'soft'

class NoteBook:
    def __init__(self, title: str, medium: Medium, pages: list[NoteBookPage]=None):
        self.title = title
        self.medium = medium
        self.pages = pages

        if pages is None:
            self.pages = []

    def __str__(self):
        return f"{self.title} ({self.medium.value} copy)"
    
    def add_page(self, content, page_no: int, color="white"):
        for page in self.pages:
            if page.page_no == page_no:
                return "This page number is already taken"
        self.pages.append(NoteBookPage(content, page_no, color))
        return "Successfully added page"

    def list_pages(self):
        if not self.pages:
            print("No pages in this notebook yet")
            return
        
        for page in self.pages:
            print("Content:")
            print(page.content)
            print("Color:",page.color)
            print("Page Number:",page.page_no)

my_diary = NoteBook("Winnie's Diary", Medium.SOFT)

# intro_page_biology = NoteBookPage("Introduction to Biology\nBiology surrounds us.", 3, "white")

# biology_textbook = NoteBook("Essential Biology", Medium.HARD, [intro_page_biology])


# print(my_diary)
# my_diary.list_pages()
# my_diary.add_page("Winnie's Diary", 23, "red")
# my_diary.list_pages()
# print(biology_textbook)


class CartItem:
    def __init__(self, item_name: str, price: int, quantity: int):
        self.name = item_name
        self.price = price
        self.quantity = quantity
    
    def total(self):
        return self.price * self.quantity

    
class Cart:
    def __init__(self, cart_items: list[CartItem]):
        self.cart_items = cart_items

    def total(self):
        total_price = 0
        for item in self.cart_items:            
            total_price += item.total()
        return total_price

cart_item1 = CartItem("eggs", 250, 4)
cart_item2 = CartItem("bread", 1200, 6)
cart = Cart([cart_item1, cart_item2])
print(cart.total()) 



# class Book:
#     def __init__(self, title: str, author: str, pages: int):
#         self.title = title
#         self.author = author
#         self.pages = pages


# class Library:
#     def __init__(self, books: list[Book]):
#         self.books = books

#     # def total_pages(self):
#     #     total_no_of_pages = 0
#     #     for book in self.books:
#     #         total_no_of_pages += book.pages
#     #     return total_no_of_pages

#     def total_pages(self):
#         return sum(book.pages for book in self.books)

# book1 = Book("Things Fall Apart", "Chinua Achebe", 300)
# book2 = Book("Purple Hibiscus", "Chimamanda Ngozi Adichie", 250)

# library = Library([book1, book2])

# print(library.total_pages())  # 550 



# class OrderItem:
#     def __init__(self, item, quantity):
#         self.item = item 
#         self.quantity = quantity


# class Order:
#     def __init__(self, order_items: list[OrderItem]):
#         self.order_items = order_items

# class Warehouse:

#     def __init__(self, inventory: dict[str, int]):
#         self.inventory = inventory

#     def place_order(self, order: Order):
#         for order_item in order.order_items:
#             if order_item.item in self.inventory and order_item.quantity <= self.inventory[order_item.item]:
#                 self.inventory[order_item.item] -= order_item.quantity
#                 return True
#             return False

# warehouse = Warehouse({
#     "laptop": 10,
#     "phone": 25,
#     "headphones": 50
# })

# order1 = Order([
#     OrderItem("laptop", 2),
#     OrderItem("phone", 5)
# ])

# order2 = Order([
#     OrderItem("laptop", 9), 
#     OrderItem("headphones", 2)
# ])

# print(warehouse.place_order(order1))
# # -> True

# print(warehouse.inventory)
# # -> {'laptop': 8, 'phone': 20, 'headphones': 50}

# print(warehouse.place_order(order2))
# # -> False

# print(warehouse.inventory)
# # -> {'laptop': 8, 'phone': 20, 'headphones': 50}



class Genre(Enum):
    HORROR = 'Horror'
    FICTION = 'Fiction'
    PSYCHOLOGICAL_THRILLER = 'Psychological Thriller'
    COMEDY = 'Comedy'
    ROM_COM = 'Romantic Comedy'
    SCI_FI = 'Sci Fi'


lookup = {g.value.lower(): g for g in Genre}


class Movie:
    def __init__(self, title: str, director: str, rating: int, duration_in_mins: int, genre: Genre):
        self.title = title
        self.director = director
        self.rating = rating
        self.duration_in_mins = duration_in_mins
        self.genre = genre

    def format_duration(self):
        return f"{self.duration_in_mins // 60} hrs, {self.duration_in_mins % 60} mins"
    

class Watchlist:
    def __init__(self, movies: list[Movie]):
        self.movies = movies

    def display_movies(self):
        for movie in self.movies:
            print(f"{movie.title} directed by {movie.director}. Duration: {movie.format_duration()}")

my_watchlist = Watchlist([])

while True:
    i = 1
    proceed = input(f"Enter the details for Movie {i} below or press 'stop' to stop or press the enter key to proceed: ").strip().lower()
    if proceed == 'stop':
        break

    title = input("Enter the title of the movie: ").strip()
    director = input("Enter the director of the movie: ").strip()
    rating = int(input("Enter the rating of the movie: "))
    duration_in_mins = int(input("Enter the duration in minutes of the movie: "))
    genre = input("Enter the genre of the movie: ").strip().lower()

    genre = lookup[genre]

    movie = Movie(title, director, rating, duration_in_mins, genre)
    my_watchlist.movies.append(movie)
    i += 1


my_watchlist.display_movies()