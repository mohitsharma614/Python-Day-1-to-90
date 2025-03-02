#Recursion & Modular
# def countdown(n):
#     if n <= 0:
#         print("Time's Up")
#     else:
#         print(n)
#         countdown(n - 1)

# countdown (5)

#Factorial Using Recursion
# n! = n × (n-1) × (n-2) × ... × 1

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n* factorial (n - 1)
# print(factorial(5))

# Fibonacci Sequence Using Recursion
#F(n) = F(n-1) + F(n-2)

# def fibonacci(n):
#     if n <= 0:
#         return "Invalid Input"
#     elif n == 1:
#         return 0
#     elif n == 2:
#      return 1
#     else:
#      return fibonacci(n - 1) + fibonacci(n - 2)
        

# print(fibonacci(0))

#Example: Using a Built-in Module (math)
# import math

# print (math.sqrt(16))  
# print(math.factorial(5)) 

#Using a Built-in Module (random)

# import random
# print (random.randint(1, 100))

# Homework
#Write a recursive function to calculate the sum of digits of a number
# def number(n):
#     if n == 0:
#         return "Zero"
#     return (n % 10) + number(n // 10)
# num = int(input("Enter a number :"))
# result = number(num)
# print(f"sum of digit of {num} is {result}")

#Use the random module to generate a random password with 8 characters (letters and numbers).
import random
import string

# Create a function to generate a password
def generate_password():
    characters = string.ascii_letters + string.digits  # Letters (A-Z, a-z) + Numbers (0-9)
    password = ''.join(random.choices(characters, k=8))  # Pick 8 random characters
    return password

# Generate and print the password
print("Generated Password:", generate_password())



