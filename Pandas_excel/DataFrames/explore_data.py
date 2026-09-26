# 6.1 DataFrames - Data Exploration & Quality Report
# Dataset: employee_data.csv
# Author: Jashmin
#
# Goal: load the dataset, look at it, check dtypes/index/selection,
# and note down anything that looks off (missing values, duplicates,
# inconsistent formatting etc.) so it can be cleaned later.

import pandas as pd

df = pd.read_csv("employee_data.csv")

report_lines = []

def log(text=""):
    print(text)
    report_lines.append(text)

log("=" * 55)
log("DATA QUALITY REPORT - employee_data.csv")
log("=" * 55)

# ---- 1. Basic shape ----
log("\n1. Shape of data")
log(f"Rows: {df.shape[0]}, Columns: {df.shape[1]}")

# ---- 2. First look ----
log("\n2. First 5 rows")
log(df.head().to_string())

# ---- 3. Dtypes ----
log("\n3. Column dtypes")
log(df.dtypes.to_string())

# ---- 4. Missing values ----
log("\n4. Missing values per column")
missing = df.isnull().sum()
missing_pct = (missing / len(df) * 100).round(1)
missing_table = pd.DataFrame({"missing_count": missing, "missing_%": missing_pct})
log(missing_table.to_string())

# ---- 5. Duplicate rows ----
log("\n5. Duplicate rows")
dup_count = df.duplicated().sum()
log(f"Full duplicate rows found: {dup_count}")
if dup_count > 0:
    log("Duplicate rows (excluding first occurrence):")
    log(df[df.duplicated()].to_string())

# ---- 6. Numeric column check (Age, Salary) ----
log("\n6. Numeric columns - basic stats")
log(df[["Age", "Salary"]].describe().to_string())

log("\nSuspicious values:")
neg_age = df[df["Age"] < 0]
log(f"- Negative age entries: {len(neg_age)} (Age can't be negative, likely bad data entry)")
high_salary = df[df["Salary"] > 100000]
log(f"- Salary above 1,00,000: {len(high_salary)} row(s) - worth double-checking, could be a typo")

# ---- 7. Categorical column check (City) ----
log("\n7. 'City' column - unique values (before cleaning)")
log(str(sorted(df["City"].dropna().unique())))
log("Notice: same city appears multiple times due to case (Hyderabad vs hyderabad)")
log("and extra spaces (e.g. 'Bangalore '). Needs standardizing (strip + title case).")

# ---- 8. JoinDate format check ----
log("\n8. 'JoinDate' column - sample values")
log(str(df["JoinDate"].dropna().unique()[:6]))
log("Notice: dates are in different formats (YYYY-MM-DD, DD-MM-YYYY, YYYY/MM/DD).")
log("Needs to be converted to one consistent format before analysis.")

# ---- 9. Email column check ----
log("\n9. 'Email' column")
missing_email = df["Email"].isnull().sum()
log(f"Missing emails: {missing_email} out of {len(df)}")

# ---- 10. Summary ----
log("\n" + "=" * 55)
log("SUMMARY OF ISSUES FOUND")
log("=" * 55)
log(f"- {missing.sum()} missing values total, spread across "
    f"{(missing > 0).sum()} column(s)")
log(f"- {dup_count} duplicate row(s)")
log(f"- {len(neg_age)} row(s) with negative age (invalid)")
log(f"- {len(high_salary)} row(s) with unusually high salary (needs check)")
log("- City names not standardized (case + spacing issues)")
log("- JoinDate has 3 different formats mixed together")
log(f"- {missing_email} missing email(s)")

with open("data_quality_report.txt", "w") as f:
    f.write("\n".join(report_lines))

print("\nReport saved to data_quality_report.txt")
