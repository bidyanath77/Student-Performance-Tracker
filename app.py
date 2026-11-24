from recovery import show_recovery_page
from filter_students import show_filter_students
from find import find_students

from login import show_login_form

import streamlit as st
import pandas as pd
import plotly.express as px
import sqlite3

from database import create_table, get_students
from forms import (
    show_student_form,
    show_edit_student_form,
    show_delete_student_form
)
from analytics import (
    total_students,
    average_marks,
    average_attendance,
    average_study_hours
)

# Page configuration
st.set_page_config(
    page_title="Student Performance Tracker",
    page_icon="🎓",
    layout="wide"
)

# Initialize database
create_table()

# Show login page before accessing the dashboard
if not st.session_state.get("logged_in", False):
    show_login_form()
    st.stop()

# Logout functionality
if st.sidebar.button("🚪 Logout"):
    st.session_state["logged_in"] = False
    st.rerun()

# Sidebar navigation
st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "Dashboard",
        "Add Student",
        "View Students",
        "Edit Student",
        "Filter Students",
        "Find Student",
        "Delete Student",
        "Recovery"
        
    ]
)

# Load real student data from SQLite
def load_student_data():
    students = get_students()

    return pd.DataFrame(
        students,
        columns=[
            "student_id",
            "student_name",
            "marks",
            "attendance",
            "study_hours"
        ]
    )


try:
    df = load_student_data()

except sqlite3.Error as error:
    st.error(f"Database error: {error}")
    st.stop()

# Refresh dashboard
if st.sidebar.button("🔄 Refresh Dashboard"):
    st.session_state["refresh_message"] = True
    st.rerun()

if st.session_state.pop("refresh_message", False):
    st.sidebar.success("Dashboard refreshed successfully!")

# -------------------------------
# DASHBOARD PAGE
# -------------------------------

if page == "Dashboard":

    st.title("🎓 Student Performance Tracking System")
    st.write("Welcome to the Student Performance Dashboard!")
    st.divider()

    st.subheader("Dashboard Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Total Students", total_students(df))

    with col2:
        st.metric("Average Marks", f"{average_marks(df):.1f}%")

    with col3:
        st.metric(
            "Average Attendance",
            f"{average_attendance(df):.1f}%"
        )

    with col4:
        st.metric(
            "Average Study Hours",
            f"{average_study_hours(df):.1f}"
        )

    st.divider()

    st.subheader("Student Records")

    if df.empty:
        st.info(
            "No student records yet. Go to Add Student "
            "to enter your first student."
        )

    else:
        display_df = df.rename(
            columns={
                "student_id": "Student ID",
                "student_name": "Student Name",
                "marks": "Marks",
                "attendance": "Attendance (%)",
                "study_hours": "Study Hours"
            }
        )

        st.dataframe(
            display_df,
            hide_index=True,
            width="stretch"
        )

        st.divider()

        st.subheader("Student Marks Comparison")

        fig = px.bar(
            df,
            x="student_name",
            y="marks",
            text="marks",
            color="student_name",
            range_y=[0, 105],
            labels={
                "student_name": "Student",
                "marks": "Marks"
            }
        )

        fig.update_traces(textposition="outside")

        fig.update_layout(
            showlegend=False,
            dragmode=False,
            height=400
        )

        fig.update_xaxes(fixedrange=True)
        fig.update_yaxes(fixedrange=True)

        st.plotly_chart(
            fig,
            width="stretch",
            config={
                "scrollZoom": False,
                "displayModeBar": False
            }
        )

        st.divider()

        st.subheader("Individual Student Performance")

        selected_id = st.selectbox(
            "Select a student",
            df["student_id"].tolist(),
            format_func=lambda student_id: (
                df.loc[
                    df["student_id"] == student_id,
                    "student_name"
                ].iloc[0]
                + f" (ID: {student_id})"
            )
        )

        student = df[
            df["student_id"] == selected_id
        ].iloc[0]

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Student Marks",
                f"{student['marks']:.1f}%"
            )

        with col2:
            st.metric(
                "Student Attendance",
                f"{student['attendance']:.1f}%"
            )

        with col3:
            st.metric(
                "Study Hours",
                f"{student['study_hours']:.1f}"
            )

    st.divider()
    st.caption("Agile Team Project | Sprint 4")


# -------------------------------
# ADD STUDENT PAGE
# -------------------------------

elif page == "Add Student":
    show_student_form()


# -------------------------------
# VIEW STUDENTS PAGE
# -------------------------------

elif page == "View Students":

    st.title("📋 View Students")
    st.write("Student Records from SQLite Database")

    if df.empty:
        st.info("No students have been saved yet.")

    else:
        display_df = df.rename(
            columns={
                "student_id": "Student ID",
                "student_name": "Student Name",
                "marks": "Marks",
                "attendance": "Attendance (%)",
                "study_hours": "Study Hours"
            }
        )

        st.dataframe(
            display_df,
            hide_index=True,
            width="stretch"
        )

        st.success(
            f"Total students in database: {len(df)}"
        )

 # -------------------------------
# EDIT STUDENT PAGE

elif page == "Edit Student":
    show_edit_student_form()
    


# -------------------------------
# DELETE STUDENT PAGE
# -------------------------------

elif page == "Delete Student":
    show_delete_student_form()
    
    # Filter Students Page
elif page == "Filter Students":
    show_filter_students()
    
    #find Student Page

elif page == "Find Student":
    st.title("🔍 Find Student")
    st.write("Search for a student by name or Student ID.")

    with st.form("find_student_form"):
        search_term = st.text_input(
            "Enter Student Name or ID"
        )
        search_button = st.form_submit_button("Search")

    if search_button:
        if not search_term.strip():
            st.warning("Please enter a student name or ID.")
        else:
            try:
                results = find_students(search_term)

                if results:
                    st.success(
                        f"Found {len(results)} matching student(s)."
                    )

                    columns = [
                        "Student ID",
                        "Student Name",
                        "Marks",
                        "Attendance",
                        "Study Hours"
                    ]

                    df = pd.DataFrame(results, columns=columns)

                    st.dataframe(
                        df,
                        width="stretch",
                        hide_index=True
                    )
                else:
                    st.info("No matching students found.")

            except sqlite3.Error:
                st.error("Unable to search student records.")
# -------------------------------
# RECOVERY PAGE - SPRINT 5
# -------------------------------

elif page == "Recovery":
    show_recovery_page()
