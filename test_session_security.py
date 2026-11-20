import unittest
from pathlib import Path
from unittest.mock import patch
from streamlit.testing.v1 import AppTest


APP_PATH = Path(__file__).resolve().parent / "app.py"

TEST_STUDENTS = [
    (1, "Test Student", 80, 90, 3)
]


class TestSessionSecurity(unittest.TestCase):

    def start_app(self):
        app = AppTest.from_file(str(APP_PATH))

        app.session_state["logged_in"] = False

        app.run(timeout=30)

        self.assertEqual(len(app.exception), 0)

        return app

    def perform_login(self, app, username, password):

        self.assertEqual(len(app.text_input), 2)

        app.text_input[0].set_value(username)
        app.text_input[1].set_value(password)

        login_button = next(
            button
            for button in app.button
            if button.label == "Login"
        )

        login_button.click()
        app.run(timeout=30)

        self.assertEqual(len(app.exception), 0)

        return app

    # Test 1: Unauthorized access
    @patch("database.create_table")
    def test_dashboard_blocked_without_login(
        self, mock_create_table
    ):
        app = self.start_app()

        self.assertFalse(
            app.session_state["logged_in"]
        )

        self.assertEqual(len(app.text_input), 2)
        self.assertEqual(len(app.sidebar.radio), 0)
        self.assertEqual(len(app.metric), 0)

        self.assertTrue(
            any(
                button.label == "Login"
                for button in app.button
            )
        )

    # Test 2: Failed login
    @patch("database.create_table")
    @patch("login.authenticate_user", return_value=False)
    def test_failed_login(
        self, mock_authenticate, mock_create_table
    ):
        app = self.start_app()

        self.perform_login(
            app, "invalid_user", "wrong_password"
        )

        self.assertFalse(
            app.session_state["logged_in"]
        )

        self.assertTrue(
            any(
                "Invalid username or password"
                in error.value
                for error in app.error
            )
        )

        self.assertEqual(len(app.sidebar.radio), 0)

        mock_authenticate.assert_called_once_with(
            "invalid_user", "wrong_password"
        )

    # Test 3: Successful login
    @patch("database.create_table")
    @patch(
        "database.get_students",
        return_value=TEST_STUDENTS
    )
    @patch("login.authenticate_user", return_value=True)
    def test_successful_login(
        self,
        mock_authenticate,
        mock_get_students,
        mock_create_table
    ):
        app = self.start_app()

        self.perform_login(
            app, "test_user", "test_password"
        )

        self.assertTrue(
            app.session_state["logged_in"]
        )

        self.assertGreater(len(app.sidebar.radio), 0)

        self.assertTrue(
            any(
                metric.label == "Total Students"
                for metric in app.metric
            )
        )

        mock_authenticate.assert_called_once_with(
            "test_user", "test_password"
        )

    # Test 4: Logout and access control
    @patch("database.create_table")
    @patch(
        "database.get_students",
        return_value=TEST_STUDENTS
    )
    @patch("login.authenticate_user", return_value=True)
    def test_logout_blocks_dashboard(
        self,
        mock_authenticate,
        mock_get_students,
        mock_create_table
    ):
        app = self.start_app()

        self.perform_login(
            app, "test_user", "test_password"
        )

        self.assertTrue(
            app.session_state["logged_in"]
        )

        logout_button = next(
            button
            for button in app.sidebar.button
            if "Logout" in button.label
        )

        logout_button.click()
        app.run(timeout=30)

        self.assertEqual(len(app.exception), 0)

        self.assertFalse(
            app.session_state["logged_in"]
        )

        self.assertEqual(len(app.text_input), 2)
        self.assertEqual(len(app.sidebar.radio), 0)
        self.assertEqual(len(app.metric), 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
