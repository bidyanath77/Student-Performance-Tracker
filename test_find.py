import sqlite3
import pytest
import database
from find import find_students


@pytest.fixture(autouse=True)
def setup_database(tmp_path, monkeypatch):
    db_path = tmp_path / "test_students.db"

    monkeypatch.setattr(database, "DATABASE_NAME", str(db_path))

    with sqlite3.connect(db_path) as conn:
        conn.execute("""
            CREATE TABLE students (
                student_id INTEGER PRIMARY KEY,
                student_name TEXT,
                marks REAL,
                attendance REAL,
                study_hours REAL
            )
        """)

        conn.executemany(
            "INSERT INTO students VALUES (?, ?, ?, ?, ?)",
            [
                (1, "Alice Smith", 85, 90, 5),
                (2, "Bob Jones", 65, 75, 3),
                (3, "Charlie Brown", 45, 60, 2)
            ]
        )


def test_find_by_id():
    result = find_students("1")
    assert len(result) == 1
    assert result[0][1] == "Alice Smith"


def test_find_by_full_name():
    result = find_students("Alice Smith")
    assert len(result) == 1


def test_find_by_partial_name():
    result = find_students("Alice")
    assert len(result) == 1


def test_case_insensitive_search():
    result = find_students("ALICE SMITH")
    assert len(result) == 1


def test_extra_spaces():
    result = find_students("  Alice   Smith  ")
    assert len(result) == 1


def test_empty_search():
    assert find_students("") == []


def test_nonexistent_student():
    assert find_students("Unknown Student") == []


def test_sql_injection():
    assert find_students("' OR 1=1 --") == []