
import unittest
from pathlib import Path
from unittest.mock import patch

from streamlit.testing.v1 import AppTest


# Path to the main Streamlit application
APP_FILE = str(Path(__file__).with_name("app.py"))

# Sample student data for testing
STUDENTS = [
    (1, "Asha", 80.0, 90.0, 3.0),
    (2, "Ravi", 90.0, 95.0, 4.0),
    (3, "Mina", 70.0, 85.0, 2.0),
]


class TestDashboard(unittest.TestCase):

    def start_app(self, students):
        # Mock the database to protect real student records
        with patch("database.create_table"), \
             patch("database.get_students", return_value=students):

            app = AppTest.from_file(APP_FILE).run(timeout=20)

        self.assertEqual(len(app.exception), 0)
        return app

    # Test 1: Dashboard metrics
    
    def test_dashboard_metrics(self):
        app = self.start_app(STUDENTS)

        metrics = {
            item.label: str(item.value)
            for item in app.metric
        }

        self.assertEqual(metrics["Total Students"], "3")
        self.assertEqual(metrics["Average Marks"], "80.0%")
        self.assertEqual(metrics["Average Attendance"], "90.0%")
        self.assertEqual(metrics["Average Study Hours"], "3.0")

    # Test 2: Empty database
    
    def test_empty_database(self):
        app = self.start_app([])

        metrics = {
            item.label: str(item.value)
            for item in app.metric
        }

        self.assertEqual(metrics["Total Students"], "0")

        self.assertTrue(
            any(
                "No student records yet" in message.value
                for message in app.info
            )
        )

    # Test 3: Dashboard refresh button
    
    def test_refresh_button(self):
        with patch("database.create_table"), \
             patch("database.get_students", return_value=STUDENTS):

            app = AppTest.from_file(APP_FILE).run(timeout=20)

            self.assertEqual(len(app.exception), 0)

            app.sidebar.button[0].click().run(timeout=20)

        self.assertEqual(len(app.exception), 0)

        self.assertTrue(
            any(
                "Dashboard refreshed successfully!" in message.value
                for message in app.sidebar.success
            )
        )

    # Test 4: View Students page
    
    def test_view_students_page(self):
        with patch("database.create_table"), \
             patch("database.get_students", return_value=STUDENTS):

            app = AppTest.from_file(APP_FILE).run(timeout=20)

            app.sidebar.radio[0].set_value(
                "View Students"
            ).run(timeout=20)

        self.assertEqual(len(app.exception), 0)

        self.assertTrue(
            any(
                "Total students in database: 3" in message.value
                for message in app.success
            )
        )

    # Test 5: Dashboard updates student count
    
    def test_student_count_updates(self):
        with patch("database.create_table"), \
             patch(
                 "database.get_students",
                 return_value=STUDENTS
             ) as get_students:

            app = AppTest.from_file(APP_FILE).run(timeout=20)

            self.assertEqual(
                str(app.metric[0].value), "3"
            )

            # Simulate one additional student
            get_students.return_value = STUDENTS + [
                (4, "Nisha", 88.0, 92.0, 5.0)
            ]

            app.run(timeout=20)

        self.assertEqual(len(app.exception), 0)

        self.assertEqual(
            str(app.metric[0].value), "4"
        )
        
 # Test 6: Edit Student navigation
    
    def test_edit_student_navigation(self):
        with patch("database.create_table"), \
             patch("database.get_students", return_value=STUDENTS), \
             patch("forms.show_edit_student_form") as edit_form:

            app = AppTest.from_file(APP_FILE).run(timeout=20)

            app.sidebar.radio[0].set_value(
                "Edit Student"
            ).run(timeout=20)

            self.assertEqual(len(app.exception), 0)
            edit_form.assert_called_once()
            
            
    # Test 7: Delete Student navigation
    
    def test_delete_student_navigation(self):
        with patch("database.create_table"), \
             patch("database.get_students", return_value=STUDENTS), \
             patch("forms.show_delete_student_form") as delete_form:

            app = AppTest.from_file(APP_FILE).run(timeout=20)

            app.sidebar.radio[0].set_value(
                "Delete Student"
            ).run(timeout=20)

            self.assertEqual(len(app.exception), 0)
            delete_form.assert_called_once()


if __name__ == "__main__":
    unittest.main(verbosity=2)
