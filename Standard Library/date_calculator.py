"""
date_calculator.py

A simple date calculator using the datetime module from the
standard library. No extra packages needed.
"""

from datetime import datetime, timedelta


DATE_FORMAT = "%Y-%m-%d"


def days_between(date1_str, date2_str):
    """Return how many days are between two dates (as text, YYYY-MM-DD)."""
    date1 = datetime.strptime(date1_str, DATE_FORMAT)
    date2 = datetime.strptime(date2_str, DATE_FORMAT)
    difference = date2 - date1
    return difference.days


def add_days(date_str, days):
    """Add a number of days to a date and return the new date as text."""
    start_date = datetime.strptime(date_str, DATE_FORMAT)
    new_date = start_date + timedelta(days=days)
    return new_date.strftime(DATE_FORMAT)


def day_of_week(date_str):
    """Return the name of the weekday for a given date."""
    date = datetime.strptime(date_str, DATE_FORMAT)
    return date.strftime("%A")


def age_in_years(birthdate_str):
    """Work out someone's age in years from their birthdate until today."""
    birthdate = datetime.strptime(birthdate_str, DATE_FORMAT)
    today = datetime.today()

    age = today.year - birthdate.year

    # if birthday has not happened yet this year, subtract 1
    had_birthday_this_year = (today.month, today.day) >= (birthdate.month, birthdate.day)
    if not had_birthday_this_year:
        age = age - 1

    return age


def main():
    print("Days between 2026-01-01 and 2026-09-14:")
    print(days_between("2026-01-01", "2026-09-14"))
    print()

    print("10 days after 2026-09-14:")
    print(add_days("2026-09-14", 10))
    print()

    print("Day of the week for 2026-09-14:")
    print(day_of_week("2026-09-14"))
    print()

    print("Age of someone born on 2000-05-20:")
    print(age_in_years("2000-05-20"))


if __name__ == "__main__":
    main()
