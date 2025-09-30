# import datetime
# from datetime import datetime
# current_year = datetime.now().year

# while True:
#     try:
#         age = int(input("Enter your age: "))
#     except ValueError:
#         print("Age must be an integer")
#         age = int(input("Enter your age: "))
        
#     else:
#         if age < 0:
#             print("Enter a correct value: ")
#             age = int(input("Enter your age: "))
#         else:
#             d_o_b = current_year - age
#             print(f"Your year of birth is {d_o_b}")
#             break
    
def celsius_to_fahrenheit(celsius: float):
    return (celsius * 9/5) + 32

while True:
    try:
        celsius = float(input("Enter the degree in celsius: "))
    except ValueError:
        print("You must enter a number")
    else: 
        print(celsius_to_fahrenheit(celsius)) 
    break