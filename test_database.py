import sqlite3
import tempfile
from pathlib import Path
from unittest.mock import patch

import database


def test_database():
    # Create a temporary database for testing
    with tempfile.TemporaryDirectory() as folder:
        test_db = str(Path(folder) / "test_students.db")

        with patch.object(database, "DATABASE_NAME", test_db):

            # Create the students table
            database.create_table()

            # Add a test student
            student_id = database.add_student(
                "Test Student", 85, 90, 4
            )

            # Retrieve students
            students = database.get_students()

            # Check the saved information
            assert len(students) == 1

            assert students[0] == (
                student_id, "Test Student", 85, 90, 4
            )

            # Check the SQLite database directly
            connection = sqlite3.connect(test_db)

            try:
                count = connection.execute(
                    "SELECT COUNT(*) FROM students"
                ).fetchone()[0]

                assert count == 1

            finally:
                connection.close()

    print("Test passed! Student saved and retrieved successfully.")


if __name__ == "__main__":
    test_database()