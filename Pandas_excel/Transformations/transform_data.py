"""
transform_data.py

Takes orders.csv + customers.csv and builds two reports:
1. monthly_summary.csv   - total sales and orders per month
2. city_product_pivot.csv - cross-table of sales, city vs product

Run: python3 transform_data.py
"""

import pandas as pd

orders = pd.read_csv("orders.csv")
customers = pd.read_csv("customers.csv")

# --- calculated column: total = quantity * unit_price ---
orders["total"] = orders["quantity"] * orders["unit_price"]

# --- join orders with customers to bring in the city ---
data = orders.merge(customers, on="customer_id", how="left")

# --- sort by date just to keep things in order ---
data["order_date"] = pd.to_datetime(data["order_date"])
data = data.sort_values("order_date")

# --- filter: keep only orders with at least 5 units (drop tiny test orders) ---
data = data[data["quantity"] >= 5]

# --- add a month column to group by ---
data["month"] = data["order_date"].dt.strftime("%Y-%m")

# ---------------------------------------------------------
# Report 1: Monthly summary (groupby + aggregate)
# ---------------------------------------------------------
monthly_summary = data.groupby("month").agg(
    total_orders=("order_id", "count"),
    total_quantity=("quantity", "sum"),
    total_sales=("total", "sum"),
).reset_index()

monthly_summary.to_csv("monthly_summary.csv", index=False)
print("Saved monthly_summary.csv")
print(monthly_summary)

# ---------------------------------------------------------
# Report 2: Cross-table - city vs product, total sales (pivot)
# ---------------------------------------------------------
city_product_pivot = pd.pivot_table(
    data,
    values="total",
    index="city",
    columns="product",
    aggfunc="sum",
    fill_value=0,
)

city_product_pivot.to_csv("city_product_pivot.csv")
print("\nSaved city_product_pivot.csv")
print(city_product_pivot)
