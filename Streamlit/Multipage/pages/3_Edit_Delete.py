import streamlit as st

from components import load_employees, save_employees, show_table
from config import DEPARTMENTS

st.title("Edit / Delete Employee")


def delete_employee(emp_id):
    df = load_employees()
    save_employees(df[df["ID"] != emp_id])
    st.session_state.deleted = True


if st.session_state.pop("deleted", False):
    st.success("Employee deleted.")

df = load_employees()
if df.empty:
    st.info("No employees to edit.")
    st.stop()

emp_id = st.selectbox(
    "Select employee",
    df["ID"],
    format_func=lambda i: f"{i} - {df.loc[df['ID'] == i, 'Name'].iloc[0]}",
)
row = df[df["ID"] == emp_id].iloc[0]

with st.form("edit_form"):
    name = st.text_input("Name", value=row["Name"])
    department = st.selectbox("Department", DEPARTMENTS, index=DEPARTMENTS.index(row["Department"]))
    role = st.text_input("Role", value=row["Role"])
    email = st.text_input("Email", value=row["Email"])
    update = st.form_submit_button("Update")

if update:
    df.loc[df["ID"] == emp_id, ["Name", "Department", "Role", "Email"]] = [name, department, role, email]
    save_employees(df)
    st.success("Employee updated.")

st.button("Delete this employee", on_click=delete_employee, args=(emp_id,))
st.subheader("Current employees")
show_table(load_employees())
