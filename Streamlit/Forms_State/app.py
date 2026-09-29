from datetime import date
from pathlib import Path

import pandas as pd
import streamlit as st

DATA_FILE = Path(__file__).resolve().parents[1] / "data" / "employees.csv"
DEPARTMENTS = ["Engineering", "HR", "Sales", "Finance", "Marketing", "Operations"]

# State is created once per session, so it survives reruns
if "step" not in st.session_state:
    st.session_state.step = 1
    st.session_state.data = {"Name": "", "Email": "", "Department": DEPARTMENTS[0], "Role": ""}
    st.session_state.error = ""
    st.session_state.message = ""


# ---------- callbacks (run before the rerun) ----------
def next_from_step1():
    name = st.session_state.f_name.strip()
    email = st.session_state.f_email.strip()
    if not name or "@" not in email:
        st.session_state.error = "Enter a name and a valid email."
        return
    st.session_state.data["Name"] = name
    st.session_state.data["Email"] = email
    st.session_state.error = ""
    st.session_state.step = 2


def back_from_step2():
    # save what was typed so nothing is lost
    st.session_state.data["Department"] = st.session_state.f_dept
    st.session_state.data["Role"] = st.session_state.f_role
    st.session_state.error = ""
    st.session_state.step = 1


def next_from_step2():
    role = st.session_state.f_role.strip()
    if not role:
        st.session_state.error = "Role is required."
        return
    st.session_state.data["Department"] = st.session_state.f_dept
    st.session_state.data["Role"] = role
    st.session_state.error = ""
    st.session_state.step = 3


def back_from_step3():
    st.session_state.step = 2


def save_employee():
    d = st.session_state.data
    df = pd.read_csv(DATA_FILE)
    new_id = int(df["ID"].max()) + 1 if not df.empty else 1
    df.loc[len(df)] = [new_id, d["Name"], d["Department"], d["Role"], d["Email"], str(date.today())]
    df.to_csv(DATA_FILE, index=False)
    st.session_state.message = f"{d['Name']} saved with ID {new_id}."
    st.session_state.data = {"Name": "", "Email": "", "Department": DEPARTMENTS[0], "Role": ""}
    st.session_state.step = 1


# ---------- page ----------
st.title("Add Employee")
if st.session_state.message:
    st.success(st.session_state.message)
    st.session_state.message = ""

step = st.session_state.step
data = st.session_state.data
st.write(f"Step {step} of 3")

if step == 1:
    with st.form("step1"):
        st.text_input("Name", value=data["Name"], key="f_name")
        st.text_input("Email", value=data["Email"], key="f_email")
        st.form_submit_button("Next", on_click=next_from_step1)
elif step == 2:
    with st.form("step2"):
        st.selectbox("Department", DEPARTMENTS, index=DEPARTMENTS.index(data["Department"]), key="f_dept")
        st.text_input("Role", value=data["Role"], key="f_role")
        col1, col2 = st.columns(2)
        col1.form_submit_button("Back", on_click=back_from_step2)
        col2.form_submit_button("Next", on_click=next_from_step2)
else:
    st.write("Please review:")
    st.write(f"**Name:** {data['Name']}")
    st.write(f"**Email:** {data['Email']}")
    st.write(f"**Department:** {data['Department']}")
    st.write(f"**Role:** {data['Role']}")
    col1, col2 = st.columns(2)
    col1.button("Back", on_click=back_from_step3)
    col2.button("Save employee", on_click=save_employee)

if st.session_state.error:
    st.error(st.session_state.error)
