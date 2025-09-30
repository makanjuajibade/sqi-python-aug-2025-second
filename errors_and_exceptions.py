

# try:
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
# except ValueError:
#     print("num1 and num2 must be integers: ")
# else:
#     print(f"The sum of {num1} and {num2} is {num1 + num2}")

# try:
#     num1 = int(input("Enter the value of num1: "))
#     num2 = int(input("Enter the value of num2: "))
#     result = num1 / num2
# except ZeroDivisionError as e:
#     print(f"num2 must not be zero: {e}")
# # except ValueError as e:
# #     print(f"num1 and num2 have to be numbers: {e}")
# except Exception as e:
#     print("Something went wrong", e)
# else:
#     print(f"{num1} divided by {num2} is {result}")
# finally:
#     print("this will always run")


# Ask the user for their age.
# Tell them when they were born.
# If the user enters an age that is not convertible to an integer, 
# then tell them they have to enter an integer and keep asking them till they enter a correct value
# If the user enters an age that is negative, keep asking them till they enter a correct value
# only show thier birth year when the value they entered is correct.
# from datetime import datetime

# current_year = datetime.now().year

# while True:
#     try:
#         age = int(input("Enter your age: "))
#     except ValueError as e:
#         print(f"Age must be a number: {e}")
#     else:
#         if age < 0:
#             print("Age must not be negative")
#         else:
#             print(f"You were born in {current_year - age}")
#             break


# ================================
# Exercise: Divide Numbers Safely
# ================================
#
# Write a program with the following requirements:
#
# 1. Define a function called `safe_divide(a, b)` that:
#    - Takes two numbers as input.
#    - Returns the result of dividing `a` by `b`.
#    - Raises a `ZeroDivisionError` if `b` is zero.
#    - Raises a `TypeError` if either `a` or `b` is not a number.
#

def safe_divide(a: int, b: int):
    try:
        result = int(a) / int(b)
    except ZeroDivisionError as e:
        return f"Cannot divide by zero: {e}"
    except TypeError as e:
        return f"a and b must be integers: {e}"
    except ValueError as e:
        return f"a and b must be integers: {e}"
    else:
        return result
    finally:
        print("This will always run")
    

# 2. In the main part of the program:
#    - Ask the user to enter two values (numerator and denominator).
#    - Use a try/except block to:
#        a) Handle division by zero.
#        b) Handle non-numeric inputs.
#    - Keep asking until the user provides valid numeric input and the division works.
#    - When successful, print the result and exit.
#

numerator = input("Enter the numerator: ")
denominator = input("Enter the denominator: ")

print(safe_divide("4", 5))

# ==========================================
# Sample Input and Output (user interaction)
# ==========================================
#
# Input: 10, 0
# Output: Cannot divide by zero.
#
# Input: ten, 2
# Output: Both inputs must be numbers.
#
# Input: 15, 3
# Output: 15 divided by 3 is 5.0
#
# ==========================================
# Your task:
# - Implement the `safe_divide` function with proper exception handling.
# - Use the function inside a loop until the user gives valid input.



# ================================
# Exercise: Convert Temperature
# ================================
#
# Write a program with the following requirements:
#
# 1. Define a function called `celsius_to_fahrenheit(celsius)` that:
#    - Takes a number as input.
#    - Returns the temperature converted to Fahrenheit. fahrenheit = (celsius * 9/5) + 32
#    - Raises a `ValueError` if the input is not convertible to a number.
#

# def celsius_to_fahrenheit(celsius):
#     return (celsius * 9/5) + 32

# 2. In the main part of the program:
#    - Ask the user to enter a temperature in Celsius.
#    - Use a try/except block to:
#        a) Handle non-numeric inputs.
#    - Keep asking until the user provides valid numeric input.
#    - When successful, print the Fahrenheit equivalent and exit.
#


# while True:
#     try:
#         celsius = float(input("Enter the temperature in celsius: "))
#     except ValueError as e:
#         print("The temperature must be a number", e)
#     else:
#         print(celsius_to_fahrenheit(celsius))
#         break


# ==========================================
# Sample Input and Output (user interaction)
# ==========================================
#
# Input: cold
# Output: Temperature must be a number.
#
# Input: 37
# Output: 37°C is 98.6°F
#
# Input: -40
# Output: -40°C is -40.0°F
#
# ==========================================
# Your task:
# - Implement the `celsius_to_fahrenheit` function with exception handling.
# - Use the function inside a loop until the user gives valid input.




# class InsufficientFundsError(Exception):
#     def __init__(self, message):
#         self.message = message
#         super().__init__(self.message)


# class Account:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self._balance = balance

#     def __str__(self):
#         return f"Account owner: {self.owner}\nAccount balance: ${self._balance:,.2f}"    

#     @property
#     def balance(self):
#         return f"${self._balance:,.2f}"
    
#     @balance.setter
#     def balance(self, new_balance):
#         if new_balance < 0:
#             raise ValueError("New Balance must be positive")
        
#         self._balance = new_balance

#     def deposit(self, amount):
#         self._balance += amount
#         print("Deposit accepted")

#     def withdraw(self, amount):
#         if amount > self._balance:
#             raise InsufficientFundsError("Funds Unavailable")
        
#         self._balance -= amount
#         print("Withdrawal accepted")


# acct1 = Account('Winnie', 100)

# # #2. Print the object
# print(acct1)
# # # Output:
# # # Account owner: Winnie
# # # Account balance: $100.00
# # #3. Show the account owner attribute
# # print(acct1.owner)  # Winnie

# # # #4. Show the account balance attribute 
# print(acct1.balance)  # 100

# # # #5. Make a series of deposits and withdrawals 
# acct1.deposit(50)  # Output: Deposit Accepted

# print(acct1.balance)  # 150
# # acct1.withdraw(15)  # Output: Withdrawal Accepted

# # # #6. Make a withdrawal that exceeds the available balance 
# try:
#     acct1.withdraw(500)  # Output: Funds Unavailable!
# except InsufficientFundsError as e:
#     print(f"Insufficient funds: {e}")


# acct1.balance = -400
# print(acct1.balance)  # 150

