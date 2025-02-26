# loop
print("Hello, World!")
print("Hello, World!")
print("Hello, World!")

#for loop
for i in range(3):
    print("Hello, World!")
    
for i in range(1,6):
    print(i)
    
# Looping Through a List
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    
# Looping Through a String (Character by Character)
for letter in "Python":
    print(letter) 
The range(start, stop, step) function generates numbers.
for i in range(2, 11, 4):
    print(i)
    
#while Loop
i = 1
while i<= 5:
    print(i)
    i += 1

 # example
 
password = ""
while password != "Python123":
    password = input("Enter Password:")
    print("Access Granted!")

#homework
# Write a program that prints numbers from 1 to 50, but skips multiples of 5 using continue.

for num in range(1, 50):
    if num % 5 == 0:
        continue  
    print(num)

#Write a program to find the sum of all even numbers from 1 to 100 using a loop.
for num in range (1, 100):
    if num % 2 == 0:
        print(num)
        
#Create a program that generates the multiplication table of a given number using a loop.
num = int(input("Enter a number:"))
for i in range(1, 11):
    print(num, "x", i, "=", num * i)

# print the pattern
for i in range(1, 6):
    print("* " * i)
    
