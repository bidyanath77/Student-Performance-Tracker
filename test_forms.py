import unittest
import math
from unittest.mock import patch

from forms import (
    validate_student,
    show_edit_student_form,
    show_delete_student_form
)


# ==========================================
# SPRINT 2 - STUDENT VALIDATION TESTS
# ==========================================

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


# ==========================================
# SPRINT 3 - EDIT STUDENT FORM TESTS
# ==========================================

class TestEditStudentForm(unittest.TestCase):

    # Test 16: Edit student successfully
    def test_edit_student_success(self):

        original_students = [
            (1, "Rupa", 75.0, 80.0, 4.0)
        ]

        updated_students = [
            (1, "Rupa Updated", 85.0, 90.0, 5.0)
        ]

        with patch("forms.st") as mock_st, \
             patch("forms.create_table"), \
             patch(
                 "forms.get_students",
                 side_effect=[original_students, updated_students]
             ), \
             patch(
                 "forms.database.update_student",
                 create=True
             ) as mock_update:

            mock_st.selectbox.return_value = 1
            mock_st.text_input.return_value = "Rupa Updated"

            mock_st.number_input.side_effect = [
                85.0, 90.0, 5.0
            ]

            mock_st.form_submit_button.return_value = True

            show_edit_student_form()

            mock_update.assert_called_once_with(
                1,
                "Rupa Updated",
                85.0,
                90.0,
                5.0
            )

            mock_st.rerun.assert_called_once()

    # Test 17: Reject invalid student update
    def test_edit_student_invalid_name(self):

        students = [
            (1, "Rupa", 75.0, 80.0, 4.0)
        ]

        with patch("forms.st") as mock_st, \
             patch("forms.create_table"), \
             patch(
                 "forms.get_students",
                 return_value=students
             ), \
             patch(
                 "forms.database.update_student",
                 create=True
             ) as mock_update:

            mock_st.selectbox.return_value = 1
            mock_st.text_input.return_value = " "

            mock_st.number_input.side_effect = [
                85.0, 90.0, 5.0
            ]

            mock_st.form_submit_button.return_value = True

            show_edit_student_form()

            mock_update.assert_not_called()

            mock_st.error.assert_called_with(
                "Student Name is required."
            )


# ==========================================
# SPRINT 3 - DELETE STUDENT FORM TESTS
# ==========================================

class TestDeleteStudentForm(unittest.TestCase):

    # Test 18: Prevent deletion without confirmation
    def test_delete_without_confirmation(self):

        students = [
            (1, "Rupa", 85.0, 90.0, 5.0)
        ]

        with patch("forms.st") as mock_st, \
             patch("forms.create_table"), \
             patch(
                 "forms.get_students",
                 return_value=students
             ), \
             patch(
                 "forms.database.delete_student",
                 create=True
             ) as mock_delete:

            mock_st.selectbox.return_value = 1
            mock_st.checkbox.return_value = False
            mock_st.form_submit_button.return_value = True

            show_delete_student_form()

            mock_delete.assert_not_called()

            mock_st.error.assert_called_with(
                "Please confirm before deleting the student."
            )

    # Test 19: Delete student with confirmation
    def test_delete_with_confirmation(self):

        students_before = [
            (1, "Rupa", 85.0, 90.0, 5.0)
        ]

        students_after = []

        with patch("forms.st") as mock_st, \
             patch("forms.create_table"), \
             patch(
                 "forms.get_students",
                 side_effect=[students_before, students_after]
             ), \
             patch(
                 "forms.database.delete_student",
                 create=True
             ) as mock_delete:

            mock_st.selectbox.return_value = 1
            mock_st.checkbox.return_value = True
            mock_st.form_submit_button.return_value = True

            show_delete_student_form()

            mock_delete.assert_called_once_with(1)
            mock_st.rerun.assert_called_once()


# ==========================================
# SPRINT 4 - INPUT VALIDATION AND XSS TESTS
# ==========================================

class TestSprint4Validation(unittest.TestCase):

    # Test 20: Reject student names longer than 100 characters
    def test_student_name_too_long(self):

        long_name = "A" * 101

        valid, message = validate_student(
            long_name, 85, 90, 5
        )

        self.assertFalse(valid)
        self.assertEqual(
            message,
            "Student Name must not exceed 100 characters."
        )

    # Test 21: Accept student names exactly 100 characters long
    def test_student_name_max_length(self):

        student_name = "A" * 100

        valid, message = validate_student(
            student_name, 85, 90, 5
        )

        self.assertTrue(valid)

    # Test 22: Accept legitimate special characters
    def test_student_name_special_characters(self):

        valid, message = validate_student(
            "Anne-Marie O'Connor", 85, 90, 5
        )

        self.assertTrue(valid)

    # Test 23: Accept Unicode student names
    def test_student_name_unicode(self):

        valid, message = validate_student(
            "श्रेया गुरुङ", 85, 90, 5
        )

        self.assertTrue(valid)

    # Test 24: Handle HTML-like input without crashing
    def test_html_input_handling(self):

        html_input = "<b>Test Student</b>"

        valid, message = validate_student(
            html_input, 85, 90, 5
        )

        self.assertIsInstance(valid, bool)
        self.assertIsInstance(message, str)

    # Test 25: Handle JavaScript-like input without crashing
    def test_xss_input_handling(self):

        xss_input = "<script>alert('XSS Test')</script>"

        valid, message = validate_student(
            xss_input, 85, 90, 5
        )

        self.assertIsInstance(valid, bool)
        self.assertIsInstance(message, str)

    # Test 26: Reject infinite numerical values
    def test_infinite_marks(self):

        valid, message = validate_student(
            "Rupa", math.inf, 90, 5
        )

        self.assertFalse(valid)

    # Test 27: Reject boolean values in numerical fields
    def test_boolean_marks(self):

        valid, message = validate_student(
            "Rupa", True, 90, 5
        )

        self.assertFalse(valid)


# ==========================================
# RUN ALL TESTS
# ==========================================

if __name__ == "__main__":
    unittest.main()
