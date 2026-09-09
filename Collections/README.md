# Collections Practice

Simple python programs made to practice collections (list, tuple, set, dict) in python.

## Files

- **inventory.py** - inventory management, add/sell/remove items, total value, low stock items
- **employee_directory.py** - employee directory, group by dept, sort by salary, avg salary per dept
- **transactions.py** - transaction data, total by category and by customer, high value transactions

## Concepts covered

- list, tuple, set, dict
- indexing and slicing
- nested dict/list structures
- mutation vs copy (shallow copy problem)
- basic aggregation using loops (no fancy built-ins)

## How to run

```
python3 inventory.py
python3 employee_directory.py
python3 transactions.py
```

Sample data is already written inside each file so no input needed, just run and check the output.

## Note

Each file also has a small demo at the end showing copy vs mutation - how editing a "copy" of a list/dict can still change the original one if the copy is shallow.
