"""
Program 13: Menu-driven Calculator CLI
Concepts used: while loop, functions, menu pattern
"""

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Error"

while True:
    print("\n--- Calculator Menu ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Exit")
    choice = input("Choose an option: ")

    if choice == "5":
        print("Exiting...")
        break

    if choice in ("1", "2", "3", "4"):
        a = float(input("First number: "))
        b = float(input("Second number: "))
        if choice == "1":
            print("Result:", add(a, b))
        elif choice == "2":
            print("Result:", subtract(a, b))
        elif choice == "3":
            print("Result:", multiply(a, b))
        elif choice == "4":
            print("Result:", divide(a, b))
    else:
        print("Invalid choice.")
