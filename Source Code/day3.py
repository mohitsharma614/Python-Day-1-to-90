# operators
# 1. Arithmetic Operators
x = 10
y = 5
print(x + y) #Addition
print(x - y) #Subtraction
print(x * y) #Multiplication
print(x / y) #division
print(x // y) #foot division
print(x % y)  #modulus
print(x ** y) #Exponentiation

# 2.Comparision Operators

print(x == y) #Equal to
print(x != y) #not equal to
print(x > y)  #Grater than
print(x < y)  #less than
print(x >= y) #grater than or equal to
print(x <= y) #less than or equal to

# Logical Operators
print(x >5 and y< 10)  #And operator(Returns True if both conditions are true)
print(x > 5 or y > 10) #Or operator(Returns True if atleast one condition is true)
print (not x > 5)  #Not operator(Reverses the condition)

#Assignment Operators
x = 10
x += 5 #i.e x = x+5
x -= 5
print(x)

# #5. Identity and Membership Operators
a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)
print(b)
print(a is c)
print( a == c)
#example
number = [10, 20, 30, 40]
print(20 in number)
print(50 not in number)

#Homework
 #Write a program that asks the user to enter two numbers and performs all arithmetic operations on them.
number1 = float(input("Enter first number:")) 
operators = input("Enter operator(+, - ,*, /, % ,//, **):")
number2 = float(input("Enter second number"))
if operators == "+":
    print("Result:", number1 + number2)
elif operators == "-":
    print("Result:", number1 - number2)
elif operators == "*":
     print("Result:", number1 * number2) 
elif operators == "%":
    print("Result:", number1 % number2) 
elif operators == "//":  
    print("Result:", number1 // number2) 
elif operators == "**":  
    print("Result:", number1 ** number2) 
elif operators == "/":
    if number2 == 0:
        print("Error! Division by Zero")
    else:
        print("Result:", number1 / number2)  
else:
    print("Invalid operator used")  

#Write a program to check if a user’s age qualifies them as an adult (18+) using logical operators.
age = float(input("Enter your Current Age:"))
if age >= 18:
 print(" users age qualifies them as an adult (18+)")
else:
    print("User are Under age")
    
#Use the modulus operator (%) to check if a number is even or odd.
num = int(input("Enter a number:"))
if num % 2 == 0:
    print(f"{num} is a Even number")
else:
    print(f"{num} is an odd number")