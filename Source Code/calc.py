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
