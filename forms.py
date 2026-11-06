
import sqlite3
import math
import streamlit as st

from database import create_table, add_student


# Validate student information before saving
def validate_student(student_name, marks, attendance, study_hours):

    # Validate student name
    if not isinstance(student_name, str) or not student_name.strip():
        return False, "Student Name is required."

    # Validate marks
    if (
        isinstance(marks, bool)
        or not isinstance(marks, (int, float))
        or not math.isfinite(marks)
        or not 0 <= marks <= 100
    ):
        return False, "Marks must be between 0 and 100."

    # Validate attendance
    if (
        isinstance(attendance, bool)
        or not isinstance(attendance, (int, float))
        or not math.isfinite(attendance)
        or not 0 <= attendance <= 100
    ):
        return False, "Attendance must be between 0 and 100."

    # Validate study hours
    if (
        isinstance(study_hours, bool)
        or not isinstance(study_hours, (int, float))
        or not math.isfinite(study_hours)
        or not 0 <= study_hours <= 24
    ):
        return False, "Study hours must be between 0 and 24."

    return True, "Valid student data."


# Display the student entry form
def show_student_form():

    # Initialize database
    create_table()

    st.title("➕ Add Student")
    st.write("Enter student performance information.")

    # Initialize session state for resetting the form
    if "form_version" not in st.session_state:
        st.session_state.form_version = 0

    # Create the student entry form
    with st.form(f"student_form_{st.session_state.form_version}"):

        student_name = st.text_input("Student Name")

        marks = st.number_input(
            "Marks",
            min_value=0.0,
            max_value=100.0,
            value=0.0
        )

        attendance = st.number_input(
            "Attendance (%)",
            min_value=0.0,
            max_value=100.0,
            value=0.0
        )

        study_hours = st.number_input(
            "Study Hours",
            min_value=0.0,
            max_value=24.0,
            value=0.0
        )

        save_button = st.form_submit_button("Save Student")

    # Process form submission
    if save_button:

        # Validate the entered data
        is_valid, message = validate_student(
            student_name,
            marks,
            attendance,
            study_hours
        )

        if not is_valid:
            st.error(message)

        else:
            try:
                # Save student to SQLite database
                student_id = add_student(
                    student_name.strip(),
                    marks,
                    attendance,
                    study_hours
                )

                # Reset form after successful submission
                st.session_state.form_version += 1

                # Store success message
                st.session_state.success_message = (
                    f"Student saved successfully! ID: {student_id}"
                )

                st.rerun()

            except sqlite3.Error as error:
                st.error(f"Database error: {error}")

    # Display success message after rerun
    if "success_message" in st.session_state:
        st.success(st.session_state.pop("success_message"))
