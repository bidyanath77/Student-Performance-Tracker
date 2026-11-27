import database
import recovery


def test_update_delete(tmp_path, monkeypatch):

    # Create an isolated temporary database
    test_db = str(tmp_path / "test_students.db")

    monkeypatch.setattr(database, "DATABASE_NAME", test_db)

    # Support the current Recovery database configuration
    if hasattr(recovery, "DATABASE_NAME"):
        monkeypatch.setattr(recovery, "DATABASE_NAME", test_db)

    database.create_table()

    # Add two test students
    ram_id = database.add_student("Ram", 70, 90, 4)
    sita_id = database.add_student("Sita", 80, 95, 3)

    # Test UPDATE
    database.update_student(ram_id, "Ram", 85, 92, 5)

    students = database.get_students()
    ram = next(s for s in students if s[0] == ram_id)

    assert ram == (ram_id, "Ram", 85, 92, 5)

    print("Update test passed!")

    # Test DELETE
    assert database.delete_student(sita_id) is True

    students = database.get_students()

    assert len(students) == 1
    assert students[0][0] == ram_id

    print("Delete test passed!")

    # Test RECYCLE BIN
    deleted_students = recovery.get_deleted_students()

    assert len(deleted_students) == 1
    assert deleted_students[0][:5] == (
        sita_id, "Sita", 80, 95, 3
    )

    print("Recycle Bin test passed!")

    # Test RESTORE
    assert recovery.restore_student(sita_id) is True

    students = database.get_students()

    assert len(students) == 2

    sita = next(s for s in students if s[0] == sita_id)

    assert sita == (sita_id, "Sita", 80, 95, 3)

    assert recovery.get_deleted_students() == []

    print("Restore test passed!")
    print("All database and recovery checks passed!")