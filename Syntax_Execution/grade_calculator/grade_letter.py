"""
Program 12: Grade Calculator using a Function with Cutoffs
Concepts used: functions, list of tuples, clean lookup logic
"""

def get_letter_grade(marks):
    cutoffs = [(90, "A+"), (75, "A"), (60, "B"), (40, "C"), (0, "F")]
    for cutoff, letter in cutoffs:
        if marks >= cutoff:
            return letter
    return "Invalid"

marks = float(input("Enter marks: "))
print(f"Grade: {get_letter_grade(marks)}")
