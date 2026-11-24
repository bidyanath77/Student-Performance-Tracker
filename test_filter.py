import sqlite3
import pytest
from filter_students import filter_students


@pytest.fixture
def conn():
    connection = sqlite3.connect(":memory:")

    connection.execute("""
        CREATE TABLE students (
            student_id INTEGER PRIMARY KEY,
            student_name TEXT,
            marks REAL,
            attendance REAL,
            study_hours REAL
        )
    """)

    connection.executemany("""
        INSERT INTO students VALUES (?, ?, ?, ?, ?)
    """, [
        (1, "Alice", 85, 90, 5),
        (2, "Bob", 60, 75, 3),
        (3, "Charlie", 40, 50, 1)
    ])

    connection.commit()
    yield connection
    connection.close()


def test_filter_by_marks(conn):
    result = filter_students(conn, min_marks=80)
    assert len(result) == 1
    assert result[0]["student_name"] == "Alice"


def test_filter_by_attendance(conn):
    result = filter_students(conn, min_attendance=80)
    assert len(result) == 1
    assert result[0]["student_name"] == "Alice"


def test_filter_by_study_hours(conn):
    result = filter_students(conn, min_study_hours=3)
    assert len(result) == 2


def test_combined_filters(conn):
    result = filter_students(
        conn,
        min_marks=50,
        min_attendance=70,
        min_study_hours=3
    )
    assert len(result) == 2


def test_no_matching_students(conn):
    result = filter_students(conn, min_marks=100)
    assert result == []