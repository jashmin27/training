from datetime import date

import streamlit as st

from components import load_employees, save_employees
from config import DEPARTMENTS

st.title("Add Employee")
df = load_employees()

with st.form("add_form", clear_on_submit=True):
    name = st.text_input("Name")
    department = st.selectbox("Department", DEPARTMENTS)
    role = st.text_input("Role")
    email = st.text_input("Email")
    submitted = st.form_submit_button("Add")

if submitted:
    if not name.strip() or "@" not in email:
        st.error("Enter a name and a valid email.")
    else:
        new_id = int(df["ID"].max()) + 1 if not df.empty else 1
        df.loc[len(df)] = [new_id, name, department, role, email, str(date.today())]
        save_employees(df)
        st.success(f"{name} added with ID {new_id}.")
