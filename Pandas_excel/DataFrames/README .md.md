# Task 6.1 - DataFrames (Data Quality Report)

## What this is
Small task to practice loading a CSV into pandas and checking it for basic
data quality issues before doing any real analysis on it.

## Files
- `employee_data.csv` - sample employee dataset (made up data, 32 rows)
- `explore_data.py` - script that loads the CSV and checks it
- `data_quality_report.txt` - output of the script, saved as a text report

## What I did
1. Loaded the CSV using `pd.read_csv()`
2. Checked shape, `.head()`, and `.dtypes`
3. Checked missing values with `.isnull().sum()`
4. Checked for duplicate rows with `.duplicated()`
5. Ran `.describe()` on Age and Salary to catch weird values (like negative age)
6. Looked at the City column and noticed the same city was written in different
   ways (Hyderabad / hyderabad / "Bangalore " with a space)
7. Looked at JoinDate and noticed the dates are not in one consistent format
8. Wrote all of the above into a summary at the end

## Issues found in the data
- Missing values in Age, Salary, JoinDate and Email columns
- 2 duplicate rows
- Some Age values are negative, which isn't possible
- A couple of Salary values look too high, might be a data entry mistake
- City names aren't standardized (case + extra spaces)
- JoinDate has 3 different date formats mixed in the same column

## Note
This was just the exploration/reporting step, so I haven't cleaned or fixed
the data yet (no dropping duplicates, no filling missing values). That would
be the next step once this report is reviewed.

## How to run
```
python3 explore_data.py
```
This prints the report to the console and also saves it to
`data_quality_report.txt`.
