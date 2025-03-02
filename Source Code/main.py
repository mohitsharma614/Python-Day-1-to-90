# import mymodule
# print(mymodule.greet("Mohit"))

import mymodule 

# Taking user input
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Using functions from the module
print(f"Addition: {mymodule.add(num1, num2)}")
print(f"Subtraction: {mymodule.subtract(num1, num2)}")
print(f"Multiplication: {mymodule.multiply(num1, num2)}")