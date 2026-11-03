
import unittest
import math

from forms import validate_student


class TestStudentForm(unittest.TestCase):

    # Test 1: Valid student information
    def test_valid_student(self):
        valid, message = validate_student(
            "Rupa", 85, 90, 5
        )
        self.assertTrue(valid)

    # Test 2: Empty student name
    def test_empty_student_name(self):
        valid, message = validate_student(
            "", 85, 90, 5
        )
        self.assertFalse(valid)
        self.assertEqual(message, "Student Name is required.")

    # Test 3: Student name with only spaces
    def test_whitespace_student_name(self):
        valid, message = validate_student(
            "   ", 85, 90, 5
        )
        self.assertFalse(valid)

    # Test 4: Marks above 100
    def test_marks_above_100(self):
        valid, message = validate_student(
            "Rupa", 120, 90, 5
        )
        self.assertFalse(valid)

    # Test 5: Negative marks
    def test_negative_marks(self):
        valid, message = validate_student(
            "Rupa", -10, 90, 5
        )
        self.assertFalse(valid)

    # Test 6: Attendance above 100
    def test_attendance_above_100(self):
        valid, message = validate_student(
            "Rupa", 85, 110, 5
        )
        self.assertFalse(valid)

    # Test 7: Negative attendance
    def test_negative_attendance(self):
        valid, message = validate_student(
            "Rupa", 85, -5, 5
        )
        self.assertFalse(valid)

    # Test 8: Negative study hours
    def test_negative_study_hours(self):
        valid, message = validate_student(
            "Rupa", 85, 90, -2
        )
        self.assertFalse(valid)

    # Test 9: Study hours above 24
    def test_study_hours_above_24(self):
        valid, message = validate_student(
            "Rupa", 85, 90, 30
        )
        self.assertFalse(valid)

    # Test 10: Boundary values
    def test_boundary_values(self):
        valid, message = validate_student(
            "Rupa", 0, 100, 24
        )
        self.assertTrue(valid)

    # Test 11: Invalid student name type
    def test_invalid_student_name_type(self):
        valid, message = validate_student(
            None, 85, 90, 5
        )
        self.assertFalse(valid)

    # Test 12: Invalid marks type
    def test_invalid_marks_type(self):
        valid, message = validate_student(
            "Rupa", "eighty", 90, 5
        )
        self.assertFalse(valid)

    # Test 13: Invalid attendance type
    def test_invalid_attendance_type(self):
        valid, message = validate_student(
            "Rupa", 85, "ninety", 5
        )
        self.assertFalse(valid)

    # Test 14: Invalid study hours type
    def test_invalid_study_hours_type(self):
        valid, message = validate_student(
            "Rupa", 85, 90, "five"
        )
        self.assertFalse(valid)

    # Test 15: Invalid numerical value (NaN)
    def test_nan_marks(self):
        valid, message = validate_student(
            "Rupa", math.nan, 90, 5
        )
        self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main()
