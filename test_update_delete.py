
import tempfile
import os
from unittest.mock import patch

import database
import recovery


def test_update_delete():
    # Create a separate database for testing
    with tempfile.TemporaryDirectory() as temp_dir:
        test_db = os.path.join(temp_dir, "test_students.db")

        # Make both modules use the test database
        with patch.object(database, "DATABASE_NAME", test_db), \
             patch.object(recovery, "DATABASE_NAME", test_db):

            database.create_table()

            # Add test students
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
            assert database.delete_student(sita_id) is True

            students = database.get_students()

            assert len(students) == 1
            assert students[0][0] == ram_id

            # Verify deleted student is in Recycle Bin
            deleted = recovery.get_deleted_students()
            assert len(deleted) == 1
            assert deleted[0][0] == sita_id

            print("Delete test passed!")
            print("Recycle Bin test passed!")
            print("All update/delete tests passed!")


if __name__ == "__main__":
    test_update_delete()
