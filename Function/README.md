# Functions Practice

Refactored the inventory, employee directory and transaction exercises into one reusable utility library, using proper functions this time.

## File

- **utility_lib.py** - all the functions in one place

## Concepts covered

- parameters and return values
- default parameters (like `threshold=20`, `label="Summary"`)
- keyword arguments (`dept="IT"`, `show_count=True`)
- `*args` - `total_of()` function takes any number of values
- `**kwargs` - `make_record()` function takes any number of named fields
- scope - global vs local variable demo at the bottom
- pure functions - inventory functions dont change the original dict, they return a new one instead

## How to run

```
python3 utility_lib.py
```

It has a demo at the bottom (`if __name__ == "__main__":`) which calls all the functions with sample data and prints the output.

## Note

Earlier the inventory/employee/transaction files were changing data directly (like `inventory[name]["qty"] += qty`). Here most functions take the data as input and return a new result instead of touching the original one directly, so there are less side effects.
