# Sales Report Workbook

Built this with openpyxl to practice reading/writing sheets, formulas vs hardcoded values, and basic formatting.

## What's in the workbook

**Sales** - raw sales records (date, region, product, units, unit price). Revenue column is a formula (`=D*E`), not typed-in numbers, so it recalculates if the units or price change.

**Expenses** - raw expense records (date, category, description, amount).

**Summary** - the actual report:
- Total Revenue, Total Expenses, Net Profit, Total Units Sold, Average Revenue per Sale - all pulled with `SUM`/`AVERAGE` formulas pointing at the other two sheets.
- Revenue by Region - `SUMIFS` per region, doesn't just eyeball the Sales sheet.
- Expenses by Category - same idea with `SUMIFS` on Expenses.

Nothing on the Summary sheet is a typed-in number - it's all formulas referencing the raw data sheets, so if I update a row in Sales or Expenses the totals update on their own.

## How I built it

- Wrote the raw data into `Sales` and `Expenses` first, in plain rows.
- Added the Revenue formula per row in Sales instead of computing it in Python and pasting the result.
- Built `Summary` last, referencing the other two sheets with `SUM`, `AVERAGE`, and `SUMIFS`.
- Bold headers with a light blue fill, currency formatting on the money columns, frozen header row on the data sheets.
- Ran it through a recalculation check afterward to make sure every formula actually evaluates (0 errors, 22 formulas).

## Files here
- `sales_report.xlsx` - the workbook
- `build_report.py` - the script that generates it, in case the data needs to change later
- `README.md` - this file
