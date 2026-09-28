# 7.2 Forms & State - Multi-step Form

A small Streamlit app that has a 3-step form. The main goal was to practice
`st.session_state`, callbacks, validation and moving between steps without
losing what the user typed.

## Steps

1. **Personal Details** - name, email, age
2. **Education & Skills** - course, year, skills
3. **Review** - shows everything, then Submit

After submitting, a success page shows the saved data and a button to start again.

## How the state is managed

- `st.session_state.step` keeps track of which step we are on (1 to 3, and 4 after submit).
- `st.session_state.data` is a dictionary that stores the values of all steps.
- `st.session_state.errors` stores validation messages to show on the page.
- Buttons use `on_click` callbacks (`go_next`, `go_back`, `submit`, `reset`)
  so the state changes before the page reruns.
- Streamlit removes widget values when a widget is not shown on the page, so the
  values are copied into the `data` dictionary when clicking Next/Back.
  The widgets read their default value from `data`, so going back
  shows the old answers.

## Validation

- Name cannot be empty
- Email must look like a valid email
- Age must be 16 or above
- Skills cannot be empty

If validation fails, the user stays on the same step and sees the errors.

## How to run

```
pip install streamlit
streamlit run app.py
```

## Files

- `app.py` - the whole app
- `README.md` - this file
