"""
perf_comparison.py

Simple experiment: take a decent-sized dataset and apply the same
transformation two ways - once with a plain Python for-loop, once
vectorized with pandas/numpy - and time both.

Also does a quick chunking demo at the end, just to see that you don't
need to load everything into memory at once to process it.
"""

import time
import numpy as np
import pandas as pd


N_ROWS = 1_000_000


def make_data(n_rows):
    rng = np.random.default_rng(42)
    df = pd.DataFrame({
        "price": rng.uniform(10, 500, size=n_rows),
        "quantity": rng.integers(1, 20, size=n_rows),
        "discount_pct": rng.uniform(0, 0.3, size=n_rows),
    })
    return df


def slow_loop_version(df):
    """
    The way you'd write this if you were thinking row by row.
    Loops over every row with .iloc, does the math in Python.
    """
    totals = []
    for i in range(len(df)):
        price = df["price"].iloc[i]
        qty = df["quantity"].iloc[i]
        discount = df["discount_pct"].iloc[i]
        total = price * qty * (1 - discount)
        totals.append(total)
    return pd.Series(totals)


def vectorized_version(df):
    """
    Same math, but done as a single operation across the whole column
    at once instead of one row at a time.
    """
    return df["price"] * df["quantity"] * (1 - df["discount_pct"])


def chunked_version(df, chunk_size=100_000):
    """
    Shows the same vectorized math but done in chunks, like you'd do
    if the file was too big to comfortably fit in memory all at once.
    """
    results = []
    for start in range(0, len(df), chunk_size):
        chunk = df.iloc[start:start + chunk_size]
        result = chunk["price"] * chunk["quantity"] * (1 - chunk["discount_pct"])
        results.append(result)
    return pd.concat(results)


def main():
    print(f"Building a test dataset with {N_ROWS:,} rows...")
    df = make_data(N_ROWS)

    # Use a smaller slice for the loop version - the full 1M rows in a
    # Python loop takes way too long to sit around waiting for.
    loop_sample_size = 20_000
    loop_df = df.iloc[:loop_sample_size].copy()

    print(f"\nRunning the loop version on {loop_sample_size:,} rows (full "
          f"{N_ROWS:,} would take too long)...")
    start = time.perf_counter()
    loop_result = slow_loop_version(loop_df)
    loop_time = time.perf_counter() - start
    print(f"Loop version took {loop_time:.3f} seconds")

    print(f"\nRunning the vectorized version on the full {N_ROWS:,} rows...")
    start = time.perf_counter()
    vec_result = vectorized_version(df)
    vec_time = time.perf_counter() - start
    print(f"Vectorized version took {vec_time:.3f} seconds")

    # fair comparison: vectorized version on the same small sample the loop used
    start = time.perf_counter()
    vec_result_sample = vectorized_version(loop_df)
    vec_sample_time = time.perf_counter() - start

    print(f"\nRunning chunked version on the full {N_ROWS:,} rows (100k rows "
          f"per chunk)...")
    start = time.perf_counter()
    chunk_result = chunked_version(df)
    chunk_time = time.perf_counter() - start
    print(f"Chunked version took {chunk_time:.3f} seconds")

    # sanity check - results should match
    matches = np.allclose(loop_result.values, vec_result_sample.values)
    print(f"\nLoop and vectorized results match: {matches}")

    speedup_same_size = loop_time / vec_sample_time
    print(f"\nOn the same {loop_sample_size:,} rows, vectorized was "
          f"{speedup_same_size:.0f}x faster than the loop.")
    print(f"(Loop: {loop_time:.3f}s vs vectorized: {vec_sample_time:.4f}s "
          f"for the same {loop_sample_size:,} rows)")

    with open("results.txt", "w") as f:
        f.write("Performance Comparison Results\n")
        f.write("===============================\n\n")
        f.write(f"Dataset size: {N_ROWS:,} rows\n\n")
        f.write(f"Loop version ({loop_sample_size:,} rows): {loop_time:.3f} seconds\n")
        f.write(f"Vectorized version (same {loop_sample_size:,} rows): "
                f"{vec_sample_time:.4f} seconds\n")
        f.write(f"Vectorized version (full {N_ROWS:,} rows): {vec_time:.3f} seconds\n")
        f.write(f"Chunked version (full {N_ROWS:,} rows, 100k per chunk): "
                f"{chunk_time:.3f} seconds\n\n")
        f.write(f"Results match between loop and vectorized: {matches}\n\n")
        f.write(f"Speedup (same row count): {speedup_same_size:.0f}x faster with "
                f"vectorization\n")

    print("\nSaved results to results.txt")


if __name__ == "__main__":
    main()
