

marks = float(input("Enter marks obtained (out of 100): "))

if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 40:
    grade = "C"
else:
    grade = "F"

print(f"Marks: {marks} -> Grade: {grade}")
