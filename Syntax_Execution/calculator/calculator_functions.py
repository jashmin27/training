"""
Program 3: Calculator using Functions
Concepts used: function definition, parameters, return values
"""

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b if b != 0 else "Error: divide by zero"

# Main execution
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operator = input("Choose operator (+, -, *, /): ")

if operator == "+":
    print("Result:", add(x, y))
elif operator == "-":
    print("Result:", subtract(x, y))
elif operator == "*":
    print("Result:", multiply(x, y))
elif operator == "/":
    print("Result:", divide(x, y))
else:
    print("Invalid operator")
