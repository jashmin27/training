
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2
division = num1 / num2 if num2 != 0 else "Undefined (division by zero)"

print(f"\nSum: {addition}")
print(f"Difference: {subtraction}")
print(f"Product: {multiplication}")
print(f"Quotient: {division}")
