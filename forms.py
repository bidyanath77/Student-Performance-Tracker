import sqlite3
import math
import streamlit as st
import database

from database import create_table, add_student, get_students


# ==========================================
# STUDENT VALIDATION - SPRINT 2
# ==========================================

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


# ==========================================
# ADD STUDENT FORM - SPRINT 1 & 2
# ==========================================

def show_student_form():

    create_table()

    st.title("➕ Add Student")
    st.write("Enter student performance information.")

    # Initialize session state for resetting the form
    if "form_version" not in st.session_state:
        st.session_state.form_version = 0

    # Create student entry form
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

                st.session_state.success_message = (
                    f"Student saved successfully! ID: {student_id}"
                )

                st.rerun()

            except sqlite3.Error as error:
                st.error(f"Database error: {error}")

    # Display success message
    if "success_message" in st.session_state:
        st.success(st.session_state.pop("success_message"))


# ==========================================
# EDIT STUDENT FORM - SPRINT 3
# ==========================================

def show_edit_student_form():

    st.title("✏️ Edit Student")
    st.write("Select a student to update their information.")

    # Initialize database and retrieve students
    try:
        create_table()
        students = get_students()

    except sqlite3.Error as error:
        st.error(f"Database error: {error}")
        return

    # Display success message
    if "edit_success" in st.session_state:
        st.success(st.session_state.pop("edit_success"))

    # Check whether student records exist
    if not students:
        st.warning("No student records found.")
        return

    # Store students using their IDs
    student_records = {
        student[0]: student
        for student in students
    }

    # Select student
    selected_id = st.selectbox(
        "Select Student",
        options=list(student_records.keys()),
        format_func=lambda student_id: (
            f"{student_id} - {student_records[student_id][1]}"
        ),
        key="edit_selected_student"
    )

    # Retrieve selected student's information
    selected_student = student_records[selected_id]

    # Initialize edit form version
    if "edit_form_version" not in st.session_state:
        st.session_state.edit_form_version = 0

    version = st.session_state.edit_form_version

    # Display current student information
    with st.form(f"edit_student_{selected_id}_{version}"):

        student_name = st.text_input(
            "Student Name",
            value=selected_student[1],
            key=f"edit_name_{selected_id}_{version}"
        )

        marks = st.number_input(
            "Marks",
            min_value=0.0,
            max_value=100.0,
            value=float(selected_student[2] or 0.0),
            key=f"edit_marks_{selected_id}_{version}"
        )

        attendance = st.number_input(
            "Attendance (%)",
            min_value=0.0,
            max_value=100.0,
            value=float(selected_student[3] or 0.0),
            key=f"edit_attendance_{selected_id}_{version}"
        )

        study_hours = st.number_input(
            "Study Hours",
            min_value=0.0,
            max_value=24.0,
            value=float(selected_student[4] or 0.0),
            key=f"edit_hours_{selected_id}_{version}"
        )

        update_button = st.form_submit_button(
            "Update Student"
        )

    # Process update request
    if update_button:

        # Validate updated information
        is_valid, message = validate_student(
            student_name,
            marks,
            attendance,
            study_hours
        )

        if not is_valid:
            st.error(message)
            return

        # Check whether update function is available
        if not hasattr(database, "update_student"):
            st.error(
                "Update function is not available yet. "
                "Please merge the database changes first."
            )
            return

        try:
            # Update student using Manisha's database function
            database.update_student(
                selected_id,
                student_name.strip(),
                marks,
                attendance,
                study_hours
            )

            # Retrieve updated student records
            updated_students = get_students()

            updated_student = next(
                (
                    student for student in updated_students
                    if student[0] == selected_id
                ),
                None
            )

            # Verify updated information was saved
            if updated_student is not None:

                saved_data = (
                    updated_student[1],
                    updated_student[2],
                    updated_student[3],
                    updated_student[4]
                )

                expected_data = (
                    student_name.strip(),
                    float(marks),
                    float(attendance),
                    float(study_hours)
                )

                if saved_data == expected_data:

                    st.session_state.edit_success = (
                        "Student information updated successfully!"
                    )

                    # Refresh form after updating
                    st.session_state.edit_form_version += 1

                    st.rerun()

                else:
                    st.error(
                        "Student update could not be verified."
                    )

            else:
                st.error("Student record not found.")

        except sqlite3.Error as error:
            st.error(f"Database error: {error}")


# ==========================================
# DELETE STUDENT FORM - SPRINT 3
# ==========================================

def show_delete_student_form():

    st.title("🗑️ Delete Student")
    st.write("Select a student to delete their record.")

    # Initialize database and retrieve students
    try:
        create_table()
        students = get_students()

    except sqlite3.Error as error:
        st.error(f"Database error: {error}")
        return

    # Display success message
    if "delete_success" in st.session_state:
        st.success(st.session_state.pop("delete_success"))

    # Check whether student records exist
    if not students:
        st.warning("No student records available.")
        return

    # Store students using student IDs
    student_records = {
        student[0]: student
        for student in students
    }

    # Select student to delete
    selected_id = st.selectbox(
        "Select Student to Delete",
        options=list(student_records.keys()),
        format_func=lambda student_id: (
            f"{student_id} - {student_records[student_id][1]}"
        ),
        key="delete_selected_student"
    )

    # Retrieve selected student information
    selected_student = student_records[selected_id]

    # Display student information
    st.subheader("Student Information")

    st.write(f"**Student ID:** {selected_student[0]}")
    st.write(f"**Student Name:** {selected_student[1]}")
    st.write(f"**Marks:** {selected_student[2]}")
    st.write(f"**Attendance:** {selected_student[3]}%")
    st.write(f"**Study Hours:** {selected_student[4]}")

    # Warning before deletion
    st.warning(
        "Warning: This action will permanently delete "
        "the selected student record."
    )

    # Confirmation form
    with st.form(f"delete_student_{selected_id}"):

        confirm_delete = st.checkbox(
            "I confirm that I want to delete this student."
        )

        delete_button = st.form_submit_button(
            "Delete Student"
        )

    # Process deletion
    if delete_button:

        # Require confirmation
        if not confirm_delete:
            st.error(
                "Please confirm before deleting the student."
            )
            return

        # Check whether delete function exists
        if not hasattr(database, "delete_student"):
            st.error(
                "Delete function is not available yet. "
                "Please merge the database changes first."
            )
            return

        try:
            # Delete student using Manisha's database function
            database.delete_student(selected_id)

            # Retrieve students after deletion
            remaining_students = get_students()

            # Verify student was deleted
            student_exists = any(
                student[0] == selected_id
                for student in remaining_students
            )

            if not student_exists:

                st.session_state.delete_success = (
                    "Student deleted successfully!"
                )

                st.rerun()

            else:
                st.error(
                    "Student deletion could not be verified."
                )

        except sqlite3.Error as error:
            st.error(f"Database error: {error}")


# ==========================================
# FORM NAVIGATION - LOCAL TESTING
# ==========================================

if __name__ == "__main__":

    st.sidebar.title("Student Performance Tracker")

    page = st.sidebar.radio(
        "Select an Option",
        [
            "Add Student",
            "Edit Student",
            "Delete Student"
        ]
    )

    if page == "Add Student":
        show_student_form()

    elif page == "Edit Student":
        show_edit_student_form()

    elif page == "Delete Student":
        show_delete_student_form()
