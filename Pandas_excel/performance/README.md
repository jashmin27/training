# Loop vs Vectorized Performance Comparison

Small experiment to see the actual difference between looping over a
DataFrame row by row vs doing the same math as a vectorized pandas/numpy
operation.

## What it does

Built a 1,000,000 row dataset (price, quantity, discount) and calculated
`total = price * quantity * (1 - discount)` three different ways:

1. **Loop version** - `for` loop using `.iloc` to grab each row's values one
   at a time and do the math in plain Python. Only ran this on 20,000 rows
   because running it on the full million would take way too long.
2. **Vectorized version** - same formula, but applied to the whole column at
   once (`df["price"] * df["quantity"] * (1 - df["discount_pct"])`). Ran this
   on the full 1,000,000 rows.
3. **Chunked version** - same vectorized formula, but processed 100,000 rows
   at a time instead of all at once. This is what you'd do if the real data
   was too big to comfortably fit in memory.

## Results

On the same 20,000 rows:
- Loop: ~0.75 seconds
- Vectorized: ~0.0005 seconds
- **That's about 1500x faster**, just from not looping.

The vectorized version handled the full 1,000,000 rows in ~0.01 seconds -
faster than the loop managed on 2% of the data.

The chunked version (also on the full 1,000,000 rows) took about the same
time as the plain vectorized version, since it's still using vectorized math
under the hood, just processed in batches instead of one shot.

Exact numbers are in `results.txt` from the last run.

## Why the loop is slow

Every `.iloc[i]` call and every arithmetic operation inside the loop runs in
plain Python, one row at a time, with Python's usual overhead on top of each
step. Pandas/numpy vectorized operations push the loop down into C, so the
whole column gets processed in one compiled operation instead of a million
tiny ones.

## Why chunking matters

Vectorized operations are fast, but they still need the data in memory. If a
file is bigger than your RAM can hold, you can't just load it all and run one
big vectorized operation. Chunking - processing, say, 100k rows at a time and
combining the results - lets you keep the speed of vectorization while only
holding one chunk in memory at a time.

## Files here

- `perf_comparison.py` - the script that runs all three versions and times them
- `results.txt` - the numbers from the last run
- `README.md` - this file
