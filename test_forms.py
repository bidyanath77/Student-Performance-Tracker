
import unittest
from unittest.mock import patch
from streamlit.testing.v1 import AppTest


class TestLogin(unittest.TestCase):

    # Test 1: Empty username and password
    def test_empty_login_fields(self):
        app = AppTest.from_string(
            "from login import show_login_form\n"
            "show_login_form()"
        ).run()

        app.form_submit_button[0].click().run()

        errors = [error.value for error in app.error]

        self.assertIn(
            "Please enter both username and password.",
            errors
        )

        self.assertEqual(len(app.exception), 0)

    # Test 2: Incorrect login credentials
    def test_invalid_login(self):
        with patch(
            "login.authenticate_user",
            return_value=False
        ):
            app = AppTest.from_string(
                "from login import show_login_form\n"
                "show_login_form()"
            ).run()

            app.text_input[0].set_value("wronguser")
            app.text_input[1].set_value("WrongPassword123")

            app.form_submit_button[0].click().run()

        errors = [error.value for error in app.error]

        self.assertIn(
            "Invalid username or password.",
            errors
        )

        self.assertFalse(
            app.session_state.get("logged_in", False)
        )

        self.assertEqual(len(app.exception), 0)

    # Test 3: Successful login
    def test_successful_login(self):
        with patch(
            "login.authenticate_user",
            return_value=True
        ):
            app = AppTest.from_string(
                "from login import show_login_form\n"
                "show_login_form()"
            ).run()

            app.text_input[0].set_value("testteacher")
            app.text_input[1].set_value("TestPassword123")

            app.form_submit_button[0].click().run()

        self.assertTrue(
            app.session_state["logged_in"]
        )

        self.assertEqual(len(app.exception), 0)

    # Test 4: Dashboard requires login
    def test_dashboard_requires_login(self):
        with patch("database.create_table"):
            app = AppTest.from_file(
                "app.py"
            ).run(timeout=20)

        self.assertEqual(
            len(app.form_submit_button), 1
        )

        self.assertEqual(
            len(app.sidebar.radio), 0
        )

        self.assertEqual(len(app.exception), 0)

    # Test 5: Logout functionality
    def test_logout(self):
        with patch("database.create_table"), \
             patch(
                 "database.get_students",
                 return_value=[
                     (1, "Test Student", 80, 90, 3)
                 ]
             ):

            app = AppTest.from_file("app.py")

            # Simulate an authenticated session
            app.session_state["logged_in"] = True
            app.run(timeout=20)

            # Click Logout
            app.sidebar.button[0].click().run(timeout=20)

        self.assertFalse(
            app.session_state["logged_in"]
        )

        # Dashboard navigation should disappear
        self.assertEqual(
            len(app.sidebar.radio), 0
        )

        self.assertEqual(len(app.exception), 0)


if __name__ == "__main__":
    unittest.main()
