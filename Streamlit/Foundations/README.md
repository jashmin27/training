# Sales Data Viewer (Streamlit)

Simple multi-section data viewer built with Streamlit. It loads a sales
CSV and shows it in 4 tabs: Overview, Table, Charts and Summary.

## Files

```
app.py       - the streamlit app
sales.csv    - sample data (150 rows: date, region, product, units, price, revenue)
README.md    - this file
```

## How to run

```
pip install streamlit pandas
streamlit run app.py
```

It opens in the browser at http://localhost:8501.

## What's in the app

- **Sidebar** - upload your own CSV (optional), filter by region and
  product, and a slider for how many rows to show in the table
- **Overview** - total revenue, units sold and number of orders
- **Table** - the filtered data
- **Charts** - revenue by region, revenue by product, revenue over time
- **Summary** - describe() stats and a region x product pivot table

If you upload your own file it needs the same columns as `sales.csv`
(date, region, product, units, price, revenue), otherwise the app will
throw an error.

## How Streamlit's execution model works (my understanding)

- Streamlit runs the whole script from top to bottom, like a normal
  python file.
- Every time the user does something (changes a dropdown, moves the
  slider, uploads a file) the **entire script runs again from the top**.
  This is called a rerun.
- Widgets return their current value each time the script runs. So
  `st.multiselect(...)` just gives back the list of what's currently
  selected, and the rest of the code uses that to filter the data.
- Since everything reruns, slow stuff like reading the csv would
  happen every time. `@st.cache_data` fixes that by remembering the
  result of `load_data` so it only actually loads once per file.
- Normal variables are reset on every rerun. If something has to
  survive between reruns you need `st.session_state` (not needed in
  this app).
- `st.stop()` ends the script early. I use it when the filters leave
  no data so the tabs below dont crash on an empty table.
- Layout stuff (`st.sidebar`, `st.columns`, `st.tabs`) only changes
  where things are drawn, the script still runs top to bottom.

## Notes

- Didn't add any database or extra pages, kept it to one file since the
  task was about the basics (widgets, layout, rerun).
- Charts use the built in `st.bar_chart` / `st.line_chart` so no extra
  chart libraries are needed.
