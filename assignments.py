
# # # 1. Create a set called fruits with values {"air", "water", "food"}. Check if "food" is in 
# # # the set and print the result.
# # fruits = {"air", "water", "food"}
# # print("food" in fruits)

# # #2. Create a set called colors with values {"red", "green", "blue"}. Add the color "yellow" 
# # # to the set and print the updated set.
# # colors = {"red", "green", "blue"}
# # colors.add("yellow",)
# # print(colors)

# # # 3. Given the set animals = {"cat", "dog", "rabbit"}, add multiple items ["horse", "sheep"] to the set and print the updated set.
# # animals = {"cat", "dog", "rabbit"}
# # other_animals = {"horse", "sheep"}
# # animals.update(other_animals)
# # print(animals)

# # # 4. Create a set called countries with values {"USA", "Canada", "Mexico"}. Remove "Canada" from the set and print the updated set.
# # countries = {"USA", "Canada", "Mexico"}
# # countries.remove("Canada")
# # print(countries)
# # #5.  Given the set cities = {"New York", "Los Angeles", "Chicago"}, remove "Houston" which is not in the set without raising an error.
# # cities = {"New York", "Los Angeles", "Chicago"}
# # cities.discard("Houston")
# # print(cities)

# # # 6. Given the list seasons = ["Spring", "Summer", "Fall", "Winter", “Spring”], convert the list to a set to get rid of the duplicate `Spring`.
# # seasons = ["Spring", "Summer", "Fall", "Winter", "Spring"]
# # print(set(seasons))

# # # 7. Create two sets, set1 = {1, 2, 3} and set2 = {3, 4, 5}. Use the union method to join the sets and print the result.
# # set1 = {1, 2, 3} 
# # set2 = {3, 4, 5}
# # set3 = set1.union(set2)
# # print(set3)

# # # 8. Given two sets, setA = {"a", "b", "c"} and setB = {"c", "d", "e"}, find the intersection of the sets and print the result.
# # setA = {"a", "b", "c"}
# # setB = {"c", "d", "e"}
# # setC = setA.intersection(setB)
# # print(setC)

# # #9. Create a set called prime_numbers with values {2, 3, 5, 7}. Add the number 11 to the set and print the updated set.
# # prime_numbers = {2, 3, 5, 7}
# # prime_numbers.add(11,)
# # print(prime_numbers)

# # #10.  Given the set odd_numbers = {1, 3, 5, 7, 9}, remove a random item from the set and print the updated set.
# # odd_numbers = {1, 3, 5, 7, 9}
# # odd_numbers.pop()
# # print(odd_numbers)

# # # 11. Create a set called vowels with values {"a", "e", "i", "o", "u"}. Empty the set and print the result.
# # vowels = {"a", "e", "i", "o", "u"}
# # vowels.clear()
# # print(vowels)

# # # 12. Given the set letters = {"a", "b", "c"}, find the difference between `letters` and another set {"b", "c", "d"}. Print the result. Afterwards, find the symmetric difference and print the result.
# # letters = {"a", "b", "c"}
# # more_letters = {"b", "c", "d"}
# # new_letters = letters.difference(more_letters)
# # print(new_letters)

# # #  13.	Create a set called tech_brands with values {"Apple", "Google", "Microsoft"}. 
# # # 	Add the items from another set {"Amazon", "Facebook"} and print the updated set 
# # # 	tech_brands without creating a new set.
# # tech_brands = {"Apple", "Google", "Microsoft"}
# # other_tech_brands = {"Amazon", "Facebook"}
# # tech_brands.update(other_tech_brands)
# # print(tech_brands)
# # #  14. 	Create a set called students with values {"Alice", "Bob", "Charlie", "David"}. Use the 
# # # 	remove method to remove "Charlie" from the set and print the updated set. Then try to 
# # # 	remove "Eve" from the set and observe the behavior.
# # students = {"Alice", "Bob", "Charlie", "David"}
# # students.remove("Charlie")
# # print(students)
# # # students.remove("Eve")
# # # print(students)

# # #  15. 	Given a list numbers_list = [1, 2, 3, 4, 4, 5, 5], convert this list to a set to remove 
# # # 	duplicates and print the resulting set.
# # numbers_list = [1, 2, 3, 4, 4, 5, 5]
# # my_set = set(numbers_list)
# # print(my_set)

# # #  16. 	Given a string text = "hello", convert this string to a set to find the unique 
# # # 	characters and print the resulting set.
# # text = "hello"
# # text = set(text)
# # print(text)

# # #  17. 	Create a set called vehicles with values {"car", "bike", "bus", "train"}. Find out how 
# # # 	many items are in the set and print the result.
# # vehicles = {"car", "bike", "bus", "train"}
# # print(len(vehicles))

# # #  18. 	Given the set gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}, print the 
# # # 	number of items in the set.
# # gadgets = {"laptop", "smartphone", "tablet", "smartwatch"}
# # print(len(gadgets))




# # ===============================
# # Nested Dictionary Modification Exercises
# # ===============================

# # # Q1. Given this dictionary, change the "math" score to 95.
# # student = {
# #     "name": "Alice",
# #     "scores": {"math": 80, "english": 85}
# # }
# # student["scores"]["math"] = 95
# # print(student)
# # # Expected Output:
# # # {'name': 'Alice', 'scores': {'math': 95, 'english': 85}}


# # # Q2. Add a new subject "science" with score 90 inside "scores".
# # student = {
# #     "name": "Alice",
# #     "scores": {"math": 80, "english": 85}
# # }
# # student["scores"]["Science"] = 90
# # print(student)
# # # Expected Output:
# # # {'name': 'Alice', 'scores': {'math': 80, 'english': 85, 'science': 90}}


# # # Q3. Change the author's name of "Python 101" to "Mike".
# # library = {
# #     "Python 101": {"author": "Tom", "year": 2020},
# #     "Data Science": {"author": "Jane", "year": 2021}
# # }
# # library["Python 101"]["author"] = "Mike"
# # print(library)
# # # Expected Output:
# # # {'Python 101': {'author': 'Mike', 'year': 2020}, 'Data Science': {'author': 'Jane', 'year': 2021}}


# # # Q4. Add a new key "publisher" = "O'Reilly" to "Data Science".
# # library = {
# #     "Python 101": {"author": "Tom", "year": 2020},
# #     "Data Science": {"author": "Jane", "year": 2021}
# # }
# # library["Data Science"]["publisher"] = "O'Reilly"
# # print(library)
# # # Expected Output:
# # # {'Python 101': {'author': 'Tom', 'year': 2020}, 'Data Science': {'author': 'Jane', 'year': 2021, 'publisher': "O'Reilly"}}



# # # Q5. In this dictionary, add a new phone number "work": "555-999" for Alice.
# # contacts = {
# #     "Alice": {"home": "555-123", "mobile": "555-456"},
# #     "Bob": {"home": "555-789"}
# # }
# # contacts["Alice"]["work"] = "555-456"
# # print(contacts)
# # # Expected Output:
# # # {'Alice': {'home': '555-123', 'mobile': '555-456', 'work': '555-999'}, 'Bob': {'home': '555-789'}}


# # # Q6. Change Bob’s "home" number to "555-000".
# # contacts = {
# #     "Alice": {"home": "555-123", "mobile": "555-456"},
# #     "Bob": {"home": "555-789"}
# # }
# # contacts["Bob"]["home"] = "555-000"
# # print(contacts)
# # # Expected Output:
# # # {'Alice': {'home': '555-123', 'mobile': '555-456'}, 'Bob': {'home': '555-000'}}
  
# # # Q7. Add a new student {"name": "Eve", "scores": {"math": 88, "english": 92}}
# # # into the list of students.
# # students = [
# #     {"name": "Alice", "scores": {"math": 80, "english": 85}},
# #     {"name": "Bob", "scores": {"math": 75, "english": 70}}
# # ]
# # item = {"name": "Eve", "scores": {"math": 88, "english": 92}}
# # students.append(item)
# # print(students)
# # # Expected Output:
# # # [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}},
# # #  {'name': 'Bob', 'scores': {'math': 75, 'english': 70}},
# # #  {'name': 'Eve', 'scores': {'math': 88, 'english': 92}}]



# # # Q8. Change Bob's english score from 70 to 78.
# # students = [
# #     {"name": "Alice", "scores": {"math": 80, "english": 85}},
# #     {"name": "Bob", "scores": {"math": 75, "english": 70}}
# # ]
# # students[1]["scores"]["english"] = 78
# # print(students)
# # # Expected Output:
# # # [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}},
# # #  {'name': 'Bob', 'scores': {'math': 75, 'english': 78}}]


# # # Q9. Add a new dictionary {"year": 2022, "semester": "Spring"} 
# # # inside Alice’s record under a new key "enrollment".
# # students = [
# #     {"name": "Alice", "scores": {"math": 80, "english": 85}},
# #     {"name": "Bob", "scores": {"math": 75, "english": 78}}
# # ]
# # new_dict = {"year": 2022, "semester": "Spring"} 
# # students.append(new_dict)
# # print(students)
# # # Expected Output:
# # # [{'name': 'Alice', 'scores': {'math': 80, 'english': 85}, 'enrollment': {'year': 2022, 'semester': 'Spring'}},
# # #  {'name': 'Bob', 'scores': {'math': 75, 'english': 78}}]



# # # Q10. In this shop cart, add a new product "Notebook" with price 200.
# # cart = {
# #     "items": [
# #         {"name": "Pen", "price": 10},
# #         {"name": "Book", "price": 50}
# #     ],
# #     "owner": "Alice"
# # }
# # new_item = {"name": "Notebook", "price": 200}
# # cart["items"].append(new_item)
# # print(cart)
# # # Expected Output:
# # # {'items': [{'name': 'Pen', 'price': 10}, {'name': 'Book', 'price': 50}, {'name': 'Notebook', 'price': 200}],
# # #  'owner': 'Alice'}

# # # ----------------------------------------------------ASSIGNMENTS----------------------------------------------------------
# # # 1. Collect two numbers as input from the user and assign as variables, a and b, write an if statement that prints "a and b are both positive" if both a and b are positive, prints "Only one is positive" if one of them is positive, and prints "Neither is positive" if neither is positive.
# # a = int(input("Enter a number: ").strip())
# # b = int(input("Enter another number: ").strip())
# # if a > 0 and b > 0:
# #     print("a and b are both positive")
# # elif (a > 0 and b <= 0) or (a <= 0 and b > 0):
# #     print("Only one is postive")
# # else:
# #     print("Neither is positive")

# # # 2. Collect three numbers x, y and z as a comma separated string input from the user and print "Increasing order" if they are in STRICTLY increasing order, "Decreasing order" if they are in STRICTLY decreasing order, and "Neither" otherwise.
# # x, y, z = (input("Enter three numbers separated by commas: ").strip().split(", "))

# # if (x < y) and (y < z):
# #     print("Increasing order")
# # elif (x > y) and (y > z):
# #     print("Decreasing order")
# # else:
# #     print("Neither")

# # 3. Write a program that reads a string called `palindrome` supplied through user input and checks if it is a palindrome. Print "Is a palindrome" if it is, otherwise print "Not a palindrome".
# # palindrome = input("Enter a palindrome: ").lower().strip().replace(" ", "")
# # if palindrome == palindrome[::-1]:
# #     print("Is a palindrome")
# # else:
# #     print("Not a palindrome")

# # 4. You have three variables: x, y, and z collected as 3 separate inputs from the user. Write an if statement that checks if exactly two out of the three variables are equal and prints "Two are equal" if this is true. Otherwise, print "All different" or "All same" accordingly.
# # x = int(input("Enter a number: ").strip())
# # y = int(input("Enter another number: ").strip())
# # z = int(input("Enter a new number: ").strip())
# # if (x == y) and (y == z) and (x == z):
# #     print("All are the same")
# # elif(x == y) or (y == z) or (x == z):
# #     print("Two are equal")
# # else:
# #     print("All are different")

# # # 5. Given three angles angle1, angle2, and angle3 collected as 3 separate inputs from the user, use if statements to check if they can form a valid triangle. Print "Valid triangle" if the sum of the angles is 180 degrees and all angles are greater than 0. Otherwise, print "Invalid triangle".
# # angle1 = int(input("Enter a number below 180: ").strip())
# # angle2 = int(input("Enter another number below 180: ").strip())
# # angle3 = int(input("Enter a new number below 180: ").strip())
# # if  angle1 + angle2 + angle3 == 180 and angle1 > 0 and angle2 > 0 and angle3 > 0:
# #     print("Valid triangle")
# # else:
# #     print("Invalid triangle")

# # # 6. You have a single character variable `ch` supplied through user input. Write an if statement that prints "Vowel" if ch is a vowel (a, e, i, o, u, both uppercase and lowercase), and "Consonant" otherwise. Assume that the input is a single alphabet character.
# # ch = input("Enter a single character: ").strip()
# # if ch in "aeiouAEIOU":
# #     print("Vowel")
# # else:
# #     print("Consonant")

# # 7. Given a comma separated string input from the user of three colors color1, color2, and color3, write an if statement to check if all three colors are primary colors (red, blue, yellow). Print "All primary colors" if they are, otherwise print "Not all primary colors".
# # color1, color2, color3 = (input("Enter three colors separated by commas: ").lower().strip().split(", "))
# # primary_colors = ["red", "blue", "yellow"]
# # if color1 in primary_colors and color2 in primary_colors and color3 in primary_colors:
# #     print("All are primary colors")
# # else:
# #     print("Not all are primary colors")
    
# # 8. You have a variable `mode` supplied by the user which can be "manual", "automatic", or "off". Write an if statement that prints "Manual mode activated" if mode is "manual", "Automatic mode activated" if mode is "automatic", and "System is off" if mode is "off".
# # mode = input("Enter a mode either manual or automatic or off: ").strip()
# # if mode == "manual" or mode == "automatic":
# #     print(f"{mode} mode activated")
# # elif mode == "off":
# #     print("System is off")
# #  else:
# #      print("Invalid mode")

# #  9. Given a string `message` entered by the user, use if statements to check if the message contains any of the words "urgent", "important", or "immediate". If it contains any of these words, print "High priority message". Otherwise, print "Normal message".
# # message = input("Enter a message: ").strip()
# # if "urgent" in message or "important" in message or "immediate" in message:
# #     print("High priority message")
# # else:
# #     print("Normal message")

# # # 10. You have two variables, status1 and status2, provided through user input, each of which can be "active", “inactive", or "pending". Write an if statement to print "Both active" if both statuses are "active", "One active" if exactly one is "active",	and "None active" if neither is "active".
# # status1 = input("Enter a status either active, inactive or pending: ").strip()
# # status2 = input("Enter a new status either active, inactive or pending: ").strip()
# # if status1 == "active" and status2 == "active":
# #     print("Both active")
# # elif status1 == "active" or status2 == "active":
# #     print("One active")
# # else:
# #     print("None active")

# #  11. 	Given a string `filename` supplied by the user, write an if statement to check if the	filename ends with “.jpg", ".png", or ".gif". Print "Image file" if it does, otherwise	print "Not an image file".
# # filename = input("Enter a fiename: ").strip()
# # if filename.endswith(".jpg") or filename.endswith(".png") or filename.endswith(".gif"):
# #     print("Image file")
# # else:
# #     print("Not an image file")
# #  12. 	You have a variable `access_level` provided through user input which can be "admin",	"user", or "guest". Write an if statement that prints "Full access" if access_level is	"admin", "Limited access" if it is "user", and "No access" if it is "guest".
# # access_level = input("Enter your access level: ")
# # if access_level == "admin":
# #     print("Full access")
# # elif access_level == "user":
# #     print("Limited access")
# # #  13. 	Given a string `email` collected from the user, write an if statement to check if the email contains both "@" and 	"." characters. Print "Valid email" if it does, otherwise	print "Invalid email".

# # #  14. 	You have a variable `day` provided by user input which can be any day of the week 	(e.g., "Monday", "Tuesday", 	etc.). Write an if statement that prints "Weekend" if the	day is "Saturday" or "Sunday", and "Weekday" if it is any other day.
# # day = input("Enter any day of the week: ").capitalize()
# # weekdays = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday")
# # weekend = ("Saturday", "Sunday")
# # if day in weekend:
# #     print("Weekend")
# # else:
# #     print("Weekdays")
# # 15. 	Write a program that takes three numbers (num1, num2, num3) as a comma-separated string 	input from the user and prints the greatest number. Use conditional statements to determine which number is the greatest. Bonus point if you can do it without `else` statements.





# # --------------------------------------------------ASSIGNMENT---------------------------------------------
# # -------------------------------ASSIGNMENT 27th August, 2025-------------------------------
# # Exercise 1
# # An amusement park ride has these rules:
# # - Must be at least 120 cm tall to ride.
# # - If under 120 cm but with an adult, still allowed.
# # - Otherwise, not allowed.
# #
# # Example input/output executions:
# #
# # Enter height: 130
# # With adult? no
# # Output: Allowed
# #
# # Enter height: 110
# # With adult? yes
# # Output: Allowed
# #
# # Enter height: 110
# # With adult? no
# # Output: Not allowed
# #
# # Enter height: 119
# # With adult? yes
# # Output: Allowed
# #
# # Enter height: 100
# # With adult? no
# # Output: Not allowed
# #
# # Enter height: 150
# # With adult? no
# # Output: Allowed
 
# height = int(input("Enter your height in cm: "))
# with_adult = input("Are you with an adult? (yes or no): ").lower()

# if height >= 120 or with_adult == "yes":
#     print("Allowed to ride")
# else:
#     print("Not allowed to ride")

# # Exercise 2
# # An exam grading system with retake rule:
# # The user enters exam score and retake status ("yes" or "no").
# # - If score is at least 50, print "Pass".
# # - If score is less than 50 but retake is "yes", print "Retake allowed".
# # - If score is less than 50 and no retake, print "Fail".

# score = int(input("Enter your exam score: "))
# retake_status = input("Would you like to retake the exam again? (yes or no): ").lower().strip()
# if score >= 50:
#     print("Pass")
# elif 0 <= score < 50 and retake_status == "yes":
#     print("Retake alllowed")
# elif 0 <= score < 50 and retake_status == "no":
#     print("Fail")
# else:
#     print("Invalid score")
# # Example input/output executions:
# #
# # Enter score: 42
# # Retake? yes
# # Output: Retake allowed
# #
# # Enter score: 42
# # Retake? no
# # Output: Fail
# #
# # Enter score: 50
# # Retake? no
# # Output: Pass
# #
# # Enter score: 75
# # Retake? yes
# # Output: Pass
# #
# # Enter score: 10
# # Retake? no
# # Output: Fail



# # # Exercise 3
# # A ride-hailing app calculates trip approval:
# # The user enters distance (km) and wallet balance.
# # Each km costs 200 units.
# # - If wallet balance is enough for the trip, print "Trip confirmed".
# # - If balance is less but at least half the cost, print "Add funds".
# # - If less than half, print "Trip denied".

# distance = float(input("Enter your estimated distance: "))
# wallet_balance = float(input("Enter your wallet balance: "))
# cost = distance * 200
# if wallet_balance >= cost:
#     print("Trip confirmed")
# elif wallet_balance <= cost/2:
#     print("Add funds")
# else:
#     print("Trip denied")

# # Example input/output executions:
# #
# # Enter distance: 10
# # Enter wallet balance: 800
# # Output: Trip denied
# # Reasoning: cost = 10 * 200 = 2000; half = 1000; balance = 800.
# # 800 < 1000 (less than half), so "Trip denied".
# #
# # Enter distance: 10
# # Enter wallet balance: 2000
# # Output: Trip confirmed
# # Reasoning: cost = 2000; balance = 2000.
# # balance >= cost, so "Trip confirmed".
# #
# # Enter distance: 10
# # Enter wallet balance: 1000
# # Output: Add funds
# # Reasoning: cost = 2000; half = 1000; balance = 1000.
# # not enough (1000 < 2000) but balance >= half, so "Add funds".
# #
# # Enter distance: 10
# # Enter wallet balance: 400
# # Output: Trip denied
# # Reasoning: cost = 2000; half = 1000; balance = 400.
# # balance < half, so "Trip denied".
# #
# # Enter distance: 5
# # Enter wallet balance: 500
# # Output: Add funds
# # Reasoning: cost = 5 * 200 = 1000; half = 500; balance = 500.
# # not enough (500 < 1000) but exactly half, so "Add funds".



# # Exercise 4
# # An airport boarding system:
# # The user enters boarding pass ("yes"/"no") and passport ("yes"/"no").
# # - If both are "yes", print "Proceed to boarding".
# # - If boarding pass is missing, print "No boarding pass".
# # - If passport is missing, print "No passport".
# # - If both missing, print "Denied entry".

# boarding_pass = input("Are you with your boarding pass? (yes or no): ").lower().strip()
# passport = input("Are you with your passport? (yes or no): ").lower().strip()
# if boarding_pass == "yes" and passport == "yes":
#     print("Proceed to boarding")
# elif boarding_pass == "no":
#     print("No boarding pass")
# elif passport == "no":
#     print("No passport")
# else:
#     print("Denied entry")

# # Example input/output executions:
# #
# # Boarding pass? no
# # Passport? yes
# # Output: No boarding pass
# #
# # Boarding pass? yes
# # Passport? no
# # Output: No passport
# #
# # Boarding pass? no
# # Passport? no
# # Output: Denied entry
# #
# # Boarding pass? yes
# # Passport? yes
# # Output: Proceed to boarding
# #
# # Boarding pass? no
# # Passport? yes
# # Output: No boarding pass

# # -------------------------------ASSIGNMENT 27th August, 2025-------------------------------
# 1.Print numbers from 1 to 5
# Expected Output:
# 1
# 2
# 3
# 4
# 5
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# 2. Print "Hello" 3 times
# Expected Output:
# Hello
# Hello
# Hello
# i = 1
# while i <= 3:
#     print(f"{i}: Hello")
#     i += 1

# 3.Print only even numbers from 2 to 10 (do not use += 2)
# Expected Output:
# 2
# 4
# 6
# 8
# 10
# i = 1
# while i <= 10:
#     if i % 2 == 0:
#         print(i)
#     i += 1

# 4. Print numbers in reverse from 5 to 1 using a while loop.
# Expected Output:
# 5
# 4
# 3
# 2
# # 1
# i = 5
# while i >= 1:
#     print(i)
#     i -= 1

#  5.	Print numbers from 1 to 10, but skip number 5 - do not use "continue" statement. 
# i = 1
# while i <= 10:
#     if i != 5:
#         print(i)
#     i += 1

# Expected Output:
# 1
# 2
# 3
# 4
# 6
# 7
# 8
# 9
# 10


#  6. 	Print a square of stars
# Ask the user to enter a number
# Example 1:
# Input: 3

# Output:
# ***
# ***
# # ***
# length = int(input("Enter the length of the rectangle: "))
# breadth = int(input("Enter the breadth of the rectangle: "))

# i = 1
# while i <= breadth:
#     print("*" * length)
    # i += 1

# Example 2:
# Input: 5

# Output:
# *****
# *****
# *****
# *****
# *****
#  7.	Print a right triangle of stars
# Ask the user to enter a number
# Example:
# # Input: 4
# n = int(input("Enter a number: "))
# i = 1
# for i in range(1, n + 1):
#     print("*" * i)

# Output:
# *
# **
# ***
# ****


#  8. 	Print a countdown
# Ask the user to enter a number where they want to start the countdown from.
# Ask the user to enter a starting number
# i = int(input("Enter a number to start the countdown: "))
# while i > 0:
#     print(i)
#     i -= 1

# Example:
# Input: 5

# Output:
# 5
# 4
# 3
# 2
# 1
# Go!
#  9. 	Print "1" ten times on the same line using a while loop
# Expected Output:
# 1111111111
# i = 1
# nums = []
# while i < 11:
#     nums.append(str(1))
#     i += 1
# nums = "".join(nums)
# print(nums)

# # 10.  Print a list of the first 12 multiples of 3 starting from 3
# i = 3
# nums = []
# while i <= 36:
#     if i % 3 == 0:
#         nums.append(i)
#     i += 1

# print(nums)
# Write a program that uses a while loop to print numbers from 1 to 10.

# Write a program that takes an integer n from the user and calculates the sum of all 
# natural numbers up to n using a while loop. e. G if n is 5, do 1+2+3+4+5 (15).
# Write a program that generates a random secret number between 1 and 50. Use a while loop to allow 
# the user to guess the number with a maximum of 5 attempts. Provide hints if the guess is too high or too low. E.g. if the secret num is 35, and the user guesses 42, their guess is too high. If they guess lower than 35, their guess is too low.
# Write a program that keeps asking the user for a password until they enter the correct one. The correct password is `secret`.
# Write a program that takes an integer input from the user and uses a while loop to print a countdown from that number to zero.
# Write a program that takes an integer n from the user and uses a while loop to print all even numbers from 1 to n.
# Write a program that takes two integers, base and exponent, from the user and uses a while loop to calculate base raised to the power of exponent.
# Sample Input:
# Enter the base: 2
# Enter the exponent: 3
# Output:
# 2 raised to the power of 3 is 8
# Sample Input:
# Enter the base: 5
# Enter the exponent: 4
# Output:
# 5 raised to the power of 4 is 625


# ----------------------------------------ASSIGNMENT----------------------------------
#1. Write a program that takes an integer input from the user and uses a loop to calculate 
# the sum of its digits. Print the sum.
# digits = input("Enter an integer of at least double digit: ")
# total = 0
# for digit in digits:
#         total += int(digit)

# print(total)

# #  Example:
# # Input: 1234234
# # Output: 10 (1+2+3+4)

# # 2. Collect a string from the user and use loops to count the number of vowels and consonants in the string. Print the counts. Example:
# text = input("Enter a text: ").strip().lower()
# vowels = 0
# consonants = 0
# for char in text:
#     if char.isalpha():
#         if char in "aeiou":
#             vowels += 1
#         else:
#             consonants += 1
    
# # print(f"Vowels: {vowels} , Consonants: {consonants}")
# # Input: "hello world"
# # Output: Vowels: 3, Consonants: 7

# # 3. Write a program that takes an integer input from the user and prints the multiplication table for that number up to 12. Example:
# num = int(input("Enter a number: "))
# for i in range(1, 13):
#     print(f"{num} x {i} = {num * i}")

# # Input: 5
# # Output:
# # 5 x 1 = 5
# # 5 x 2 = 10
# # 5 x 3 = 15
# # ...
# # 5 x 12 = 60

# # # 4. Collect a string from the user and use a loop to reverse the string. Print the reversed string. Do not reverse the string using [::-1] or reversed().
# text = input("Enter a text: ")
# reversed_text = ""
# for i in range(len(text) - 1, -1, -1):
#     reversed_text += text[i]

# print(reversed_text)

# # Example:
# # Input: "python"
# # Output: "nohtyp"

# # 5. Write a program that takes a list of numbers (entered as comma-separated values) from the user and removes any duplicate values. Print the new list. Do not use the set() constructor. Use a loop. 
# numbers = [int(i) for i in input("Enter a list of comma separated values: ").split(",")]
# numbers = int(numbers)
# new_list = []
# for number in numbers:
#     if number in new_list:
#         continue
#     else:
#         new_list.append(number)

# print(new_list)

# Example:
# Input: "1, 2, 3, 2, 4, 3"
# Output: [1, 2, 3, 4]

# #  6.	Write a program that takes an integer input n from the user and prints the first n numbers in the Fibonacci sequence. Example:
# n = int(input("Enter how many Fibonacci numbers you want: "))
# a, b = 0, 1
# for i in range(n):
#     print(a)
#     a, b = b, a + b

# # 	Input: 10
# # 	Output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34
# #  7. 	Collect a list of numbers from the user (entered as comma-separated values) and use a loop to find and print the largest number in the list. Don’t use the built-in max function or anything similar.
# numbers = [int(i) for i in input("Enter a list of comma separated values: ").split(",")]
# largest_num = numbers[0]
# for number in numbers:
#     if number > largest_num:
#         largest_num = number

# print(largest_num)

# # 	Input: "10, 20, 5, 15"
# # 	Output: 20

# #  8. 	Write a program that takes an integer n from the user and calculates the sum of all even numbers from 1 to n. Print the sum.
# n = int(input("Enter any number you want: "))
# total = 0
# for i in range(1, n+1):
#     if i % 2 == 0:
#         total += i

# print(total)

# # 	Input: 10
# # 	Output: 30 (2 + 4 + 6 + 8 + 10)
# #  9. 	Collect a string from the user and use a loop to count the frequency of each character 
# # 	in the string. Print each character along with its frequency. 
# text = input("Enter a string: ")
# counts = {}
# for char in text:
#     if char in counts:
#         counts[char] += 1
#     else:
#         counts[char] = 1

# print(counts)

# # Example:
# # 	Input: "hello"
# # 	Output:
# # h: 1
# # e: 1
# # l: 2
# # o: 1

# #  10.	Write a program that takes an integer n from the user and calculates the sum of 
# # 	squares of all numbers from 1 to n. Print the sum.
# n = int(input("Enter any number you want: "))
# total = 0
# for i in range(1, n+1):
#     total += i ** 2

# print(total)

#  Example:
# 	Input: 3
# 	Output: 14 (1^2 + 2^2 + 3^2)

#  11. 	Collect a phrase from the user and use a loop to generate an acronym by taking the first
	# letter of each word. Print the acronym. 
# phrase = input("Enter a phrase: ").split()
# acronym = ""
# for word in phrase:
#     acronym += word[0].upper()

# print(acronym)
# # Example:
# # 	Input: "Portable Network Graphics"
# # 	Output: "PNG"

# #  12. 	Collect a string from the user and use a loop to count the number of words in the string. 
# # 	Print the count. 
# text = input("Enter a string: ").split()
# counts = 0
# for word in text:
#     counts += 1

# print(counts)

# # Example:
# # 	Input: "Hello world from Python"
# # 	Output: 4

# #  13. 	Collect a string from the user and only print put the words that start with the letter 
# # 	‘S’. 
# sentence = input("Enter a sentence: ").strip().lower()
# words = sentence.split()
# for word in words:
#     if word.startswith("s"):
#         print(word)
# # Example:
# # 	Input: “Print only the words that start with s in this sentence”
# # 	Output: 
# # 	start
# # 	s
# # 	Sentence

# #  14. 	Print all the even numbers from 1 to 20 using the range function and a loop.
# even_nums = []
# for i in range(21):
#     if i % 2 == 0:
#         even_nums.append(i)
# print(even_nums)

# #  15. 	Use a list comprehension to create a list of numbers between 1 and 50 that are divisible
# # 	by 3.
# multiples_of_3 = [i for i in range(1, 51) if i % 3 == 0]

# print(multiples_of_3)

# #  16.	Go through the string below and if the length of a word is even, print that word.
# text = "Print every word in this sentence that has an even number of letters".split()
# even_lettered_word = []
# for word in text:
#     if len(word) % 2 == 0:
#         even_lettered_word.append(word)
# print(even_lettered_word)

# # 	Output: 
# # 	word
# # 	in
# # 	this
# # 	sentence
# # 	that
# # 	an
# # 	even
# # 	number
# # 	of
# #  17. 	Write a program that prints the integers from 1 to 100. But for multiples of three, print 
# # 	“Fizz” instead of the number, and for multiples of five, print “Buzz”. For numbers which 
# # 	are multiples of both three and five, print “FizzBuzz”.
# for i in range(1, 101):
#     if i % 3 == 0 and i % 5 == 0:
#         print("FizzBuzz")
#     elif i % 3 == 0:
#         print("Fizz")
#     elif i % 5 == 0:
#         print("Buzz")
#     else:
#         print(i)

# #  18.	You are given two lists, names and grades. Print them together
# names = ['Ken', 'Mia', 'Rose', 'Henry', 'Suzan']
# grades = ['A', 'E', 'F', 'C', 'B']

# # Expected Output:
# # Ken got grade A
# # Mia got grade E
# # Rose got grade F
# # Henry got grade C
# # Suzan got grade B


# #  19. Print only the items at even indexes
# items = ['shoe', 'stick', 'toy', 'fruit']

# # Expected Output:
# # 0: shoe
# # 2: toy

# #  20.	Given two lists of numbers of the same length, print the indices and values
# #  	of where they differ in a list.
# # list1 = [5, 8, 6, 7, 12, 4]
# # list2 = [5, 3, 6, 9, 12, 0]

# # Expected output:
# # [
# #   'Index 1: 8 != 3',
# #   'Index 3: 7 != 9',
# #   'Index 5: 4 != 0',
# # ]


# # 7. Are all the words made up of only uppercase letters?
# # Input: ["HELLO", "world", "pyTHon", "ROCKS"]
# # Expected Output: False
# greetings = ["HELLO", "world", "pyTHon", "ROCKS"]
# any_word_isupper = any(greeting.isupper() for greeting in greetings)
# print(any_word_isupper)

# # 8. Is there any word that starts with 'z'?
# # Input: ["apple", "zebra", "mango", "lemon"]
# # Expected Output: True
# words = ["apple", "zebra", "mango", "lemon"]
# any_word_begins_with_z = any(word.lower().startswith("z") for word in words)
# print(any_word_begins_with_z)

# # 9. Is there any email address that contains ".org"?
# # Input: ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# # Expected Output: True
# emails = ["alice@gmail.com", "bob@yahoo.com", "team@openai.org"]
# any_mail_with_org = any(".org" in email.lower() for email in emails)
# print(any_mail_with_org)

# # 10. Are all numbers odd?
# # Input: [1, 3, 5, 7, 9]
# # Expected Output: True
# values = [1, 3, 5, 7, 9]
# are_all_nums_odd = all(value % 2 != 0 for value in values)
# print(are_all_nums_odd)

# # 11. Are all words longer than 2 characters?
# # Input: ["hi", "dog", "go", "sun"]
# # Expected Output: False
# words = ["hi", "dog", "go", "sun"]
# are_all_words_2char_long = all(len(word) > 2 for word in words)
# print(are_all_words_2char_long)

# # 12. Create a list of triple the value of each number
# # Input: [2, 4, 6, 8]
# # Expected Output: [6, 12, 18, 24]
# nums = [2, 4, 6, 8]
# triple_of_value = [num * 3 for num in nums]
# print(triple_of_value)

# # 13. Are all temperatures above 0°C?
# # Input: [12, 7, 3, -1, 5]
# # Expected Output: False
# temperatures = [12, 7, 3, -1, 5]
# are_all_temp_above_0 = all(temperature > 0 for temperature in temperatures)
# print(are_all_temp_above_0)

# # 14. Do all words end with a vowel?
# # Input: ["banana", "mango", "kiwi", "grape"]
# # Expected Output: True
# fruits = ["banana", "mango", "kiwi", "grape"]
# all_words_end_with_vowel = all(fruit[-1] in "aeiou" for fruit in fruits)
# print(all_words_end_with_vowel)

# # 15. Create a list of words in lowercase
# # Input: ["HELLO", "WORLD", "PYTHON"]
# # Expected Output: ["hello", "world", "python"]
# greetings = ["HELLO", "WORLD", "PYTHON"]
# new_greetings = [greeting.lower() for greeting in greetings]
# print(new_greetings)

# # 16. Is there any number less than 0?
# # Input: [5, -2, 3, 0, 8]
# # Expected Output: True
# numbers = [5, -2, 3, 0, 8]
# any_nums_less_than_0 = any(number < 0 for number in numbers)
# print(any_nums_less_than_0)

# # 17. Create a list of words that contain the letter 'e'
# # Input: ["sky", "tree", "rock", "stone"]
# # Expected Output: ["tree", "stone"]
# items = ["sky", "tree", "rock", "stone"]
# new_items = [item for item in items if "e" in item.lower()]
# print(new_items)

# # 18. Are all names starting with uppercase letters?
# # Input: ["Alice", "Bob", "charlie", "David"]
# # Expected Output: False
# names = ["Alice", "Bob", "charlie", "David"]
# all_names_start_with_uppercase = all(name[-1].isupper() for name in names)
# print(all_names_start_with_uppercase)

# # 19. Is there any sentence longer than 20 characters?
# # Input: ["Short one", "This is a much longer sentence", "Okay"]
# # Expected Output: True
# sentences = ["Short one", "This is a much longer sentence", "Okay"]
# any_word_longer_than_20chars = any(len(sentences) > 20 for sentences in sentences)
# print(any_word_longer_than_20chars)
# --------------------------------LIST COMPREHENSION & GENERATORS EXERCISES--------------------------------




#1. Write a function sum_numbers(a, b) that returns the sum of two numbers.
# def sum_numbers(a, b):
#     return a + b

# print(sum_numbers(16, 12))

# # # 2. Write a function is_even(n) that returns True if n is even and False if n is odd.
# def is_even(n):
#     return n % 2 == 0

# print(is_even(5))

# # # 3. Write a function is_prime(n) that returns True if n is a prime number and False otherwise.
# def is_prime(n):
#     if n <= 0:
#          return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
    
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(17))

# # # 4. Using the is_prime(n) function from number 3, write a function that asks a user for an input n and returns all the prime numbers up to n.
# n = int(input("Enter any number: "))
# def is_prime(n):
#     if n <= 0:
#          return False
#     if n == 2:
#         return True
#     if n % 2 == 0:
#         return False
    
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# print(is_prime(n))

# # # 5. Write a function lesser_of_two_evens(a, b) that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd.
# def lesser_of_two_evens(a, b):
#         if a % 2 == 0 and b % 2 == 0:
#             return min(a, b)
#         else:
#             return max(a, b)
        
# # print(lesser_of_two_evens(8, 17))

# # # 6. Write a function is_alliteration(two_word_string) that takes a two-word string  and returns True if both words begin with the same letter. is_alliteration(‘Levelheaded llama’) —> True is_alliteration(‘Crazy Kangaroo’) –> False
# # 1. write the function
# # 2. unpack the two word string into another variable by splitting it and also lowercase/uppercase the words to prevent case sensitivity
# # 3. check if the first letters of the already separated words are equal to each other and if they are, it returns true otherwise it returns false
# # 4. Afterwards call the function

# def is_alliteration(two_word_string: str):      
#     words = two_word_string.lower().split()
#     print(words)
#     return words[0][0] == words[1][0]

# # print(is_alliteration("Hello house"))
        
# # # 7. Write a function old_macdonald(name) that capitalizes the first and fourth letters of a name old_macdonald(‘macdonald’) —> MacDonald Note: ‘macdonald’.capitalize() returns Macdonald, not MacDonald.
# def old_macdonald(name):
#     return name[0].upper() + name[1:3] + name[3].upper() + name[4:]

# # print(old_macdonald("macdonald"))

# # 8. Write a function spy_game(list_of_ints) that takes in a list of integers and returns True if it contains 007 in order.spy_game([1, 2, 4, 0, 0, 7, 5]) —> True spy_game([1, 0, 2, 4, 0, 5, 7]) —> True spy_game([1, 7, 2, 0, 4, 5, 0]) —> False
# def spy_game(list_of_ints):
#     spy_code = [0, 0, 7]
#     for i in list_of_ints:
#         if i == spy_code[0]:
#             spy_code.pop(0)
#         if len(spy_code) == 0:
#             return True
#     return False

# # print(spy_game([2,0,3,0,2,7,5]))

# # 9. Write a function vol(radius) that computes the volume of a sphere given its radius.
# import math
# def vol(radius):
#     return (4/3) * math.pi * radius ** 3

# # print(vol(3.5))

# # 10. Write a function range_check(num, low, high) that checks whether a number is in a given range (inclusive of high and low).
# def range_check(num, low, high):
#     return low <= num <= high

# # print(range_check(low= 7, num = 6, high = 9))

# # 11. Write a function upper_lower(text) that accepts a string and calculates the number of uppercase letters and lowercase letters.
# def upper_lower(text):
#     upper_case = 0
#     lower_case = 0
#     for char in text:
#         if char.isupper():
#             upper_case += 1
#         else:
#             lower_case += 1
#     return f"Uppercase: {upper_case}, Lowercase: {lower_case}"

# # print(upper_lower("ArgumeNTATivE"))

# # 12. Write a function unique_list(list_items) that takes in a list and returns a new list with unique elements of the first list. Do not use the set() constructor.
# def unique_list(list_items):
#     new_list = []
#     for item in list_items:
#         if item in new_list:
#             new_list.append(item)
#     return new_list

# # print(unique_list(["eggs", "beef", "chicken", "fish"]))

# #  13.	Write a function multiply(list_items) to multiply all the numbers in a list.	Sample List: [1, 2, 3, -4]	Expected output: -24
# def multiply(list_items):
#     result = 1
#     for num in list_items:
#         result *= num   
#     return result

# print(multiply([1, 2, 3, -4]))

# #  14. 	Write a function is_pangram(text) to check whether a string is a pangram or not. 	Note: A pangram is a word or sentence that contains every letter of the alphabet at	least once. For example: “The quick brown fox jumps over the lazy dog”.	Hint: Import and use the string module.
# import string  
# def is_pangram(text: str):
#     text = text.lower()
#     letters_in_text = set(char for char in text if char.isalpha())
#     return letters_in_text >= set(string.ascii_lowercase)
    
# print(is_pangram("The quick brown fox jumps over the lazy dog")) 

# # Test cases
# # print(is_pangram("Hello world"))  

# #  15. 	Write a function are_anagrams(s1, s2) that checks if two strings are anagrams of each	other. a word, phrase, or name formed by rearranging the letters of another, such as	spar, formed from rasp.
# def are_anagrams(s1, s2):
#     s1 = s1.replace(" ", "").lower()
#     s2 = s2.replace(" ", "").lower()
    
#     if sorted(s1) == sorted(s2):
#         print("They are anagrams")
#     else:
#         print("They are not anagrams")

# are_anagrams("spar", "rasp")     

# # 16. Write a function calculate_bmi(weight, height) that calculates the Body Mass Index 
# # 	(BMI) given weight in kilograms and height in meters.
# def calculate_bmi(weight, height):
#     return weight / (height ** 2)

# print
# #  17. 	Write a function calculate_simple_interest(principal, rate, time) that calculates the 
# # 	simple interest given principal amount, interest rate, and time (in years).
# def calculate_simple_interest(principal, rate, time):
#     return (principal * rate * time) / 100

# print(calculate_simple_interest(5000, 5, 4))



# ====================================ASSIGNMENT===========================================
# 1. Create a function called get_total_length that returns the total number of characters in all the words passed in.
# def get_total_length(*words):
#     total_num_of_chars = 0
#     for word in words:
#         total_num_of_chars += len(word)
#     return total_num_of_chars

# print(get_total_length("apple", "banana", "car"))
# Test Data:
# print(get_total_length("apple", "banana", "car"))
# print(get_total_length("hi", "hello"))

# Expected Output:
# 16
# 7


# 2. Create a function called highest_score that returns the name of the student with the highest score.
# def highest_score(**students_scores: dict):
#     return max(students_scores.keys())
    
# print(highest_score(Ada=72, Bisi=89, Charles=67))

# Test Data:
# print(highest_score(Ada=72, Bisi=89, Charles=67))
# print(highest_score(Emeka=90, Tolu=91, Zainab=88))

# Expected Output:
# Bisi
# Tolu

# 3. Create a function called multiply_first_two that returns the product of the first two numbers passed in.
# def multiply_first_two(*numbers):
#     return numbers[0] * numbers[1]
    
# print(multiply_first_two(3, 5, 9, 2))

# Test Data:
# print(multiply_first_two(3, 5, 9, 2))
# print(multiply_first_two(10, 2, 7))

# Expected Output:
# 15
# 20


# 4. Create a function called describe_books that prints out each book title and its author.
# def describe_books(**books_and_authors: dict[str, str]):
#     for book, author in books_and_authors.items():
#         print(f"{book} is written by {author}.")

# describe_books(Hamlet="Shakespeare", ThingsFallApart="Chinua Achebe", Dune="Frank Herbert")

# Test Data:
# describe_books(Matilda="Roald Dahl", 1984="George Orwell")

# Expected Output:
# Hamlet is written by Shakespeare
# ThingsFallApart is written by Chinua Achebe
# Dune is written by Frank Herbert
# Matilda is written by Roald Dahl
# 1984 is written by George Orwell


# 5. Create a function called total_age that returns the sum of all the ages given.
# def total_age(*ages):
#     result = 1
#     for age in ages:
#         result *= age
#     return result

# print(total_age(12, 30, 18))

# Test Data:
# print(total_age(40, 25))

# Expected Output:
# 60
# 65


# 6. Create a function called list_countries that prints out each country passed in.
# def list_countries(*countries):
#     for country in countries:
#         print(country)

# list_countries("Nigeria", "Ghana", "Kenya")

# Test Data:
# list_countries("Canada", "Mexico")

# Expected Output:
# Nigeria
# Ghana
# Kenya
# Canada
# Mexico

# 7. Create a function called student_details that prints each student’s name and score.
def student_details(**students_name_): 
    pass
# Test Data:
# student_details(Fola=78, Muna=88, Kola=65)
# student_details(Sandra=91, Alex=85)

# Expected Output:
# Fola scored 78
# Muna scored 88
# Kola scored 65
# Sandra scored 91
# Alex scored 85


# 8. Create a function called average_score that returns the average of all scores passed in.

# Test Data:
# print(average_score(50, 60, 70))
# print(average_score(80, 90))

# Expected Output:
# 60.0
# 85.0

# 9. Create a function called total_price that adds up the prices of all items passed as keyword arguments.

# Test Data:
# print(total_price(bread=500, milk=1200, eggs=700))
# print(total_price(book=1500, pen=200))

# Expected Output:
# 2400
# 1700


# 10. Create a function called first_and_last that prints the first and last values passed in.

# Test Data:
# first_and_last(4, 10, 6, 9, 12)
# first_and_last("a", "b", "c", "d")

# Expected Output:
# First: 4, Last: 12
# First: a, Last: d


# 11. Create a function called describe_animals that prints out animal and their sound.

# Test Data:
# describe_animals(cat="meow", dog="bark", cow="moo")
# describe_animals(lion="roar", snake="hiss")

# Expected Output:
# cat makes the sound meow
# dog makes the sound bark
# cow makes the sound moo
# lion makes the sound roar
# snake makes the sound hiss


# 12. Create a function called total_characters that returns how many characters in total exist in all keyword values.

# Test Data:
# print(total_characters(a="banana", b="mango", c="kiwi"))
# print(total_characters(x="hi", y="there"))

# Expected Output:
# 16
# 7


# 13. Create a function called find_minimum that returns the smallest number from all the values passed in.

# Test Data:
# print(find_minimum(99, 45, 12, 88))
# print(find_minimum(8, 3, 7))

# Expected Output:
# 12
# 3


# 14. Create a function called sum_scores_and_bonuses that returns the total of all numbers passed, including keyword values.

# Test Data:
# print(sum_scores_and_bonuses(10, 20, bonus1=5, bonus2=15))
# print(sum_scores_and_bonuses(100, bonus=50))

# Expected Output:
# 50
# 150


# 15. Create a function called longest_word that returns the longest string from all the values passed in (args + kwargs).

# Test Data:
# print(longest_word("cat", "hippopotamus", animal="giraffe", bird="eagle"))
# print(longest_word("short", name="exaggeration", tool="pen"))

# Expected Output:
# hippopotamus
# exaggeration





# ====================================ASSIGNMENT===========================================
# Fill in the Line class methods to accept coordinates as a pair of tuples and 
# return the slope and distance of the line. Look up the formulas for finding the distance and slope of a line.

import math

class Line:
    def __init__(self, coor1, coor2): 
        self.coor1 = coor1
        self.coor2 = coor2

    def distance(self):
        distance = math.sqrt((coordinate2[0] - coordinatel[0]) ** 2 + (coordinate2[1] - coordinatel[1]) ** 2)
        return distance

    def slope(self):
        slope = (coordinate2[1] - coordinatel[1]) / (coordinate2[0] - coordinatel[0])
        return slope

# EXAMPLE EXECUTION

coordinatel = (3,2)
coordinate2 = (8,10)

line_1 = Line(coordinatel, coordinate2)

print(line_1.distance())  # 9.433981132056603
print(line_1.slope())  # 1.6

#  2.	Fill in the class

class Cylinder:
    def __init__(self, height=1, radius=1):
        self.height = height
        self.radius = radius

    def volume (self):
        return round((math.pi * (self.radius ** 2) * self.height), 2)
    
    def surface_area(self):
        surface_area = round((2 * math.pi * self.radius * self.height) + (2 * math.pi * (self.radius ** 2)), 2)
        return surface_area

# EXAMPLE EXECUTION

cylinder = Cylinder(2,3)
print(cylinder.volume())  # 56.52
print(cylinder.surface_area())  # 94.2


# Scenario: You want to create a bank account that supports deposits and withdrawals.

# Task: Create a bank account class that has two attributes:

# owner
# balance

# and two methods:
# deposit
# Withdraw

# Withdrawals may not exceed the available balance.
# Instantiate your class, make several deposits and withdrawals, and test to make sure the account 
# can't be overdrawn.

# You are not expected to use the input function, just pass in values for the amounts into 
# the methods directly, no need for loops either.

# See the next slide for a sample execution of the code you will write.
class Account: 
    def __init__(self, owner: str, balance: float):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"Account name: {self.owner}\nAccount balance:${self.balance}"
    
    def deposit(self, amount: float):
        self.balance += amount
        print("Deposit Accepted")

    def withdraw(self, amount: float):
        if self.balance < amount:
            print("Funds Unavailable")
            return
        else:
            self.balance -= amount
        print("Withdrawal Accepted")  

    

#1. Instantiate the class
acct1 = Account('Winnie', 100)

#2. Print the object
print(acct1)
# Output:
# Account owner: Winnie
# Account balance: $100

#3. Show the account owner attribute
print(acct1.owner)  # Winnie

#4. Show the account balance attribute 
print(acct1.balance)  # 100

#5. Make a series of deposits and withdrawals 
acct1.deposit(50)  # Output: Deposit Accepted

acct1.withdraw(15)  # Output: Withdrawal Accepted

#6. Make a withdrawal that exceeds the available balance 
acct1.withdraw(500)  # Output: Funds Unavailable!

# ===========================
# Assignment Exercises
# ===========================

# Each exercise describes a scenario with classes, objects, and interactions.  
# Your task: implement the classes and methods so that the given sample execution works  
# and produces the expected output.

# -----------------------------------------------------------
# 1. Library & Borrowing

class Book:
    def __init__(self, title: str, author: str, copies: int):
        self.title = title
        self.author = author
        self.copies = copies

    def borrow(self) -> bool:
        if self.copies > 0:
            self.copies -= 1
            return True
        return False


class Library:
    def __init__(self, books: list[Book]):
        self.books = books

    def borrow(self, title: str) -> bool:
        for book in self.books:
            if book.title == title:
                return book.borrow()
        return False  

    def available_books(self) -> dict:
        return {book.title: book.copies for book in self.books}


# --- Example usage ---
book1 = Book("1984", "George Orwell", 5)
book2 = Book("Brave New World", "Aldous Huxley", 2)

library = Library([book1, book2])

print(library.borrow("1984"))            # True
print(library.borrow("Brave New World")) # True
print(library.borrow("Brave New World")) # True
print(library.borrow("Brave New World")) # False

print(library.available_books())         # {'1984': 4, 'Brave New World': 0}


# -----------------------------------------------------------
# 2. Shopping Cart with Discounts
# -----------------------------------------------------------
# cart = ShoppingCart()

# cart.add_item("milk", 500, 2)
# cart.add_item("bread", 1000, 1)

# print(cart.total())
# # -> 2000

# cart.apply_discount(10)   # 10% discount
# print(cart.total())
# # -> 1800


# -----------------------------------------------------------
# 3. Cinema Ticket Booking (with user input)
# -----------------------------------------------------------
# # Assume input:
# # Enter movie name: Interstellar
# # Enter seats to book: 3

# cinema = Cinema({"Interstellar": 5, "Inception": 2})

# movie = input("Enter movie name: ").strip()
# seats = int(input("Enter seats to book: "))

# print(cinema.book(movie, seats))
# # If user entered "Interstellar" and "3"
# # -> True

# print(cinema.show_available())
# # -> {'Interstellar': 2, 'Inception': 2}


# -----------------------------------------------------------
# 4. Student Grades & Average
# -----------------------------------------------------------
# course1 = Course("Math", 80)
# course2 = Course("Physics", 70)
# course3 = Course("English", 90)

# student = Student("Amina", [course1, course2, course3])

# print(student.average())
# # -> 80.0

# print(student.best_course())
# # -> English

# ====================================ASSIGNMENT===========================================


# You are building a simple simulation of a space mission. There are different types of spacecraft.

# 1. Create a base class
# Create a class called Spacecraft with:
# Attributes:
# name (string)
# fuel (integer)

# Methods:
# launch() — prints "Launching {name}!"
# Reduces fuel by 50 units.
# If not enough fuel, print "Not enough fuel to launch."

# refuel(amount) — adds amount to fuel.


# 2. Create subclasses
# CargoShip
# Has an additional attribute: cargo_weight (integer)
# Override launch() — launching consumes extra fuel depending on cargo:
# total fuel reduction = 50 + (cargo_weight * 2)

# PassengerShip
# Has an additional attribute: passenger_count (integer)
# Override launch() — if passenger_count > 100, print "Too many passengers. Cannot launch."
# Otherwise, launch normally (reduce fuel by 50 units)

# 3. Handle negative refuel amounts.


class Spacecraft:
    def __init__(self, name: str, fuel: int):
        self.name = name
        self.fuel = fuel

    def launch(self):
        if self.fuel >= 50:
            self.fuel -= 50
            print(f"Launching {self.name}!")
        else:
            print("Not enough fuel to launch.")

    def refuel(self, amount: int):
        if amount <= 0:
            print("Refuel amount must be positive.")
        else:
            self.fuel += amount
            print(f"{self.name} refueled by {amount}. Current fuel: {self.fuel}")


class CargoShip(Spacecraft):
    def __init__(self, name: str, fuel: int, cargo_weight: int):
        super().__init__(name, fuel)
        self.cargo_weight = cargo_weight

    def launch(self):
        fuel_needed = 50 + (self.cargo_weight * 2)
        if self.fuel >= fuel_needed:
            self.fuel -= fuel_needed
            print(f"Launching {self.name} with cargo! Fuel consumed: {fuel_needed}")
        else:
            print("Not enough fuel to launch with cargo.")


class PassengerShip(Spacecraft):
    def __init__(self, name: str, fuel: int, passenger_count: int):
        super().__init__(name, fuel)
        self.passenger_count = passenger_count

    def launch(self):
        if self.passenger_count > 100:
            print("Too many passengers. Cannot launch.")
        elif self.fuel >= 50:
            self.fuel -= 50
            print(f"Launching {self.name} with passengers!")
        else:
            print("Not enough fuel to launch.")


if __name__ == "__main__":

    c1 = CargoShip("Galactic Hauler", 200, 30)
    c1.launch()

    p1 = PassengerShip("Star Voyager", 120, 80)
    p1.launch()



#1 Define a custom exception called NegativeNumberError.
# Write a function check_positive(number) that raises 
# NegativeNumberError if the input number is negative.
# Catch the exception when calling the function.

# Define custom exception
class NegativeNumberError(Exception):
    """Custom exception raised when a negative number is encountered."""
    pass

def check_positive(number):
    if number < 0:
        raise NegativeNumberError(f"Negative number not allowed: {number}")
    else:
        print(f"{number} is positive.")

try:
    num = int(input("Enter a number: "))
    check_positive(num)
except NegativeNumberError as e:
    print(f"Error: {e}")


# Handle Multiple Exceptions

# Write a function safe_divide(a, b) that performs division.
# Handle ZeroDivisionError if the divisor is zero.
# Handle TypeError if the inputs are not numbers.
# Handle ValueError if the inputs are not convertible to floats.

def safe_divide(a, b):
    try:
        a = float(a)
        b = float(b)
        result = a / b
        return result

    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."
    except TypeError:
        return "Error: Both inputs must be numbers."
    except ValueError:
        return "Error: Inputs must be convertible to numbers."
    
print(safe_divide(10, 2)) 
print(safe_divide(10, 0))      
print(safe_divide("abc", 2)) 
print(safe_divide(10, "xyz")) 
print(safe_divide([1, 2], 5))  








# Scrape (the first page of) quotes from the site and perform some basic text and author-based analysis.
# Use the demo site: http://quotes.toscrape.com/
# Count total number of quotes
# Count the number of unique authors
# Find the author with the most quotes on the page
# Count how many quotes contain the word “is” (case-insensitive)
# List all tags that appear and how many times each appears
