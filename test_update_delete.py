import tempfile
import os
import database

def test_update_delete():
    # Create a temporary database for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        original_db = database.DATABASE_NAME
        database.DATABASE_NAME = os.path.join(temp_dir, "test_students.db")

        try:
            database.create_table()

            # Add two test students
            ram_id = database.add_student("Ram", 70, 90, 4)
            sita_id = database.add_student("Sita", 80, 95, 3)

            # Test UPDATE
            database.update_student(ram_id, "Ram", 85, 92, 5)

            students = database.get_students()
            ram = next(s for s in students if s[0] == ram_id)

            assert ram[2] == 85
            assert ram[3] == 92
            assert ram[4] == 5

            print("Update test passed!")

            # Test DELETE
            database.delete_student(sita_id)

            students = database.get_students()

            assert len(students) == 1
            assert students[0][0] == ram_id

            print("Delete test passed!")
            print("All Sprint 3 database tests passed!")

        finally:
            database.DATABASE_NAME = original_db


if __name__ == "__main__":
    test_update_delete()