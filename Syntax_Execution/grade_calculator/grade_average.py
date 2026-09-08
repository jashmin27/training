"""
Program 10: Average Grade Calculator (multiple subjects)
Concepts used: lists, loops (preview), sum(), len()
"""

num_subjects = int(input("How many subjects? "))
marks_list = []

for i in range(num_subjects):
    marks = float(input(f"Enter marks for subject {i + 1}: "))
    marks_list.append(marks)

average = sum(marks_list) / len(marks_list)
print(f"\nAll marks: {marks_list}")
print(f"Average marks: {average:.2f}")
