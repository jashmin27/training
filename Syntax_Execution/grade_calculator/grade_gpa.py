
subjects = ["Math", "Physics", "Programming"]
grade_points = [9, 8, 10]      # out of 10
credits = [4, 3, 3]             # credit hours

total_points = sum(gp * c for gp, c in zip(grade_points, credits))
total_credits = sum(credits)
gpa = total_points / total_credits

for subject, gp, c in zip(subjects, grade_points, credits):
    print(f"{subject}: {gp}/10 (credits: {c})")

print(f"\nGPA: {gpa:.2f}")
