import streamlit as st

from components import load_employees, show_table

st.title("View Employees")
show_table(load_employees())
