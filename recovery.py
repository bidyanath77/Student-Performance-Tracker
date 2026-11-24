
import sqlite3
import streamlit as st
from database import DATABASE_NAME


# Create the Recycle Bin table if it does not exist
def create_recycle_bin(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS deleted_students (
            student_id INTEGER PRIMARY KEY,
            student_name TEXT NOT NULL,
            marks REAL,
            attendance REAL,
            study_hours REAL,
            deleted_at TEXT NOT NULL
                DEFAULT CURRENT_TIMESTAMP
        )
    """)


# Move a student from the active table to the Recycle Bin
def move_to_recycle_bin(student_id):
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute("BEGIN IMMEDIATE")
        create_recycle_bin(conn)

        student = conn.execute(
            """
            SELECT student_id, student_name, marks,
                   attendance, study_hours
            FROM students
            WHERE student_id = ?
            """,
            (student_id,)
        ).fetchone()

        if student is None:
            return False

        # Save the student in the Recycle Bin
        conn.execute(
            """
            INSERT INTO deleted_students
            (student_id, student_name, marks,
             attendance, study_hours)
            VALUES (?, ?, ?, ?, ?)
            """,
            student
        )

        # Remove the student from active records
        conn.execute(
            "DELETE FROM students WHERE student_id = ?",
            (student_id,)
        )

    return True


# Get all students currently in the Recycle Bin
def get_deleted_students():
    with sqlite3.connect(DATABASE_NAME) as conn:
        create_recycle_bin(conn)

        return conn.execute(
            """
            SELECT student_id, student_name, marks,
                   attendance, study_hours, deleted_at
            FROM deleted_students
            ORDER BY deleted_at DESC, student_id DESC
            """
        ).fetchall()


# Restore one student from the Recycle Bin
def restore_student(student_id):
    with sqlite3.connect(DATABASE_NAME) as conn:
        conn.execute("BEGIN IMMEDIATE")
        create_recycle_bin(conn)

        student = conn.execute(
            """
            SELECT student_id, student_name, marks,
                   attendance, study_hours
            FROM deleted_students
            WHERE student_id = ?
            """,
            (student_id,)
        ).fetchone()

        if student is None:
            return False

        # Prevent overwriting an existing student
        existing = conn.execute(
            "SELECT 1 FROM students WHERE student_id = ?",
            (student_id,)
        ).fetchone()

        if existing:
            raise ValueError(
                "This student ID is already used. "
                "Restoration needs manual review."
            )

        # Return the student to the main database
        conn.execute(
            """
            INSERT INTO students
            (student_id, student_name, marks,
             attendance, study_hours)
            VALUES (?, ?, ?, ?, ?)
            """,
            student
        )

        # Remove the restored student from Recycle Bin
        conn.execute(
            "DELETE FROM deleted_students WHERE student_id = ?",
            (student_id,)
        )

    return True


# Streamlit Recovery interface
def show_recovery_page():
    st.title("♻️ Student Recovery")
    st.subheader("Recycle Bin")

    st.write(
        "View deleted student records and restore "
        "them to the Student Performance Tracking System."
    )

    if "recovery_success" in st.session_state:
        st.success(st.session_state.pop("recovery_success"))

    try:
        deleted = get_deleted_students()
    except sqlite3.Error:
        st.error("Unable to load deleted student records.")
        return

    if not deleted:
        st.info("Recycle Bin is empty.")
        return

    st.write(f"### Deleted Students ({len(deleted)})")

    columns = [
        "Student ID", "Student Name", "Marks",
        "Attendance", "Study Hours", "Deleted At"
    ]

    st.dataframe(
        [dict(zip(columns, row)) for row in deleted],
        width="stretch",
        hide_index=True
    )

    student_records = {
        student[0]: student for student in deleted
    }

    with st.form("restore_student_form"):
        selected_id = st.selectbox(
            "Select Student to Recover",
            options=list(student_records.keys()),
            format_func=lambda sid: (
                f"{sid} - {student_records[sid][1]}"
            )
        )

        confirm_restore = st.checkbox(
            "I confirm that I want to restore this student."
        )

        restore_button = st.form_submit_button(
            "♻️ Restore Student"
        )

    if restore_button:
        if not confirm_restore:
            st.error("Please confirm before restoring.")
            return

        try:
            restored = restore_student(selected_id)

            if restored:
                st.session_state.recovery_success = (
                    "Student recovered successfully!"
                )
                st.rerun()
            else:
                st.warning("Student not found in Recycle Bin.")

        except ValueError as error:
            st.error(str(error))
        except sqlite3.Error:
            st.error("Database error during recovery.")


# Run independently for local testing
if __name__ == "__main__":
    show_recovery_page()
