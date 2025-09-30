
book_info = "john doe ; the art of programming ; 2020 ; ISN 978-3-16-148410-0 ; 350 ; 2500"

# book_infp

components = book_info.split(" ; ")
# print(components)

# author = components[0]
# book_title = components[1]
# year_published = components[2]
# isbn = components[3]
# no_of_pages = components[4]
# cost = components[5]

author, book_title, year_published, isbn, no_of_pages, cost = components
author = author.title()
book_title = book_title.strip().title()
isbn = isbn.replace("ISN","ISBN") 
naira = "\u20A6"
cost = f"{naira}{int(cost):.2f}"

# The book `book_title` was written by `author` and published in `year_published`.
# It has `no_of_pages` pages and `isbn` and costs `cost`.Using the example above, the expected output is: he book The Art Of Programming was written by John Doe and published in 2020.
# It has 350 pages and ISBN 978-3-16-148410-0 and costs ₦2500.00.

sentence = (f"""The book {book_title} was written by {author} and published in {year_published} .
It has {no_of_pages} pages and {isbn} and costs {cost} .""")
print(sentence)

# print("author:", author)
# print("book_title:", book_title)
# print("year_published:", year_published)
# print("isbn:", isbn)
# print("no_of_pages:", no_of_pages)
# print("cost:", cost)


