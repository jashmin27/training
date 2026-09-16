# Validation Exercise

This is a small exercise about exceptions in Python.

## What I practiced
- try / except / else / finally
- raising exceptions on purpose
- making my own exception class
- writing simple validation functions

## Files
- `validation.py` - the code

## What the code does
It checks three kinds of input:
- age (must be a whole number, 0 to 120)
- email (must have an @ and a dot after it)
- username (3 to 15 characters, letters/numbers/underscore only)

If the input is bad, the code raises a `ValidationError`. This is my own
exception class, made by inheriting from `Exception`.

## Expected error vs bug
The important idea in this exercise is telling apart two different
things:

1. A **validation error** - this is expected. It just means the user
   typed something wrong, like an age of 200 or an email with no @.
   We catch `ValidationError` for this.

2. A **bug** - this is not expected. It means there is a mistake in the
   code itself, like calling a function without giving it the value it
   needs. We catch this separately with `except Exception` (or
   `TypeError` in the last example) so it is not confused with bad
   input.

The `check()` function shows this using try/except/else/finally:
- `try` - run the validation
- `except ValidationError` - print that the input was invalid (expected)
- `except Exception` - print that something unexpected broke (a bug)
- `else` - runs only if the value was valid
- `finally` - always runs, prints that the check is done

## How to run it
```
python validation.py
```

It will print a list of checks, showing which ones passed, which ones
failed validation, and which one was an actual bug.
