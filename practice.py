# #INDEXING AND IMMUTABILITY
# #  a="This is a longer string"
# # print(a[1],a[2],a[10])
# # b ="This is a multiline string"
# # print(b[10])
# # STRING CONCATENATION
# # school = "SQI ICT ACADEMY"
# # location = "Dugbe,Ibadan"
# # print(school + " " + location)
# #
# #  STRING SLICING
# # text = "This is a multiline word"
# # print(text[0:6]) BASIC SLICING
# # print(text[:-8])NEGATIVE SLICING
# # print(text[-7:])NEGATIVE SLICING
# # print(text[2:9])BASIC SLICING
# # print(text[:6])OMITTING END
# # print(text[8:])OMITTING START
# # print(text[::-1])REVERSE SLICING
# # print(text[0:4:2])COMBINING START,END AND STEP
 
# # STRING INTERPOLATION
# # first_name = 'Ifeoluwa'
# # last_name = 'Makanju'
# # print('{} {}'.format (first_name, last_name)) FORMAT METHOD

# # name = 'Oluwakayode'
# # age = 25
# # height = 5.9
# # is_student = True
# # print(f'{name} is {age} years old,{height} feet tall, and it is {is_student} that he is a student') F-STRING METHOD
# # print('{} is {} years old,{} feet tall, and it is {} that he is a student.'.format(name,age,height,is_student)) FORMAT METHOD

# # Create two variables
# # location = "SQI"
# # greeting = "Good Morning,"
# # print(greeting + " " + location)


# # story = "It is {} that i slept early last night. My favourite food is {}.\nThe distance from my school to my house is {} km.\nAlso, my favourite number is {}" . format (slept_early, favourite_food, distance, favourite_num)
# # print(story)

# # story = """It is {} that i slept early last night.My favourite food is {}.
# # The distance from my school to my house is {}km. 
# # Also, my favourite number is {}.""".format(slept_early, favourite_food, distance, favourite_num)
# # print(story)

# # favourite_num = 34
# # favourite_food = "yam and egg"
# # slept_early = False
# # distance = 34.7

# # story = f"""It is {slept_early} that i slept early last night. My favourite food is {favourite_food}.
# # The distance from my school to my house is {distance}km
# # Also, my favourite number is {favourite_num}."""
# # print(story)
# # age = 12
# # # Concatenation
# # print("I am " + str(age) + " years old.")
# # # interpolation with format method
# # print("I am {} years old.".format(age))
# # #interpolation with f string 
# # print(f"I am {age} years old.")


# # 1. Create two string variables: first_name with value "John" and last_name with value 
# # "Smith". Concatenate them together with a space in between and print the result.
# first_name = "John"
# last_name = "Smith"
# print(first_name + " " + last_name)
# #2. Given the string word = "Python", print the first character.
# word = "Python"
# print(word[0])
# # 3. Create a string variable greeting with the value "Hello". Use string interpolation to insert the name "Alice" into the greeting and print the result.
# greeting = "Hello"
# name = "Alice"
# print(f"{greeting} {name}")
# # 4.Given the strings part1 = "Data" and part2 = "Science", concatenate them to form "DataScience" and print the result.
# part1 ="Data"
# part2 = "Science"
# print(part1 + part2 )
# # 5.Given the string phrase = "Welcome", print the last character using negative indexing.
# phrase = "Welcome"
# print(phrase[-1])
# #6.Create a string variable food with the value "pizza". Use string interpolation to create the sentence "I love pizza" and print it.
# food = "pizza"
# print(f"I love {food}")
# #7. Given the strings str_1 = "Good" and str_2 = "Morning", concatenate them with a space in between to form "Good Morning" and print the result.
# str_1 = "Good"
# str_2 = "Morning"
# print(str_1 + " " + str_2)
# #8. Given the string text = "Concatenate", print the character at index 5.
# text = "Concatenate"
# print(text[5])
# #9. Create a variable age with the value 25. Use string interpolation to create the sentence "I am 25 years old" and print it.
# age = 25
# print(f"I am {age} years old")
# # 10. Create three string variables: city = "New", space = " ", and country = "York". Concatenate them to form "New York" and print the result.
# city = "New"
# space = " "
# country = "York"
# print(city + space + country)
# # 11.Given the string alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ", print the 10th character.
# alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# print(alphabet[9])
# # 12. Create variables day = "Sunday" and activity = "hiking". Use string interpolation to create the sentence "On Sunday, I am going hiking" and print it.
# day = "Sunday"
# activity = "hiking"
# print(f"On {day}, I am going {activity}")
# #13. Given the strings a = "Super" and b = "Hero", concatenate them to form "SuperHero" and print the result.
# a = "Super"
# b = "Hero"
# print(a + b)

# # 14. Given the string universe = "MilkyWay", print the third character from the end using 
# # negative indexing.
# universe = "MilkyWay"
# print(universe[-3])
# # 15. Create variables item = "book" and price = 12.99. Use string interpolation to create the 
# # sentence "The price of the book is $12.99" and print it.
# item = "book"
# price = 12.99
# print(f"The price of the {item} is ${price}")
# # 16. Given the strings hello = "Hello" and world = "World", concatenate them with a comma and space 
# # in between to form "Hello, World" and print the result.
# hello = "Hello" 
# world = "World"
# print(hello +", "+ world)
# # 17. Given the string sequence = "ABCDEFG", print the character at index 4.
# sequence = "ABCDEFG"
# print(sequence[3])
# # 18. Create a variable language = "Python". Use string interpolation to create the sentence "I am 
# # learning Python" and print it.
# language = "Python"
# print(f"I am learning {language}")
# # 19. Given the strings start = "Once upon a" and end = " time", concatenate them to form "Once upon a 
# # time" and print the result.
# start = "Once upon a"
# end = "time"
# print(start + " " + end)
# # 20. Given the string sports = "Basketball", print the second character.
# sports = "Basketball"
# print(sports[1])
# # 21. Create a variable named x and assign the value 50 to it.
# x = 50
# #22. Create two string variables: first_name with value "John" and last_name with value "Doe". Concatenate them together and print the result.
# first_name = "John"
# last_name = "Doe"
# print(first_name + " "+ last_name)
# # 23. Create a string variable message with the value "Hello, ". Interpolate the variable name (assigned the value "Alice") into the message and print the result.
# message = "Hello"
# name = "Alice"
# print(f"{message} {name}")


# statement = "hello world"
# print(statement.upper().endswith())



# # 17. Convert a string “James John Kennedy” called “names” to a list using the string 
# # .split() method. Store the result in a list called “names_list”
# names = "James John Kennedy"
# names_list = (names.split())
# print(names_list)
# # 18. You have a list of cities called cities_list containing ['New York', 'Los Angeles', 
# # 'Chicago']. Convert this list into a single string where each city is separated by a 
# # semicolon and a space. Store the result in a string called cities_string.
# cities_list = ['New York', 'Los Angeles', 'Chicago']
# cities_string = "; ".join(cities_list)
# print(cities_string)
# # 19. Create a string variable sentence with the value "the quick brown fox jumps over the 
# # lazy dog". Capitalize the first letter of the string and 
# # print the result.
# sentence = "the quick brown fox jumps over the lazy dog"
# print(sentence.capitalize())
# # 20. Create a string variable book_title with the value "to kill a mockingbird". Capitalize 
# # the first letter of each word and print the result.
# book_title = "to kill a mockingbird"
# print(book_title.title())
# # 21. Create a string variable text with the value "hello world". Count the number of 
# # occurrences of the letter 'o' and print the result.
# text = "hello world"
# print(text.count("o"))
# # 22. Create a string variable filename with the value "document.txt". Check if the string 
# # starts with "doc" and print the result.
# filename = "document.txt"
# print(filename.startswith("doc"))
# # 23.	Create a string variable url with the value "https://www.example.com". Check if the 
# # string ends with ".com" and print the result.
# url = "https://www.example.com"
# print(url.endswith(".com"))
# # 24.	Create a string variable phrase with the value "find the needle in the haystack". Find 
# # the position of the word "needle" and print the result.
# phrase = "find the needle in the haystack"
# print(phrase.find("needle"))
# # 25. Create a string variable template with the value "Hello, {}. Welcome to {}.". Use the 
# # format() method to replace the placeholders with "Alice" and "Wonderland" and print the 
# # Result. Bonus point if you can do it with the f-string and concatenation methods also.
# template = "Hello, {}. Welcome to {}."
# placeholder1 = "Alice"
# placeholder2 = "Wonderland"
# print(template.format(placeholder1 ,placeholder2))
# print(f"Hello, {placeholder1}. Welcome to {placeholder2}.")
# print("Hello, " + placeholder1 + ". Welcome to " + placeholder2 + ".")
# # 26.	Create a string variable `quote` with the value "To be or not to be". Find the position 
# # of the word "not" and print the result.
# quote = "To be or not to be"
# print(quote.index("not"))
# # 27.	Create a string variable word with the value "hello". Check if all characters in the 
# # string are lowercase and print the result.
# word = "hello"
# print(word.islower())
# # 28.	Create a string variable shout with the value "HELLO". Check if all characters in the 
# # string are uppercase and print the result.
# shout = "HELLO"
# print(shout.isupper())
# # 29. Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# # lowercase and print the result.
# mixed_case = "PyThOn"
# print(mixed_case.lower())
# # 30. 	Create a string variable mixed_case with the value "PyThOn". Convert all characters to 
# # uppercase and print the result.
# mixed_case = "PyThOn"
# print(mixed_case.upper())
# # 31. 	Create a string variable padded_text with the value " hello ". Remove leading whitespace and 
# # print the result.
# padded_text = " hello "
# print(padded_text.lstrip())
# # 32. 	Create a string variable padded_text with the value " hello ". Remove trailing whitespace and 
# # print the result.
# padded_text = " hello "
# print(padded_text.rstrip())
# # 33.	Create a string variable padded_text with the value " hello ". Remove both leading and trailing 
# # whitespace and print the result.
# padded_text = " hello "
# print(padded_text.strip())
# # 34.	Create a string variable greeting with the value "Hello, World!". Replace "World" with "Alice" 
# # and print the result.
# greeting = "Hello, World!"
# print(greeting.replace("World" ,"Alice"))

book_info = "f. scott fitzgerald ; the great gatsby ; 1925 ; ISN 978-0-7432-7356-5 ; 180 ; 2799"
components = book_info.split(" ; ")
# author, book_title, year, isbn, no_of_pages, price = book_info
print(components)
author, book_title, year, isbn, no_of_pages, price = components
print(author)

#   INPUT FUNCTION
# name = input("What is your name?: ")
# print(f"Hello, {name}!")


# favorite_color
# Red is awesome!


# Ask the user to enter their location
# And ask them to enter their phone number

# Output:
# Location: SQI
# Phone Number: 09030556529

# location = input("Enter your location: ").strip()
# phone_number = input("Enter your phone number: ").strip()

# print(f"""Location: {location}
# Phone number: {phone_number}""")



# Ask the user for their first_name, last_name, email and phone number

# Output:

# Contact Information:
# Name: Winifred Igboama
# Email: winnie@gmail.com
# Phone: 09030556512


# first_name = input("Enter your first name: ").strip()
# last_name = input("Enter your last name: ").strip()
# email = input("Enter your email address: ").strip()
# phone_num = input("Enter your phone number: ").strip()


# print(f"""Contact Information:
# Name: {first_name} {last_name}
# Email: {email}
# Phone: {phone_num}""")


# john_favorite_num = input("John, enter your favorite number: ")

# benjamin_favorite_num = input("Benjamin, enter your favorite number: ")

# sum_of_their_nums = int(john_favorite_num) + int(benjamin_favorite_num)
# print("The sum of their favorite numbers is " + str(sum_of_their_nums))
# print(f"The sum of their favorite numbers is {sum_of_their_nums}")



# Ask the user for their age
# Tell them when they were born


# import datetime

# current_year = datetime.datetime.now().hour

# print(current_year)

# from datetime import datetime

# current_year = datetime.now().year

# age = input("How old are you now?: ")
# birth_year = current_year - int(age)
# print(f"You were born in {birth_year}")


# INPUT FUNCTION PRACTICE
# One has been done for you as an example:

# Sample Execution:
# Enter your name: David
# Enter the activity you did (e.g., running, cycling): Hiking
# Enter the duration of the activity (in minutes): 120
# Enter the calories burned: 850
#
# Fitness Activity:
# Name: David
# Activity: Hiking
# Duration: 120 minutes
# Calories Burned: 850 kcal
#
# Task:
# Write a Python program that works exactly like the sample above.
# The program should ask the user for their name, activity, duration, and calories burned,
# and then print the details in the same format.

# # Solution
# name = input("Enter your name: ")
# activity = input("Enter the activity you did (e.g., running, cycling): ")
# duration = input("Enter the duration of the activity (in minutes): ")
# calories = input("Enter the calories burned: ")

# print("\nFitness Activity:")
# print(f"Name: {name}")
# print(f"Activity: {activity}")
# print(f"Duration: {duration} minutes")
# print(f"Calories Burned: {calories} kcal")


# NOW DO THESE:
# Exercise 1:
# Sample Execution:
# Enter your first name: Alice
# Enter your last name: Johnson
#
# Full Name: Alice Johnson
#
# Task:
# Write a Python program that asks the user for their first name and last name,
# then prints their full name in the format shown above.
# SOLUTION
first_name = input("Enter your first name?: ")
last_name = input("Enter your last name?: ")
full_name = first_name + " " + last_name
print(f"Full name: {full_name}")

# Exercise 2:
# Sample Execution:
# Enter the length of the rectangle: 8
# Enter the width of the rectangle: 5
#
# Area of the rectangle: 40
#
# Task:
# Write a Python program that calculates the area of a rectangle.
# The program should ask for length and width, then display the area.
# SOLUTION
len_of_rec = input("What is the length of the rectangle?: ")
wid_of_rec = input("What is the width of the rectangle?: ")
area_of_rec = int(len_of_rec) * int(wid_of_rec)
print(f"Area of Rectangle = {area_of_rec}")

# Exercise 3:
# Sample Execution:
# Enter the temperature in Celsius: 25
#
# Temperature in Fahrenheit: 77.0
#
# Task:
# Create a Python program that converts a temperature from Celsius to Fahrenheit.
# Formula: F = (C × 9/5) + 32
# SOLUTION
celsius = input("Enter the temperature in celsius: ")
fahrenheit = (float(celsius) * 9/5) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")

# Exercise 4:
# Sample Execution:
# Enter the number of apples: 4
# Enter the number of bananas: 6
#
# Total fruits: 10
#
# Task:
# Write a program that asks the user for the number of apples and bananas,
# then prints the total number of fruits.
# SOLUTION
num_of_apples = input("Enter the number of apples: ").strip()
num_of_banana = input("Enter the number of banana: ").strip()
tot_fruits = int(num_of_apples) + int(num_of_banana)
print(f"Total fruits: {tot_fruits} ")

# Exercise 5:
# Sample Execution:
# Enter your age: 30
#
# You will be 35 years old in 5 years.
#
# Task:
# Create a program that asks the user for their age,
# then calculates and prints how old they will be in 5 years.
# SOLUTION
age = input("Enter your age: ")
new_age = int(age) + 5
print(f"You will be {new_age} years old in 5 years.")

# Exercise 6:
# Sample Execution:
# Enter the distance in kilometers: 10
#
# Distance in miles: 6.21371
#
# Task:
# Write a Python program that converts kilometers to miles.
# 1 kilometer = 0.621371 miles.
# SOLUTION
kilometers = float(input("Enter the distance in kilometers: "))
miles = kilometers * 0.621371
print(f"Distance in miles: {miles}")

# Exercise 7:
# Sample Execution:
# Enter your favorite color: Blue
# Enter your favorite food: Pizza
#
# Your favorite color is Blue and your favorite food is Pizza.
#
# Task:
# Write a Python program that asks the user for their favorite color and food,
# then displays the message exactly like the example.
# SOLUTION
fav_color = input("What is your favorite color?: ")
fav_food = input("What is your favorite food?: ")
print(f"Your favorite color is {fav_color} and your favourite food is {fav_food}.")

# Exercise 8:
# Sample Execution:
# Enter the price of an item: 50
# Enter the discount percentage: 20
#
# Price after discount: 40.0
#
# Task:
# Write a program that calculates the final price after a discount.
# Formula: final_price = price - (price × discount/100)
# SOLUTION
item_price = input("Enter the price of the item: ")
discount_perc = input("Enter the discount percentage: ")
final_price = float(item_price) - (float(item_price) * float(discount_perc)/100)
print(f"Price after discount: {final_price} ")
# Exercise 9:
# Sample Execution:
# Enter the number of hours worked: 40
# Enter your hourly rate: 15
#
# Weekly pay: 600
#
# Task:
# Write a program that calculates a worker's weekly pay
# based on hours worked and hourly rate.
# SOLUTION
num_of_hours = int(input("Enter the number of hours worked: "))
rate = int(input("Enter your hourly rate: "))
weekly_pay = num_of_hours * rate 
print(f"Weekly pay: {weekly_pay}")

# Exercise 10:
# Sample Execution:
# Enter your favorite movie: Inception
# Enter your favorite song: Bohemian Rhapsody
#
# Your favorite movie is Inception and your favorite song is Bohemian Rhapsody.
#
# Task:
# Create a Python program that asks the user for their favorite movie and song,
# then prints them in the same format as the example.
# SOLUTION
fav_movie = input("What is your favorite movie?: ")
fav_song = input("What is your favorite song?: ")
print(f"Your favorite movie is {fav_movie} and your favorite song is {fav_song}.")


# # # # 1. Write a program that asks the user for their name and then greets them with their 
# # # # name: Print a greeting message that includes the user's name in the format "Hello, {name}!".
# # # # SOLUTION
# # # name = input("What is your name?: ")
# # # print(f"Hello, {name}!")

# # # #2. Ask the user for their birth year and calculate their age. Print the user's age in the format “You are {age} years old.”.input9
# # # # SOLUTION
# # # birth_year = int(input("What is your birth year?: "))
# # # import datetime
# # # current_year = datetime.datetime.now().hour
# # # print(current_year)
# # # from datetime import datetime
# # # current_year = datetime.now().year
# # # age = current_year - birth_year
# # # print(f"You are {age} years old.")

# # # #3 Ask the user for their favourite color. Print a statement that includes the color in the format “Your favorite color is {favourite_color}.”.
# # # # SOLUTION
# # # fav_color = input("Enter your favorite color: ")
# # # print(f"Your favorite color is {fav_color}.")

# # # # 4. Ask the user to input some text and check if it is a palindrome. A palindrome is a word, phrase, or sequence that reads the same backwards as forwards, e.g. `madam` or `nurses run` or `121`.Print a statement in the format “It is {is_palindrome} that {text} is a palindrome.”. `is_palindrome` is either `True` or `False`.
# # # text = input("Enter a palindrome: ").strip().lower()
# # # is_palindrome = text == text[::-1]
# # # print(f"It is {is_palindrome} that {text} is a palindrome.")
# # # # 5. Create a program that asks the user to input a password and checks if it meets certain criteria (at least 8 characters and not more than 30 characters).Print a statement in the format “It is {is_valid} that the password fulfils the criteria.”. `is_valid` is either `True` or `False`.Bonus point if you can hide the password input from displaying on the screen as clear text.
# # # # SOLUTION
# # # import getpass
# # # password = getpass.getpass("Enter your password: ") 
# # # is_valid = 8 <= len(password) <= 30
# # # print(f"It is {is_valid} that the password fulfils the criteria.")
# # # #6. Write a program that asks the user for their weight (in kilograms) and height (in meters) and calculates their Body Mass Index (BMI). Calculate the BMI using the formula BMI = weight / (height ** 2). Round the BMI to 2 decimal places. Print a statement in the format “Your BMI is {BMI}”.
# # # # SOLUTION
# # # weight = float(input("Enter your weight: "))
# # # height = float(input("Enter your height: "))
# # # body_mass_index = weight / (height ** 2)
# # # bmi = f"{body_mass_index:.2f}"
# # # print(f"Your BMI is {bmi}.") 

# # # ------------------------------------------ ASSIGNMENT ------------------------------------------------
# # # 1. Create a list called fruits with items "apple", "banana", and "orange". Print the first item.
# # fruits = ["apple", "banana", "orange"]
# # print(fruits[0])

# # # 2. Create a list called colors with items "red", "green", "blue". Print the last item using negative indexing.
# # colors = ["red", "green", "blue"]
# # print(colors[-1])

# # # 3. Create a list called numbers with items from 1 to 10. Print items from index 3 to index 7.
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # print(numbers[3:8])

# # # 4. Create a list called alphabets with items "a", "b", "c", ..., "z". Print a slice from index -3 to the end.
# # alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
# # print(alphabets[-3:])

# # # 5. Create a list called ages with items 20, 30, 40. Change the value of the second item to 35.
# # ages = [20, 30, 40]
# # ages[1] = 35
# # print(ages)

# # # 6. Create a list called grades with items "A", "B", "C", "D". Change the values of items from index 1 to index 3 to "X".
# # grades = ["A", "B", "C", "D"]
# # grades[1:3] = ["X"]
# # print(grades)

# # #7. Create a list called cities with items "New York", "London", "Paris". Insert "Tokyo" at the beginning of the list.
# # cities = ["New York", "London", "Paris"]
# # cities.insert(0, "Tokyo")
# # print(cities) 

# # #8. Create a list called fruits with items "apple", "banana", "cherry". Print the number of items in the list.
# # fruits_1 = ["apple", "banana", "cherry"]
# # print(len(fruits_1))

# # # 9.Create a list called prices with items 10.5, 20.0, 15.75. Print the data type of the list.
# # prices = [10.5, 20.0, 15.75]
# # print(type(prices))

# # # 10. Create a list called mixed with items 10, "apple", True. Print the list.
# # mixed_with_items = [10, "apple", True]
# # print(mixed_with_items)

# # # 11. Create a tuple called tuple_data with items "a", "b", "c". Convert the tuple into a list.
# # tuple_data = ("a", "b", "c")
# # list(tuple_data)

# # # 12. Create a list called books with items "Python", "Java". Append "JavaScript" to the end of the list.
# # books = ["Python", "Java"]
# # books.append("Javascript")
# # print(books)

# # # 13. Create a list called names with items "Alice", "Bob", "Eve". Insert "Charlie" at index 1.
# # names = ["Alice", "Bob", "Eve"]
# # names.insert(1, "Charlie")
# # print(names)

# # # 14. Create two lists called list1 and list2 with items 1, 2, 3 and 4, 5, 6 respectively. Extend list1 with list2.
# # list_1 = [1, 2, 3]
# # list_2 = [4, 5, 6]
# # list_1.extend(list_2)
# # print(list_1)

# # # 15. Create a list called students with items "Alice", "Bob". Add items from a tuple ("Charlie", "David") to students.
# # students = ["Alice", "Bob"]
# # new_students = ("Charlie", "David") 
# # students.extend(new_students)
# # print(students)

# # # 16. Create a list called colors with items "red", "green", "blue". Remove "green" from the list.
# # colors_1 = ["red", "green", "blue"]
# # colors_1.remove("green")
# # print(colors_1)

# # # 17. Create a list called numbers with items 10, 20, 30, 40. Use the del keyword to remove the item at index 2.
# # numbers_1 = [10, 20, 30, 40]
# # del numbers_1[2]
# # print(numbers_1)

# # # 18. Create a list called fruits with items "apple", "banana", "cherry". Clear the list.
# # fruits_2 = ["apple", "banana", "cherry"]
# # fruits_2.clear()
# # print(fruits_2)

# # #  19.	Create a list called names with items "Zoe", "Alice", "Bob". Sort the list alphabetically.
# # names_1 = ["Zoe", "Alice", "Bob"]
# # names_1.sort()
# # print(names_1)

# # #  20. 	Create a list called ages with items 25, 35, 20. Sort the list in descending order.
# # ages_1 = [25, 35, 20]
# # ages_1.sort(reverse=True)
# # print(ages_1)

# # #  21. 	Sorting lists is CASE-SENSITIVE by default. Create a list called words with items 
# # # "Apple", "banana", "Orange". Sort the list in CASE-INSENSITIVE alphabetical order.
# # words_with_items = [ "Apple", "banana", "Orange"]
# # words_with_items.sort(key=str.lower)
# # print(words_with_items)

# # #  22. 	Create a list called numbers with items 1, 2, 3, 4. Print the list in reverse order.
# # numbers_2 = [1, 2, 3, 4]
# # numbers_2.sort(reverse=True)
# # print(numbers_2)

# # #  23.	Create a list called letters with items "a", "b", "c", "d". Print the list in reverse order using slicing.
# # letters = ["a", "b", "c", "d"]
# # letters = letters[::-1]
# # print(letters)

# # #  24.	Create a list called original with items "one", "two", "three". Create a copy of the list.
# # original = ["one", "two", "three"]
# # original_copy = original.copy()
# # print(original_copy)

# # #  25.	Create two lists called list1 with items "a", "b" and list2 with items "c", "d". Join list1 and list2 together.
# # list_1 = ["a", "b"]
# # list_2 = ["c", "d"]
# # list_1.extend(list_2)
# # print(list_1)

# # #  26.	Access and print the second subject of the first person in the list.	
# # data = [
# #     ["Alice", 25, ["Math", "Physics"]],
# #     ["Bob", 30, ["Chemistry", "Biology"]],
# #     ["Charlie", 35, ["History", "Geography"]]
# # ]
# # print(data[0][2][1])

# # #  27.	Access and print the first value in the list of numbers associated with "San Francisco".	
# # records = [
# #     ["New York", [10, 20, 30]],
# #     ["San Francisco", [40, 50, 60]],
# #     ["Austin", [70, 80, 90]]
# # ]
# # print(records[1][1][0])

# # #  28.	Get the first e in Ayo’s gender and Get Ben’s age.
# # group = [
# #     ["Ayo", ["Female", 12]],
# #     ["Ben", ["Male", 9]]
# # ]
# # print(group[0][1][0][1])
# # print(group[1][1][1])

# # #  29.	Get the l in Nina’s gender and Get Tobi’s age
# # records = [
# #     ["Tobi", ["Male", [6]]],
# #     ["Nina", ["Female", [7]]]
# # ]
# # print(records[1][1][0][4])
# # print(records[0][1][1][0])

# # #  30.	Get the two oo’s in X1’s 2nd mobility status (loose) together (slicing) and Get the battery percentage of R2
# # robot_grid = [
# #     ["R2", ["battery", [98]]],
# #     ["R5", ["status", "active"]],
# #     ["X1", [["joint", "loose"], "error"]]
# # ]
# # print(robot_grid[2][1][0][1][1:3])
# # print(robot_grid[0][1][1][0])

# # #  31.	Get the Five in the Jazz song title and Get the duration of the Jazz song
# # playlist = [
# #     ["Jazz", ["Take Five", 5.24]],
# #     ["Pop", ["Blinding Lights", 3.20]],
# #     ["Rock", ["Bohemian Rhapsody", 5.55]]
# # ]
# # print(playlist[0][1][1])
# # print(playlist[0][1][1])

# # #  32.	Get the letter v in Tiger’s category and Get the first letter of the Frog’s type
# # animals = [
# #     ["Elephant", ["Herbivore"]],
# #     ["Tiger", ["Carnivore"]],
# #     ["Frog", ["Amphibian"]]
# # ]
# # print(animals[1][1][0][5])
# # print(animals[2][1][0][0])





# # 1. Create a tuple called dimensions with values 10, 20, 30. Unpack the values into variables 
# # length, width, and height, and print each variable.
# dimensions = (10, 20, 30)
# length, width, height = dimensions
# print(length)
# print(width)
# print(height)

# # 2. Given the tuple coordinates:
# # coordinates = (1.5, 2.5, 3.5)
# # Unpack the tuple into variables x, y, and z, and print the value of y.
# coordinates = (1.5, 2.5, 3.5)
# x, y, z = coordinates
# print(y)

# # 3. Create a tuple called person with values ("John", 25, "Engineer"). Unpack the values into variables name, age, and profession, and print the value of profession.
# person = ("John", 25, "Engineer")
# _, _, profession = person
# print(profession)

# #4. Given the nested tuple data:
# # data = (("Alice", "Bob"), ("Math", "Science"), (90, 85))
# # Unpack the first element of data into variables student1 and student2, and print student2.
# data = (("Alice", "Bob"),
#         ("Math", "Science"), 
#         (90, 85)
#         )
# student_1, student_2 = data
# print(student_2)

# # 5. Create a tuple called colors with values ("red", "green", "blue", "yellow"). Unpack the first two values into variables color1 and color2, and print both variables.
# colors = ("red", "green", "blue", "yellow")
# color_1 , color_2 = colors[0:2]
# print(color_1)
# print(color_2)

# # 6. Given the tuple record:
# # record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# # Unpack the tuple to extract the name, the tuple containing age and position, and the list of departments. Print the extracted age and the first department.
# record = ("Jane", (32, "Manager"), ["HR", "Finance"])
# name, ageposition, list_of_deprtments = record
# print(ageposition[0])
# print(list_of_deprtments[0])
# #7. Create a tuple called triplet with values ("one", "two", "three"). Unpack the tuple into variables and print the value of the second variable.
# triplet = ("one", "two", "three")
# num_1, num_2, num_3 = triplet
# print(num_2)
# # 8. Given the tuple info:
# # info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# # Unpack the tuple to get the product ID, category, price, and manufacture date. Print the category and the manufacture year.
# info = ("product123", ("Electronics", 299.99), (20, 5, 2022))
# product_ID, categoryprice, manufacture_date = info
# print(categoryprice[0])
# print(manufacture_date)
# # 9. Create a tuple called nested_tuple with values (("a", "b"), ("c", "d"), ("e", "f")). Unpack the nested tuples into individual variables and print the second value of the third tuple.
# nested_tuple = (("a", "b"), ("c", "d"), ("e", "f"))
# tuple_1, tuple_2, tuple_3 = nested_tuple
# print(tuple_3[1])
# #10. Given the tuple inventory: inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# # Unpack the tuple to get each fruit and its corresponding quantity, then print the quantity of bananas.
# inventory = (("apples", 50), ("bananas", 100), ("cherries", 75))
# fruit_1, fruit_2, fruit_3 = inventory
# print(fruit_2[1])


# # ----------------------------------------ASSIGNMENTS--------------------------------
# #1. Create a dictionary called `student` with keys "name", "age", and "grade", and 
# # corresponding values "John", 20, and "A". Access and print the value of "name".
# student = {"name": "John", "age": 20, "grade": "A"}
# print(student["name"])

# #2. Create a dictionary called `product` with keys "name", "price", and "stock", and 
# # corresponding values "Laptop", 999.99, and 50. Change the value of "price" to 899.99.
# product = {"name": "Laptop", "price": 999.99, "stock": 50}
# product["price"] = 899.99
# print(product)

# # 3. Create a dictionary called `employee` with keys "name" and "position", and corresponding values "Alice" and "Manager". Add a new key "salary" with the value 50000.
# employee = {"name": "Alice", "position": "Manager"}
# employee["salary"] = 50000
# print(employee)

# #4. Create a dictionary called `inventory` with keys "apple", "banana", and "orange", and values 10, 5, and 8 respectively. Remove the key "banana".
# inventory = {"apple": 10, "banana": 5, "orange": 8}
# del inventory["banana"]
# print(inventory)

# # 5. Create a dictionary called person with keys "name", "age", and "city", and corresponding values "Bob", 25, and "New York". Use the copy() method to make a copy of the dictionary and call it person_copy.
# person = {"name": "Bob", "age": 25, "city": "New York"}
# person_copy = person.copy()
# print(person)
# print(person_copy)

# # 6. Create a nested dictionary called `family` with keys "child1", "child2", and "child3", each containing a dictionary with keys "name" and "age" with appropriate values. Access and print the age of "child2".
# family = {
#     "child1": [
#         {"name": "Adam", "age": 14},
#     ],
#     "child2": [
#         {"name": "Ayomide", "age": 16},
#     ],
#     "child3": [
#         {"name": "Temitayo", "age": 22}
#     ] 
# }
# print(family["child2"][0]["age"])
# #7. Create a dictionary called `car` with keys "brand", "model", and "year", and corresponding values "Toyota", "Corolla", and 2020. Access and print the value of "model".
# car = {"brand": "Toyota", "model": "corolla", "year": 2020}
# print(car["model"])

# # 8.Create a dictionary called `settings` with keys "volume", "brightness", and "language", and corresponding values 50, 75, and "English". Change the "language" to "Spanish".
# settings = {"volume": 50, "brightness": 75, "language": "English"}
# settings["language"] = "Spanish"
# print(settings)
# #9. Create a dictionary called `scores` with keys "math", "science", and "english", and corresponding values 90, 85, and 88. Remove the key "science".
# scores = {"math": 90, "science": 85, "english": 88}
# del scores["science"]
# print(scores)

# #10. Create a dictionary called `menu` with keys "starter", "main_course", and "dessert", and corresponding values "Soup", "Steak", and "Ice Cream". Check if the key "appetizer" is present in the dictionary.
# menu = {"starter": "Soup", "main_course": "Steak", "dessert": "Ice cream"}
# print("appetizer" in menu)

# # 11. Create a dictionary called `config` with keys "theme", "language", and "timezone", and corresponding values "dark", "English", and "UTC". Clear the dictionary.
# config = {"theme": "dark", "language": "English", "timezone": "UTC"}
# config.clear()
# print(config)

# #  12.	Create a dictionary called `phone_book` with keys "Alice", "Bob", and "Charlie", and corresponding phone numbers as values. Print the number of 
# # items in the dictionary.
# phone_book = {"Alice": "08030642834", "Bob": "07055229763", "Charlie": "08166735524"}
# print(len(phone_book))
# #  13. Create a dictionary called `grades` with keys "math", "science", and "history", 
# # and corresponding values "A", "B", and "C". Get a LIST of all the keys in the 
# # dictionary.
# grades = {"math": "A", "science": "B", "history": "C"}
# print(list(grades.keys()))

# #  14. 	Create a dictionary called `employee` with keys "name", "position", and 
# # "salary", and corresponding values "David", "Engineer", and 70000. Get a LIST 
# # of all the values in the dictionary.
# employee = {"name": "David", "position": "Engineer", "salary": 70000}
# print(list(employee.values()))

# #  15. 	Create a dictionary called `game` with keys "title", "genre", and "rating", and 
# # corresponding values "Minecraft", "Sandbox", and 4.5. Get a LIST of all 
# # key-value pairs in the dictionary.
# game = {"title": "Minecraft", "genre": "Sandbox", "rating": 4.5}
# my_list = list(game.items())
# print(my_list)


# # 1. Access and print the name of the teacher of "class2".
# school = {
#     "class1": {
#         "students": ["Alice", "Bob"],
#         "teacher": "Mr. Smith"
#     },
#     "class2": {
#         "students": ["Charlie", "David"],
#         "teacher": "Ms. Johnson"
#     }
# }
# print(school["class2"]["teacher"])
# # 2. Access and print the second employee in the "Engineering" department.
# company = {
#     "HR": ["Alice", "Bob"],
#     "Engineering": ["Charlie", "David"]
# }
# print(company["Engineering"][1])
# # 3. Access and print the name of the second assistant.
# university = {
#     "faculty": {
#         "professors": ["Dr. Smith", "Dr. Brown"],
#         "assistants": ["Ms. Green", "Mr. White"]
#     },
#     "students": ["John", "Jane", "Alice", "Bob"]
# }
# print(university["faculty"]["assistants"][1])
# #  4.	Access and print the price of the third fruit.
# store = {
#     "fruits": [
#         {"name": "apple", "price": 0.5},
#         {"name": "banana", "price": 0.2},
#         {"name": "cherry", "price": 1.5}
#     ],
#     "vegetables": [
#         {"name": "carrot", "price": 0.3},
#         {"name": "lettuce", "price": 1.0},
#         {"name": "onion", "price": 0.4}
#     ]
# }
# print(store["fruits"][2]["price"])
# #  5. 	Access and print the second non-fiction book.
# library = {
#     "fiction": ["1984", "To Kill a Mockingbird", "The Great Gatsby"],
#     "non-fiction": ["Sapiens", "Educated", "The Wright Brothers"]
# }
# print(library["non-fiction"][1])
# #  6. 	Access and print the age of the first child.	
# family = {
#     "parents": ["John", "Jane"],
#     "children": [
#         {"name": "Tom", "age": 5},
#         {"name": "Lucy", "age": 8}
#     ]
# }
# print(family["children"][0]["age"])
# #  7.	Access and print the name of the second main course.	
# restaurant = {
#     "menu": {
#         "appetizers": ["soup", "salad"],
#         "main_courses": ["steak", "pasta"],
#         "desserts": ["cake", "ice cream"]
#     },
#     "staff": ["Chef A", "Chef B", "Waiter X", "Waiter Y"]
# }
# print(restaurant["menu"]["main_courses"][1])
# #  8. 	Access and print the department of the user of the first desk.
# workspace = {
#     "desks": [
#         {"user": "Alice", "department": "HR"},
#         {"user": "Bob", "department": "Engineering"}
#     ],
#     "equipment": {"computers": 20, "printers": 10}
# }
# print(workspace["desks"][0]["department"])
# #  9. 	Access and print the name of the second designer.
# team = {
#     "developers": ["Dev A", "Dev B"],
#     "designers": ["Designer X", "Designer Y"],
#     "projects": ["Project 1", "Project 2"]
# }
# print(team["designers"][1])
# #  10. 	Access and print the second international destination.
# travel = {"domestic": ["Boston", "Chicago"], "international": ["Paris", "Tokyo"], "expenses": 
# {"flights": 1500, "hotels": 2000}}

# print(travel["international"][1])