import unittest

from forms import validate_student


class TestStudentForm(unittest.TestCase):

    def test_valid_student(self):
        valid, message = validate_student(
            "Rupa", 85, 90, 5
        )
        self.assertTrue(valid)

    def test_empty_student_name(self):
        valid, message = validate_student(
            "", 85, 90, 5
        )
        self.assertFalse(valid)

    def test_whitespace_student_name(self):
        valid, message = validate_student(
            "   ", 85, 90, 5
        )
        self.assertFalse(valid)

    def test_marks_above_100(self):
        valid, message = validate_student(
            "Rupa", 120, 90, 5
        )
        self.assertFalse(valid)

    def test_negative_marks(self):
        valid, message = validate_student(
            "Rupa", -10, 90, 5
        )
        self.assertFalse(valid)

    def test_attendance_above_100(self):
        valid, message = validate_student(
            "Rupa", 85, 110, 5
        )
        self.assertFalse(valid)

    def test_negative_attendance(self):
        valid, message = validate_student(
            "Rupa", 85, -5, 5
        )
        self.assertFalse(valid)

    def test_negative_study_hours(self):
        valid, message = validate_student(
            "Rupa", 85, 90, -2
        )
        self.assertFalse(valid)

    def test_study_hours_above_24(self):
        valid, message = validate_student(
            "Rupa", 85, 90, 30
        )
        self.assertFalse(valid)


if __name__ == "__main__":
    unittest.main()
