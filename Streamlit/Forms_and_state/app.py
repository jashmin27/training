import re
import streamlit as st

st.set_page_config(page_title="Registration Form")

COURSES = ["B.Tech", "M.Tech", "BCA", "MCA", "Other"]
YEARS = ["1st", "2nd", "3rd", "4th"]

# ---------- initial state ----------
if "step" not in st.session_state:
    st.session_state.step = 1          # 1, 2, 3 = form steps, 4 = submitted
if "data" not in st.session_state:
    st.session_state.data = {
        "name": "",
        "email": "",
        "age": 18,
        "course": COURSES[0],
        "year": YEARS[0],
        "skills": "",
    }
if "errors" not in st.session_state:
    st.session_state.errors = []


# ---------- validation ----------
def validate_step1(name, email, age):
    errors = []
    if not name.strip():
        errors.append("Name is required.")
    if not re.match(r"^[\w.+-]+@[\w-]+\.[\w.]+$", email.strip()):
        errors.append("Please enter a valid email.")
    if age < 16:
        errors.append("Age must be 16 or above.")
    return errors


def validate_step2(skills):
    errors = []
    if len(skills.strip()) < 3:
        errors.append("Please enter at least one skill.")
    return errors


# ---------- callbacks ----------
def go_next():
    step = st.session_state.step
    data = st.session_state.data

    if step == 1:
        errors = validate_step1(
            st.session_state.name_input,
            st.session_state.email_input,
            st.session_state.age_input,
        )
        if errors:
            st.session_state.errors = errors
            return
        # save to data only when valid
        data["name"] = st.session_state.name_input.strip()
        data["email"] = st.session_state.email_input.strip()
        data["age"] = st.session_state.age_input

    elif step == 2:
        errors = validate_step2(st.session_state.skills_input)
        if errors:
            st.session_state.errors = errors
            return
        data["course"] = st.session_state.course_input
        data["year"] = st.session_state.year_input
        data["skills"] = st.session_state.skills_input.strip()

    st.session_state.errors = []
    st.session_state.step += 1


def go_back():
    # save whatever is typed on step 2 so it is not lost when going back
    if st.session_state.step == 2:
        st.session_state.data["course"] = st.session_state.course_input
        st.session_state.data["year"] = st.session_state.year_input
        st.session_state.data["skills"] = st.session_state.skills_input
    st.session_state.errors = []
    st.session_state.step -= 1


def submit():
    st.session_state.step = 4


def reset():
    del st.session_state["step"]
    del st.session_state["data"]
    del st.session_state["errors"]


# ---------- UI ----------
st.title("Registration Form")

step = st.session_state.step
data = st.session_state.data

if step <= 3:
    st.progress(step / 3)
    st.write(f"Step {step} of 3")

for e in st.session_state.errors:
    st.error(e)

if step == 1:
    st.subheader("Personal Details")
    st.text_input("Name", value=data["name"], key="name_input")
    st.text_input("Email", value=data["email"], key="email_input")
    st.number_input("Age", min_value=1, max_value=100, value=data["age"], key="age_input")
    st.button("Next", on_click=go_next)

elif step == 2:
    st.subheader("Education & Skills")
    st.selectbox("Course", COURSES, index=COURSES.index(data["course"]), key="course_input")
    st.selectbox("Year", YEARS, index=YEARS.index(data["year"]), key="year_input")
    st.text_area("Skills (comma separated)", value=data["skills"], key="skills_input")
    col1, col2 = st.columns(2)
    col1.button("Back", on_click=go_back)
    col2.button("Next", on_click=go_next)

elif step == 3:
    st.subheader("Review")
    st.write(f"**Name:** {data['name']}")
    st.write(f"**Email:** {data['email']}")
    st.write(f"**Age:** {data['age']}")
    st.write(f"**Course:** {data['course']} ({data['year']} year)")
    st.write(f"**Skills:** {data['skills']}")
    col1, col2 = st.columns(2)
    col1.button("Back", on_click=go_back)
    col2.button("Submit", on_click=submit)

elif step == 4:
    st.success("Form submitted successfully!")
    st.json(data)
    st.button("Fill another form", on_click=reset)
