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

            # Simulate selecting a student
            mock_st.selectbox.return_value = 1

            # Simulate entering updated information
            mock_st.text_input.return_value = "Rupa Updated"

            mock_st.number_input.side_effect = [
                85.0, 90.0, 5.0
            ]

            # Simulate clicking Update Student
            mock_st.form_submit_button.return_value = True

            # Run edit student form
            show_edit_student_form()

            # Verify database update was requested
            mock_update.assert_called_once_with(
                1,
                "Rupa Updated",
                85.0,
                90.0,
                5.0
            )

            # Verify form refresh
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

            # Invalid empty student name
            mock_st.text_input.return_value = " "

            mock_st.number_input.side_effect = [
                85.0, 90.0, 5.0
            ]

            mock_st.form_submit_button.return_value = True

            show_edit_student_form()

            # Database update should not happen
            mock_update.assert_not_called()

            # Validation error should be displayed
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

            # Confirmation checkbox is not selected
            mock_st.checkbox.return_value = False

            mock_st.form_submit_button.return_value = True

            show_delete_student_form()

            # Verify student was not deleted
            mock_delete.assert_not_called()

            # Verify error message
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

            # Confirmation checkbox is selected
            mock_st.checkbox.return_value = True

            mock_st.form_submit_button.return_value = True

            show_delete_student_form()

            # Verify correct student deletion was requested
            mock_delete.assert_called_once_with(1)

            # Verify form refresh
            mock_st.rerun.assert_called_once()


# ==========================================
# RUN ALL TESTS
# ==========================================

if __name__ == "__main__":
    unittest.main()
