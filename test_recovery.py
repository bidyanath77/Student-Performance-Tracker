import sqlite3
import pytest
import recovery


@pytest.fixture
def test_db(tmp_path, monkeypatch):
    db_path = tmp_path / "test_recovery.db"
    monkeypatch.setattr(recovery, "DATABASE_NAME", str(db_path))

    with sqlite3.connect(db_path) as conn:
        conn.execute("""
            CREATE TABLE students (
                student_id INTEGER PRIMARY KEY,
                student_name TEXT NOT NULL,
                marks REAL,
                attendance REAL,
                study_hours REAL
            )
        """)

        conn.execute("""
            INSERT INTO students
            VALUES (1, 'Test Student', 85, 90, 5)
        """)

    return db_path


def test_empty_recycle_bin(test_db):
    assert recovery.get_deleted_students() == []


def test_move_to_recycle_bin(test_db):
    assert recovery.move_to_recycle_bin(1) is True

    deleted = recovery.get_deleted_students()
    assert len(deleted) == 1
    assert deleted[0][0] == 1


def test_removed_from_active_records(test_db):
    recovery.move_to_recycle_bin(1)

    with sqlite3.connect(test_db) as conn:
        students = conn.execute(
            "SELECT * FROM students"
        ).fetchall()

    assert students == []


def test_restore_student(test_db):
    recovery.move_to_recycle_bin(1)
    assert recovery.restore_student(1) is True

    with sqlite3.connect(test_db) as conn:
        student = conn.execute(
            "SELECT * FROM students WHERE student_id = 1"
        ).fetchone()

    assert student == (1, "Test Student", 85, 90, 5)


def test_removed_from_bin_after_restore(test_db):
    recovery.move_to_recycle_bin(1)
    recovery.restore_student(1)

    assert recovery.get_deleted_students() == []


def test_delete_nonexistent_student(test_db):
    assert recovery.move_to_recycle_bin(999) is False


def test_restore_nonexistent_student(test_db):
    assert recovery.restore_student(999) is False


def test_prevent_duplicate_student_id(test_db):
    recovery.move_to_recycle_bin(1)

    with sqlite3.connect(test_db) as conn:
        conn.execute("""
            INSERT INTO students
            VALUES (1, 'Another Student', 70, 80, 4)
        """)

    with pytest.raises(ValueError):
        recovery.restore_student(1)

    assert len(recovery.get_deleted_students()) == 1

    with sqlite3.connect(test_db) as conn:
        student = conn.execute(
            "SELECT student_name FROM students WHERE student_id = 1"
        ).fetchone()

    assert student == ("Another Student",)