# Standard Library Exercise

This is a small exercise about the Python standard library.

## What I practiced
- datetime
- pathlib
- json
- csv
- collections (Counter, defaultdict)
- itertools (groupby)
- re (basic regex)

## Files
- `date_calculator.py` - works with dates
- `json_transformer.py` - reads and changes JSON data
- `log_processor.py` - reads a log file and makes a report

Each file also makes its own sample data when you run it, so nothing
needs to be set up first.

## date_calculator.py
Uses `datetime` to:
- find how many days are between two dates
- add days to a date
- find the day of the week for a date
- work out someone's age from their birthdate

## json_transformer.py
Uses `json`, `pathlib`, and `collections.defaultdict` to:
- make a sample `people.json` file
- read it back in
- group the people by city
- save the grouped result to `people_by_city.json`

## log_processor.py
Uses `re`, `collections.Counter`, `itertools.groupby`, and `csv` to:
- make a sample `sample.log` file
- read the log file (and check it exists first, using `pathlib`)
- use `re` to pull out the date, level, and message from each line
- count how many lines are INFO / WARNING / ERROR using `Counter`
- find streaks of the same level in a row using `itertools.groupby`
- save the level counts to `level_counts.csv`

## Why standard library
All three tools are built using only modules that come with Python.
No extra packages needed to be installed for any of this.

## How to run it
```
python date_calculator.py
python json_transformer.py
python log_processor.py
```
