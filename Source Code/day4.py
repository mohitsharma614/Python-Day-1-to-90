#Conditional Statement
#if,if-else Condition
age = int(input("Enter your currnet age:"))

if age >= 18:                      
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")  
    
#if,else elif

marks = int(input("Enter your Marks:"))
if marks > 90:
    print("Grade: A")
elif marks > 80:
    print("Grade: B")
elif marks > 70:
    print("Grade: C")
elif marks > 60:
    print("Grade: D")
else:
    print("Grade: F, Improve your grade otherwise i call your parents ")

#nested if statement
num = int(input("Enter a number:"))
if num > 0:
    print("positive number")
    if num % 2 == 0:
        print("Even number")
        
    else:
        print("odd number")
else:
    print("Negative number")
    
#logical opeeration conditions
age = int(input("Enter your age:"))
income = int(input("Enter yoour monthly income:"))

if age > 18 and income >= 20000:
    print("You are eligible for a credit card.")
else:
    print("You are not eligible for a credit card.")

# Homework
#Write a program that asks the user for a number and prints "Even" or "Odd".
num = int(input("Enter a number:"))
if num % 2 == 0:
     print("Even number")
else:
    print("Odd number")
    
#  Create a program that asks for a password. If the password is "Python123", print "Access Granted", otherwise print "Access Denied"

password = input("Enter Password:")
if password == "Python123":
    print("Access Granted")
else:
    print("Access Denied")
#  Write a program that checks whether a year is a leap year or not. (Hint: A leap year is divisible by 4 but not 100, except when divisible by 400)

year = int(input("Enter a year:"))

if(year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year")