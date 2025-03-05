#Error Handling in Python
num = int(input("Enter a number: ")) ## If user enters "abc", it crashes!
print("you entered:", num )

#Handling Errors with try-except
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a number.")
#Handling Multiple Errors
# try:
    a = int(input("Enter a number: "))
    b = int(input("Enter another number: "))
    result = a / b
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")
except ValueError:
    print("Error: Please enter numbers only!")

#using finally
try:
    file = open("test.txt", "r")
    content = file.read()
    print(content)
except FileNotFoundError:
    print("Error: File not found!")
finally:
    print("Closing file...") 

#Raising Custom Exceptions
age = int(input("Enter your age: "))

if age < 18:
    raise ValueError("You must be 18 or older to sign up!")

print("Welcome!")


# Homework
#Write a program that asks the user for two numbers and performs division, handling errors like zero division and invalid input.
try:
    # Taking input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Performing division
    result = num1 / num2

    # Printing the result
    print(f"Result: {num1} / {num2} = {result}")

 # Handling division by zero error
except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

# Handling invalid input error (non-numeric values)
except ValueError:
    print("Error: Please enter valid numbers!")

#Create a custom exception that checks if a username is at least 5 characters long.
#Custom Exception Class
class UsernameTooShortError(Exception):
    def __init__(self, message="Username must be at least 5 characters long."):
        self.message = message
        super().__init__(self.message)

# Function to check username length
def check_username(username):
    if len(username) < 5:
        raise UsernameTooShortError  # Raise custom exception
    return "Username is valid!"

# # Taking user input
try:
    user_input = input("Enter a username: ")
    print(check_username(user_input))
except UsernameTooShortError as e:
    print("Error:", e)
    
#Use finally to ensure a message like "Program execution completed." always prints.


# Custom Exception Class
class UsernameTooShortError(Exception):
    def __init__(self, message="Username must be at least 5 characters long."):
        self.message = message
        super().__init__(self.message)

# Function to check username length
def check_username(username):
    if len(username) < 5:
        raise UsernameTooShortError  # Raise custom exception
    return "Username is valid!"

# Taking user input with error handling
try:
    user_input = input("Enter a username: ")
    print(check_username(user_input))
except UsernameTooShortError as e:
    print("Error:", e)
finally:
    print("Program execution completed.")  # Always prints
