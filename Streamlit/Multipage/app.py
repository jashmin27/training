import streamlit as st

from config import APP_TITLE

st.set_page_config(page_title=APP_TITLE)
st.title(APP_TITLE)
st.write("Use the sidebar to open a page: **View**, **Add**, or **Edit Delete**.")
