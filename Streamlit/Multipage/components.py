import pandas as pd
import streamlit as st

from config import DATA_FILE


def load_employees():
    return pd.read_csv(DATA_FILE)


def save_employees(df):
    df.to_csv(DATA_FILE, index=False)


def show_table(df):
    """Reusable table, used by more than one page."""
    if df.empty:
        st.info("No employees yet.")
    else:
        st.dataframe(df, hide_index=True)
