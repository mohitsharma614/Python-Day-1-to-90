# Defining and Calling a Function
def greet():
    print("Hello, Welcome To Jammu!")
   
   
greet()

# Functions with Parameters
def greet(name):
    print("Hello, " +name + "!") 
greet("Mohit")

# Function to Add Two Numbers
def add_number(a , b):
    sum = a + b
    print(f"sum: {sum}")  #f-string
    # or 
    print("sum:", sum)
add_number(5 , 10)

#Functions with Return Values
def square (num):
    return num * num
result = square(4)
print(f"square: {result}")

#Function to Find the Maximum of Three Numbers
def find_max(a, b, c):
    return max(a, b, c)
print("MAX:", find_max(10, 25, 15))
 
 #Default Parameters in Functions
def greet(name= "Guest"):
    print("hello," + name + "!")
greet()
greet("Amit")

# Lambda Functions (One-Line Functions)

square = lambda x: x * x
print(square(5))    

#Example: Sum of Two Numbers
add = lambda a, b: a + b
print(add(10, 20))

# Homework

# Write a function that takes a number as input and returns whether it is even or odd.
def check_even_odd(num):
    if num % 2 == 0:
        return "even"
    else:
        return "Odd"
number = int(input("Enter a number: "))
result = check_even_odd(number)
print(f"The number {number} is {result}.")

# Create a function that takes a list of numbers and returns the sum of all elements.

def sum_of_list(number):
    return sum(number)
nums = [1, 2, 3, 4, 5]
result = sum_of_list(nums)
print(f"sum of the list: {result}")

# Write a function that calculates the factorial of a number.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


num = int(input("Enter a number: "))
result = factorial(num)
print(f"Factorial of {num} is {result}")

# Use a lambda function to find the square of a number.
square = lambda x: x * x
print(square(12))

# or
# use a lambda function to find the square of a number from user input
square = lambda num: num * num
num = int(input("Enter a number: "))
print(f"Square of {num} is {square(num)}")
 


        
