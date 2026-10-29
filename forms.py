
import sqlite3
import streamlit as st
import pandas as pd

from database import create_table, add_student, get_students


def show_student_form():
    create_table()

    st.title("➕ Add Student")
    st.write("Enter student performance information.")

    if "form_version" not in st.session_state:
        st.session_state.form_version = 0

    with st.form(f"student_form_{st.session_state.form_version}"):
        student_name = st.text_input("Student Name")

        marks = st.number_input(
            "Marks", min_value=0.0, max_value=100.0
        )

        attendance = st.number_input(
            "Attendance (%)", min_value=0.0, max_value=100.0
        )

        study_hours = st.number_input(
            "Study Hours", min_value=0.0, max_value=24.0
        )

        save_button = st.form_submit_button("Save Student")

    if save_button:
        if not student_name.strip():
            st.error("Student Name is required.")
        else:
            try:
                student_id = add_student(
                    student_name.strip(),
                    marks,
                    attendance,
                    study_hours
                )

                st.session_state.form_version += 1
                st.session_state.success_message = (
                    f"Student saved successfully! ID: {student_id}"
                )
                st.rerun()

            except sqlite3.Error as error:
                st.error(f"Database error: {error}")

    if "success_message" in st.session_state:
        st.success(st.session_state.pop("success_message"))
