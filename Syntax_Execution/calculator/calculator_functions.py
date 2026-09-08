x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

operator = input("Choose operator (+, -, *, /): ")

if operator == "+":
    print("Result:", x + y)

elif operator == "-":
    print("Result:", x - y)

elif operator == "*":
    print("Result:", x * y)

elif operator == "/":
    if y != 0:
        print("Result:", x / y)
    else:
        print("Cannot divide by zero")

else:
    print("Invalid operator")
