import sqlite3
import streamlit as st
from database import DATABASE_NAME


# Function to filter students from database
def filter_students(
    conn,
    min_marks=0,
    max_marks=100,
    min_attendance=0,
    max_attendance=100,
    min_study_hours=0
):

    query = """
        SELECT student_id, student_name, marks,
               attendance, study_hours
        FROM students
        WHERE marks BETWEEN ? AND ?
        AND attendance BETWEEN ? AND ?
        AND study_hours >= ?
        ORDER BY student_name
    """

    parameters = (
        min_marks,
        max_marks,
        min_attendance,
        max_attendance,
        min_study_hours
    )

    cursor = conn.execute(query, parameters)

    columns = [column[0] for column in cursor.description]

    students = [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

    return students


# Streamlit interface
def show_filter_students():

    st.title("Student Performance Tracking System")

    st.subheader("Filter Students")

    st.write(
        "Use the filters below to find students "
        "based on marks, attendance and study hours."
    )

    # Filter form
    with st.form("filter_form"):

        st.write("### Select Filter Conditions")

        # Marks filter
        marks_range = st.slider(
            "Marks Range",
            min_value=0.0,
            max_value=100.0,
            value=(0.0, 100.0),
            step=1.0
        )

        # Attendance filter
        attendance_range = st.slider(
            "Attendance Range (%)",
            min_value=0.0,
            max_value=100.0,
            value=(0.0, 100.0),
            step=1.0
        )

        # Study hours filter
        min_study_hours = st.number_input(
            "Minimum Study Hours",
            min_value=0.0,
            value=0.0,
            step=0.5
        )

        # Apply filter button
        submitted = st.form_submit_button(
            "Apply Filter"
        )

    # Display results
    if submitted:

        try:
            with sqlite3.connect(DATABASE_NAME) as conn:

                students = filter_students(
                    conn,
                    min_marks=marks_range[0],
                    max_marks=marks_range[1],
                    min_attendance=attendance_range[0],
                    max_attendance=attendance_range[1],
                    min_study_hours=min_study_hours
                )

            st.write("### Filter Results")

            if students:

                st.success(
                    f"Found {len(students)} matching student(s)."
                )

                st.dataframe(
                    students,
                    width="stretch",
                    hide_index=True
                )

            else:

                st.info(
                    "No students match the selected filters."
                )

        except sqlite3.Error:

            st.error(
                "An error occurred while retrieving student records."
            )


# Run independently for testing
if __name__ == "__main__":

    show_filter_students()
