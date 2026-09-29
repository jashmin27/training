# Task 7.3 - Multi-page Apps

**Learn:** page organization, navigation, reusable UI components, configuration.
**Task:** 3-page CRUD-style application.

## Structure
```
app.py             home page
config.py          settings: title, data file path, departments
components.py      reusable pieces: load_employees, save_employees, show_table
pages/
  1_View.py        Read
  2_Add.py         Create
  3_Edit_Delete.py Update + Delete
```

## Topics used
- Navigation: files inside `pages/` appear in the sidebar automatically (numbers set the order)
- Reusable component: `show_table` is used by the View and Edit/Delete pages
- Configuration: `config.py` keeps settings in one place
- Reuses the forms from 7.2 and the same `data/employees.csv`

## Pass: maintainable structure
Each page does one job, and shared code lives in `config.py` and `components.py`.

## Next
7.4 improves how the app behaves with filters, downloads, and errors.

Run from this folder: `streamlit run app.py`
