# Data Cleaning Task - Orders Dataset

## What this is
`messy_orders.csv` is a small sample orders dataset with the kind of
issues you usually run into with real data - missing values, duplicate
rows, mixed date formats, inconsistent text casing, and a couple of
bad values. `clean_data.py` cleans it up and saves the result as
`cleaned_orders.csv`.

## How to run it
```
python3 clean_data.py
```
Needs pandas and numpy installed. It reads `messy_orders.csv` from the
same folder and writes `cleaned_orders.csv`.

## Issues found in the raw data
- Duplicate orders (same customer, email, amount, date but different
  order_id) - looked like the same order got submitted twice
- Missing values in `customer_name`, `signup_date`, `amount`, `quantity`
- `signup_date` written in 3 different formats (`2023-01-15`,
  `15/01/2023`, `03-12-2023`)
- Inconsistent casing in `customer_name`, `city`, `status` (e.g.
  "priya sharma", "DELIVERED", "delivered")
- Extra whitespace in some fields (e.g. `"Hyderabad "`)
- `quantity` had a value written as the word "two" instead of 2
- One `amount` was negative, which doesn't make sense for an order total
- One email was incomplete (`karan.singh@`)

## Assumptions made (since I couldn't go ask the "customer")
- **Duplicates**: if customer name, email, amount, date and quantity
  all match, I treated it as the same order entered twice and kept
  only the first one.
- **Missing customer_name**: guessed from the part of the email before
  the `@` (e.g. `anita.das@gmail.com` -> "Anita Das"). Not perfect, but
  better than leaving it blank.
- **Missing signup_date**: left as blank rather than guessing a date,
  since there's no reliable way to infer it.
- **Negative amount**: assumed this was a typo (extra minus sign) and
  treated it as missing rather than trying to "fix" the number, then
  filled it in with the median amount along with the other missing
  amounts. Using the median instead of average so one large/small order
  doesn't skew things.
- **Missing quantity**: assumed 1 item, since that's the most common
  order size in this data.
- **"two" as quantity**: converted written-out numbers (one-five) to
  digits.
- **Bad email (`karan.singh@`)**: kept the row but added an
  `email_valid` column set to False, instead of deleting the row -
  didn't want to throw away a whole order just because of one bad
  field.
- **Text formatting**: trimmed extra spaces and standardized casing
  (Title Case for names/cities, Title Case for status) so grouping/
  filtering later actually works properly.

## Output
`cleaned_orders.csv` - same columns as the original, plus one extra
column `email_valid` (True/False) so anyone using this data downstream
knows which emails might need a manual check.

## Notes / what I'd do differently with more time
- Right now missing amounts are filled with the median for the whole
  dataset. With more data I'd probably fill it per city or per status
  instead, since order sizes likely differ by city.
- The email regex check is very basic, just checks for the general
  `something@something.something` shape, not whether the domain
  actually exists.
