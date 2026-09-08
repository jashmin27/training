"""
Program 2: Scientific Calculator
Concepts used: operators (**, %, //), math module import
"""

import math

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nPower ({num1} ^ {num2}): {num1 ** num2}")
print(f"Modulus: {num1 % num2}")
print(f"Floor Division: {num1 // num2}")
print(f"Square root of first number: {math.sqrt(abs(num1))}")
print(f"Log of first number (base 10): {math.log10(num1) if num1 > 0 else 'undefined'}")
