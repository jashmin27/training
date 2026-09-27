"""
Just makes a sample employee_data.xlsx with a few rows that are broken on purpose,
so I have something to actually test the validator against.
"""

from openpyxl import Workbook

wb = Workbook()
ws = wb.active
ws.title = "Employees"

ws.append(["EmployeeID", "Name", "Age", "Salary", "Email"])

rows = [
    ("E001", "Ravi Kumar", 28, 45000, "ravi.kumar@example.com"),
    ("E002", "Sneha Reddy", 34, 52000, "sneha.reddy@example.com"),
    ("E003", "", 30, 48000, "noemail@example.com"),          # missing name
    ("E004", "Arjun Rao", 17, 30000, "arjun.rao@example.com"),  # age below allowed range
    ("E002", "Priya Das", 29, 41000, "priya.das@example.com"),  # duplicate EmployeeID (E002 again)
    ("E006", "Kiran Shah", 45, -5000, "kiran.shah@example.com"),  # negative salary
    ("E007", "Meera Iyer", 31, None, "meera.iyer@example.com"),  # missing salary
    ("E008", "Farhan Ali", 70, 60000, "farhan.ali@example.com"),  # age above allowed range
]

for r in rows:
    ws.append(r)

wb.save("employee_data.xlsx")
print("sample file created")
