"""
validation.py

Validation utilities and failure-handling exercises.

Topics practiced: try/except/else/finally, raising exceptions,
custom exceptions, validation.

Main idea: a validation error (bad input, expected) is different from a
programming defect (a bug, unexpected). We use our own exception class
for validation errors so we can catch just those, and let real bugs show
up as normal Python errors.
"""


# ---------------------------------------------------
# Custom exception
# ---------------------------------------------------

class ValidationError(Exception):
    """Raised when input is invalid. This is an expected kind of error."""
    pass


# ---------------------------------------------------
# Validation functions
# ---------------------------------------------------

def validate_age(age):
    """Age must be a whole number between 0 and 120."""
    if age is None:
        raise ValidationError("age is missing")

    if not isinstance(age, int):
        raise ValidationError("age must be a whole number")

    if age < 0 or age > 120:
        raise ValidationError("age must be between 0 and 120")

    return age


def validate_email(email):
    """Very simple email check: must contain '@' and a '.' after it."""
    if email is None or email == "":
        raise ValidationError("email is missing")

    if "@" not in email:
        raise ValidationError("email must contain @")

    domain_part = email.split("@")[-1]
    if "." not in domain_part:
        raise ValidationError("email domain must contain a dot")

    return email


def validate_username(username):
    """Username must be 3-15 characters, only letters/numbers/underscore."""
    if username is None or username == "":
        raise ValidationError("username is missing")

    if len(username) < 3 or len(username) > 15:
        raise ValidationError("username must be 3-15 characters long")

    for char in username:
        if not (char.isalnum() or char == "_"):
            raise ValidationError("username can only have letters, numbers, and _")

    return username


# ---------------------------------------------------
# Exercise: try / except / else / finally
# ---------------------------------------------------

def check(label, value_function, value):
    """
    Run one validation and print what happened.

    try:     attempt the validation
    except ValidationError: this is an expected problem (bad input)
    except Exception: this is a bug in the program, not bad input
    else:    only runs if nothing went wrong
    finally: always runs, no matter what happened
    """
    print(label)
    try:
        result = value_function(value)
    except ValidationError as error:
        print("  Validation error (expected):", error)
    except Exception as error:
        print("  Program bug (not expected):", error)
    else:
        print("  OK, valid value:", result)
    finally:
        print("  done checking\n")


def main():
    print("--- Age checks ---")
    check("Good age", validate_age, 20)
    check("Missing age", validate_age, None)
    check("Age too big", validate_age, 200)
    check("Age is text, not a number", validate_age, "twenty")

    print("--- Email checks ---")
    check("Good email", validate_email, "student@example.com")
    check("Missing email", validate_email, "")
    check("Email with no @", validate_email, "studentexample.com")

    print("--- Username checks ---")
    check("Good username", validate_username, "student1")
    check("Username too short", validate_username, "ab")
    check("Username with bad symbol", validate_username, "bad name!")

    print("--- Example of a real bug (not a validation error) ---")
    # This is NOT bad input, it is a mistake in how the function is used:
    # we are calling validate_age with no value at all.
    try:
        validate_age()
    except ValidationError as error:
        print("  Validation error (expected):", error)
    except TypeError as error:
        print("  Program bug (not expected):", error)
    finally:
        print("  done checking\n")


if __name__ == "__main__":
    main()
