"""
clean_data.py

Simple script to clean up the messy orders dataset (messy_orders.csv).
Steps: handle missing values, remove duplicates, fix data types,
normalize text/date formats, and do some basic validation.

Run: python3 clean_data.py
Output: cleaned_orders.csv
"""

import pandas as pd
import numpy as np

INPUT_FILE = "messy_orders.csv"
OUTPUT_FILE = "cleaned_orders.csv"

df = pd.read_csv(INPUT_FILE)
print(f"Loaded {len(df)} rows")

# --- 2. Clean up text columns (strip spaces, fix casing) ---
df["customer_name"] = df["customer_name"].str.strip()
df["customer_name"] = df["customer_name"].str.title()

df["city"] = df["city"].str.strip().str.title()

df["status"] = df["status"].str.strip().str.title()

# --- 3. Fill missing customer_name using email where possible ---
# if name is missing, try to guess from email (before the @)
missing_name = df["customer_name"].isna()
df.loc[missing_name, "customer_name"] = (
    df.loc[missing_name, "email"].str.split("@").str[0].str.replace(".", " ").str.title()
)

# --- 4. Normalize signup_date to a single format (YYYY-MM-DD) ---
# dates in the raw file show up in 3 different formats, so we try
# a few parsers instead of assuming one
def parse_date(value):
    if pd.isna(value) or str(value).strip() == "":
        return pd.NaT
    for fmt in ("%Y-%m-%d", "%d/%m/%Y", "%m-%d-%Y", "%Y/%m/%d"):
        try:
            return pd.to_datetime(value, format=fmt)
        except (ValueError, TypeError):
            continue
    # last resort, let pandas guess
    return pd.to_datetime(value, errors="coerce")

df["signup_date"] = df["signup_date"].apply(parse_date)
missing_dates = df["signup_date"].isna().sum()
print(f"{missing_dates} rows had a missing/unreadable signup_date (left blank, not guessed)")

# --- 5. Fix amount column ---
# amount should be numeric. Negative amounts don't make sense for an
# order total, so those are treated as data entry errors and dropped.
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
neg_amounts = (df["amount"] < 0).sum()
df.loc[df["amount"] < 0, "amount"] = np.nan
print(f"{neg_amounts} negative amount(s) found and set to missing (assumed typo)")

# fill missing amount with the median amount (simple, avoids skew from outliers)
median_amount = df["amount"].median()
df["amount"] = df["amount"].fillna(round(median_amount, 2))

# --- 6. Fix quantity column ---
# "two" instead of 2, NaN as text, actual NaN, etc.
word_to_num = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
def fix_quantity(value):
    if pd.isna(value):
        return np.nan
    value = str(value).strip().lower()
    if value in word_to_num:
        return word_to_num[value]
    if value == "nan":
        return np.nan
    try:
        return int(float(value))
    except ValueError:
        return np.nan

df["quantity"] = df["quantity"].apply(fix_quantity)
# assume missing quantity means 1 item (most common case for this kind of order)
df["quantity"] = df["quantity"].fillna(1).astype(int)

# --- 7. Basic email validation (just flag, don't drop) ---
df["email_valid"] = df["email"].str.match(r"^[^@]+@[^@]+\.[^@]+$", na=False)
invalid_emails = (~df["email_valid"]).sum()
print(f"{invalid_emails} row(s) have a suspicious/incomplete email (flagged, not removed)")

# --- 8. Remove duplicate orders ---
# same customer, same email, same amount, same date = looks like the
# same order got entered twice under a different order_id. Keeping the
# first one and dropping the rest.
before = len(df)
df = df.drop_duplicates(subset=["customer_name", "email", "signup_date", "amount", "quantity"])
print(f"Removed {before - len(df)} duplicate order(s) (same customer/email/amount/date)")

# --- 9. Final formatting ---
df["signup_date"] = df["signup_date"].dt.strftime("%Y-%m-%d")
df = df.sort_values("order_id").reset_index(drop=True)

df.to_csv(OUTPUT_FILE, index=False)
print(f"Saved cleaned data to {OUTPUT_FILE} ({len(df)} rows)")
