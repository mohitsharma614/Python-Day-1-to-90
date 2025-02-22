# name = "Mohit"
# age = 25
# height = 5.9
# is_student  = True
# print(name)
# print(age)
# print(height)
# print(is_student)
# #type
# print(type(name))
# print(type(height))
# print(type(age))
# print(type(is_student))
#input
#name = input("Enter your name:")
#print("hello, " + name + "!")#The + operator joins (concatenates) these strings together.
#print(f"hello, {name}!") #Instead of using +, we f-strings which are more readable:

# Example: Taking Numeric Input
# By default, input() returns a string. Convert it to an integer (int) or float (float):

# age = int(input("Enter your age:"))
# height = float(input("Enter your height:"))
 
# print(f"your age is, {age}")
# print(f"your height is, {height} cm")

#Type Conversion (Casting)
# num_str = "100"
# num_int = int(num_str)
# num_float = float(num_int)
# print(num_int)
# print(num_float)
# 🔍 Homework:
# 1️ Write a program that asks the user for their name, age, and city and prints a sentence like:
# "Hello, I am Mohit. I am 25 years old and I live in Delhi."
# name = input("Enter your name:")
# age = int(input("enter your age:"))
# city = input("Enter your City:")
# print(f"hello, I am {name}. I am {age} years old and I live in {city}.")
# 2️ Convert a user’s input from kilograms to grams (kg * 1000).
# kg = float(input("Enter the weight in Kg:"))
# gram = kg * 1000
# print(f"{kg} kg is equal to {gram} gram.")
# 3️ Try using type conversion (int(), float(), str()) in different ways.
num_str = "100"
num_int = int(num_str)
num_float = float(num_int)

print(num_int)
print(num_float)
print(num_str)