"""
Program 1: Basic Calculator
Concepts used: variables, input/output, type conversion, operators
"""

# Take two numbers from the user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# Perform all basic operations using arithmetic operators
addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

# Display results
print(f"\nSum: {addition}")
print(f"Difference: {subtraction}")
print(f"Product: {multiplication}")
print(f"Quotient: {division}")
