# Task 7.1 - Foundations

**Learn:** app execution, widgets, text/table/chart output, layout, rerun model.
**Task:** multi-section data viewer.

## What it does
Reads `data/employees.csv` and shows three sections: Summary (metrics), Table, Chart.
A sidebar dropdown filters by department.

## Topics used
- Text: `st.title`, `st.header`
- Widget: `st.selectbox`
- Table / chart: `st.dataframe`, `st.bar_chart`, `st.metric`
- Layout: `st.columns`, `st.sidebar`

## Pass: Streamlit's execution model
Streamlit runs the script from top to bottom. Every time a widget changes, it runs the
**whole script again** (a rerun). The widget returns its new value, so the page updates.
Normal variables are lost on each rerun (this is why 7.2 needs `session_state`).

## Next
7.2 adds new employees using forms and state.

Run: `streamlit run app.py`
