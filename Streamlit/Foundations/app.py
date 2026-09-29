from pathlib import Path

import pandas as pd
import streamlit as st

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "employees.csv"

st.title("Employee Data Viewer")
df = pd.read_csv(DATA_FILE)

# Widget in the sidebar (layout). Changing it re-runs this whole script.
department = st.sidebar.selectbox("Department", ["All"] + sorted(df["Department"].unique()))
if department != "All":
    df = df[df["Department"] == department]

st.header("1. Summary")
col1, col2 = st.columns(2)
col1.metric("Employees", len(df))
col2.metric("Departments", df["Department"].nunique())

st.header("2. Table")
st.dataframe(df, hide_index=True)

st.header("3. Chart")
st.bar_chart(df["Department"].value_counts())
