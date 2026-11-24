
import sqlite3

DATABASE_NAME = "students.db"


def create_table():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INTEGER PRIMARY KEY AUTOINCREMENT,
            student_name TEXT NOT NULL,
            marks REAL,
            attendance REAL,
            study_hours REAL
        )
    """)

    connection.commit()
    connection.close()


def add_student(student_name, marks, attendance, study_hours):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students
        (student_name, marks, attendance, study_hours)
        VALUES (?, ?, ?, ?)
    """, (student_name, marks, attendance, study_hours))

    student_id = cursor.lastrowid

    connection.commit()
    connection.close()

    return student_id


def get_students():
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM students")

    students = cursor.fetchall()

    connection.close()

    return students

def update_student(student_id, student_name, marks, attendance, study_hours):
    connection = sqlite3.connect(DATABASE_NAME)
    cursor = connection.cursor()

    cursor.execute("""
        UPDATE students
        SET student_name = ?,
            marks = ?,
            attendance = ?,
            study_hours = ?
        WHERE student_id = ?
    """, (student_name, marks, attendance, study_hours, student_id))

    connection.commit()
    connection.close()

def delete_student(student_id):
    from recovery import move_to_recycle_bin
    return move_to_recycle_bin(student_id)


if __name__ == "__main__":
    create_table()
    print("Database initialized successfully!")