"""
Program 16: Combined Dashboard Menu
Concepts used: nested menus, function composition, imports (modular design)
"""

def grade_from_marks(marks):
    if marks >= 90: return "A+"
    if marks >= 75: return "A"
    if marks >= 60: return "B"
    if marks >= 40: return "C"
    return "F"

def km_to_miles(km):
    return km * 0.621371

while True:
    print("\n=== Student Dashboard ===")
    print("1. Grade Calculator\n2. Distance Converter\n3. Exit")
    choice = input("Choose an option: ")

    if choice == "1":
        marks = float(input("Enter marks: "))
        print(f"Grade: {grade_from_marks(marks)}")
    elif choice == "2":
        km = float(input("Enter distance in km: "))
        print(f"{km} km = {km_to_miles(km):.2f} miles")
    elif choice == "3":
        print("Session ended.")
        break
    else:
        print("Invalid choice.")
