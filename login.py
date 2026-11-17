
import streamlit as st
from auth import authenticate_user


def show_login_form():
    st.title("🎓 Student Performance Tracking System")
    st.subheader("Login")

    st.write("Please log in to access the student dashboard.")

    with st.form("login_form"):
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        submitted = st.form_submit_button("Login")

        if submitted:
            if not username.strip() or not password:
                st.error("Please enter both username and password.")

            elif authenticate_user(username, password):
                st.session_state["logged_in"] = True
                st.success("Login successful!")
                st.rerun()

            else:
                st.error("Invalid username or password.")

