# Q24. Create a calculator app using if-else.


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /): ")

if op == "+":
    print("Result:", num1 + num2)

elif op == "-":
    print("Result:", num1 - num2)

elif op == "*":
    print("Result:", num1 * num2)

elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
        
    else:
        print("Error! Division by zero.")
else:
    print("Invalid operator")