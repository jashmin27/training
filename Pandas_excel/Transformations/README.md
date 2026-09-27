# Data Transformation Task - Orders Reports

## What this is
Two small tables - `orders.csv` (each order placed) and `customers.csv`
(which customer belongs to which city) - joined together and turned
into two reports using `transform_data.py`.

## How to run it
```
python3 transform_data.py
```
Needs pandas. Reads `orders.csv` and `customers.csv` from the same
folder and writes `monthly_summary.csv` and `city_product_pivot.csv`.

## What the script does
1. Adds a calculated column `total` = quantity x unit_price
2. Merges `orders` with `customers` on `customer_id` to bring in the city
3. Sorts everything by order date
4. Filters out small orders (quantity < 5), assuming those are test/
   sample entries and not real orders
5. Adds a `month` column (YYYY-MM) pulled from the order date
6. Groups by month to get order count, quantity, and total sales
7. Builds a pivot table: city vs product, total sales in each cell

## Output files

**monthly_summary.csv** - one row per month with:
- total_orders
- total_quantity
- total_sales

**city_product_pivot.csv** - cross-table report, cities as rows,
products as columns, values are total sales for that city+product
combination (0 if there were no sales for that combo)

## Assumptions made
- Orders with quantity under 5 were treated as test/sample data and
  filtered out before building the reports - didn't want them
  skewing the totals.
- "Monthly" grouping is based on `order_date`, not order_id order.
- Missing city/product combinations in the pivot are shown as 0, not
  blank, so the report is easier to read at a glance.
