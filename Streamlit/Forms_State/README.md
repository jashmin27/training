# Task 7.2 - Forms & State

**Learn:** forms, session_state, callbacks, validation, state transitions.
**Task:** multi-step input workflow without losing user data.

## What it does
Adds an employee in 3 steps: (1) name + email, (2) department + role, (3) review and save.
The new employee is written to the same `data/employees.csv` that 7.1 displays.

## Topics used
- Forms: `st.form`, `st.form_submit_button`
- State: `st.session_state` holds `step`, `data`, `error`, `message`
- Callbacks: `on_click=` functions move between steps
- Validation: name/email in step 1, role in step 2

## Pass: managing state predictably
- The current step and typed data live only in `session_state`.
- Step changes happen only inside callbacks (`next_...`, `back_...`).
- "Back" saves what was typed, so nothing is lost.

## Connection
Run 7.1 after saving an employee here to see the new row in the viewer.
Next: 7.3 splits everything into pages.

Run: `streamlit run app.py`
