"""
Program 4: Calculator using a Dictionary of Operations
Concepts used: dictionaries, functions as values, lambda expressions
"""

# Map each symbol to a function (lambda = small anonymous function)
operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b if b != 0 else "Error: divide by zero",
}

x = float(input("Enter first number: "))
op = input(f"Choose operator {list(operations.keys())}: ")
y = float(input("Enter second number: "))

if op in operations:
    print("Result:", operations[op](x, y))
else:
    print("Invalid operator")
