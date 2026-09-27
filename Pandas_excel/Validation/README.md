# Excel Validation Utility

A small script that checks an Excel sheet for the usual data-entry problems: missing
required fields, values outside a sensible range, and duplicate IDs. Wrote it to be
reusable - the rules live in one config block at the top, so it's not tied to one
specific spreadsheet.

## Files here

- `excel_validator.py` - the actual utility
- `make_sample_data.py` - generates `employee_data.xlsx`, a test file with some rows
  broken on purpose so there's something real to run the validator against
- `employee_data.xlsx` - the sample (messy) data
- `validation_report.txt` - what the validator prints when you run it on that file

## What it checks

1. **Required columns aren't blank** - e.g. every row needs a Name, can't be empty
2. **Values are inside an allowed range** - e.g. Age has to be 18-65, Salary can't be negative
3. **A key column has no duplicates** - e.g. EmployeeID has to be unique per row

## How to use it

Open `excel_validator.py` and edit the config block near the top:

```python
SHEET_NAME = "Employees"
REQUIRED_COLUMNS = ["EmployeeID", "Name", "Age", "Salary"]
RANGES = {
    "Age": (18, 65),
    "Salary": (0, None),   # None means no upper limit
}
UNIQUE_COLUMN = "EmployeeID"
```

Change those to match your own sheet's column names and rules, then run:

```
python excel_validator.py your_file.xlsx
```

It prints every problem it finds, with the exact row number and what's wrong with it,
and also saves the same thing to `validation_report.txt`. If nothing's wrong, it just
says "No problems found."

You can also import `validate_sheet()` into another script if you want to run checks
as part of a bigger pipeline instead of from the command line.

## Test run

Ran it against the sample file (which has 6 problems planted in it on purpose) and it
caught all of them - a blank name, an age too low, an age too high, a negative salary, a
missing salary, and a duplicate employee ID. See `validation_report.txt` for the exact
output.
