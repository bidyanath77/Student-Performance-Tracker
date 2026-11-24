import sqlite3
import database


def normalize_name(name):
    return " ".join(name.split()).casefold()


def find_students(search_term):
    search_term = normalize_name(search_term)

    if not search_term:
        return []

    connection = sqlite3.connect(database.DATABASE_NAME)

    try:
        connection.create_function("normalize_name", 1, normalize_name)

        cursor = connection.cursor()

        cursor.execute("""
            SELECT student_id, student_name, marks,
                   attendance, study_hours
            FROM students
            WHERE CAST(student_id AS TEXT) = ?
            OR instr(normalize_name(student_name), ?) > 0
            ORDER BY student_id
        """, (search_term, search_term))

        return cursor.fetchall()

    finally:
        connection.close()